from shiny import App, ui, render
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Define the UI
app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_file("upload_grouped_by_engine", "Upload Grouped by Engine Data"),
            ui.input_file("upload_merged_data", "Upload Merged Data")
        ),
        ui.panel_main(
            ui.output_plot("race_plot"),
            ui.output_plot("grid_pos_plot"),
            ui.output_plot("pts_plot"),
            ui.output_plot("wins_plot"),
            ui.output_plot("tukey_test_plot")
        )
    )
)

# Define the server logic
def server(input, output, session):

    # Function to create race plot
    def create_race_plot(grouped_by_engine):
        fig, ax = plt.subplots()
        order = grouped_by_engine.sort_values('RACE', ascending=False).index
        sns.barplot(y=grouped_by_engine.index, x=grouped_by_engine['RACE'],
                    palette="Blues_d", order=order, ax=ax)
        ax.set_title('Average Race Position by Engine Type', fontsize=16, fontweight='bold')
        ax.set_ylabel('Engine Type', fontsize=14)
        ax.set_xlabel('Average Race Position', fontsize=14)
        return fig

    # Render race plot
    @output
    @render.plot
    def race_plot():
        file = input.upload_grouped_by_engine()
        if file is not None:
            grouped_by_engine = pd.read_csv(file)
            return create_race_plot(grouped_by_engine)

    # Similar functions for grid_pos_plot, pts_plot, wins_plot

    # Function to create Tukey HSD test plots
    def create_tukey_test_plots(merged_data):
        analysis_columns = ['RACE', 'GRID POS', 'W', 'PTS']
        fig, axs = plt.subplots(2, 2, figsize=(18, 10))  # 2 rows, 2 columns for subplots
        axs = axs.flatten()  # Flatten the 2x2 array to 1D for easy iteration

        for index, column in enumerate(analysis_columns):
            tukey_results = pairwise_tukeyhsd(endog=merged_data[column],
                                              groups=merged_data['ENGINE'].astype(str),
                                              alpha=0.05)
            tukey_results_df = pd.DataFrame(data=tukey_results._results_table.data[1:],
                                            columns=tukey_results._results_table.data[0])
            significant_results_df = tukey_results_df[tukey_results_df['reject'] == True]
            significant_results_df = significant_results_df.sort_values('meandiff', ascending=False)
            sns.barplot(x='meandiff', y='group1', data=significant_results_df, errorbar=None, ax=axs[index])
            axs[index].set_xlabel('Mean Difference in ' + column, fontsize=10)
            axs[index].set_ylabel('Engine Type', fontsize=10)
            axs[index].set_title('Significant Mean Differences in ' + column + ' by Engine Type', fontsize=15, fontweight="bold")
        plt.tight_layout()
        return fig

    # Render Tukey HSD test plot
    @output
    @render.plot
    def tukey_test_plot():
        file = input.upload_merged_data()
        if file is not None:
            merged_data = pd.read_csv(file)
            return create_tukey_test_plots(merged_data)

# Create the Shiny app
app = App(app_ui, server)

# Run the app
if __name__ == "__main__":
    app.run()
    