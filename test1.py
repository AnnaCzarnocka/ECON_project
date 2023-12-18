import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Load the datasets
@st.cache_data
def load_data():
    grouped_by_engine = pd.read_csv('grouped_by_engine.csv')
    merged_data = pd.read_csv('merge_data_f.csv')
    return grouped_by_engine, merged_data

grouped_by_engine, merged_data = load_data()

def create_race_plot(grouped_by_engine):
    fig, ax = plt.subplots()
    order = grouped_by_engine.sort_values('RACE', ascending=False).index
    sns.barplot(y=grouped_by_engine.index, x=grouped_by_engine['RACE'], 
                palette="Blues_d", order=order, ax=ax)
    ax.set_title('Average Race Position by Engine Type', fontsize=16, fontweight='bold')
    ax.set_ylabel('Engine Type', fontsize=14)
    ax.set_xlabel('Average Race Position', fontsize=14)
    return fig

def create_grid_pos_plot(grouped_by_engine):
    fig, ax = plt.subplots()
    order = grouped_by_engine.sort_values('GRID POS', ascending=False).index
    sns.barplot(y=grouped_by_engine.index, x=grouped_by_engine['GRID POS'], 
                palette="Blues_d", order=order, ax=ax)
    ax.set_title('Average Grid Position by Engine Type', fontsize=16, fontweight='bold')
    ax.set_ylabel('Engine Type', fontsize=14)
    ax.set_xlabel('Average Grid Position', fontsize=14)
    return fig

def create_pts_plot(grouped_by_engine):
    fig, ax = plt.subplots()
    order = grouped_by_engine.sort_values('PTS', ascending=False).index
    sns.barplot(y=grouped_by_engine.index, x=grouped_by_engine['PTS'], 
                palette="Blues_d", order=order, ax=ax)
    ax.set_title('Total Points by Engine Type', fontsize=16, fontweight='bold')
    ax.set_ylabel('Engine Type', fontsize=14)
    ax.set_xlabel('Total Points', fontsize=14)
    return fig

def create_wins_plot(grouped_by_engine):
    fig, ax = plt.subplots()
    order = grouped_by_engine.sort_values('W', ascending=False).index
    sns.barplot(y=grouped_by_engine.index, x=grouped_by_engine['W'], 
                palette="Blues_d", order=order, ax=ax)
    ax.set_title('Count of Wins by Engine Type', fontsize=16, fontweight='bold')
    ax.set_ylabel('Engine Type', fontsize=14)
    ax.set_xlabel('Count of Wins', fontsize=14)
    return fig

# Display each plot in its own section
st.header('Average Race Position')
race_fig = create_race_plot(grouped_by_engine)
st.pyplot(race_fig)

st.header('Average Grid Position')
grid_pos_fig = create_grid_pos_plot(grouped_by_engine)
st.pyplot(grid_pos_fig)

st.header('Total Points')
pts_fig = create_pts_plot(grouped_by_engine)
st.pyplot(pts_fig)

st.header('Count of Wins')
wins_fig = create_wins_plot(grouped_by_engine)
st.pyplot(wins_fig)

# Function to create the Tukey HSD test plots
def create_tukey_test_plots(merged_data):
    analysis_columns = ['RACE', 'GRID POS', 'W', 'PTS']
    fig, axs = plt.subplots(2, 2, figsize=(18, 10)) # 2 rows, 2 columns for subplots
    axs = axs.flatten() # Flatten the 2x2 array to 1D for easy iteration

    for index, column in enumerate(analysis_columns):
        tukey_results = pairwise_tukeyhsd(endog=merged_data[column],
                                          groups=merged_data['ENGINES'].astype(str),
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

# Streamlit layout
st.title('F1 Engine Performance Dashboard')

# Tukey HSD Test Plots
st.header('Tukey HSD Test Results')
tukey_test_fig = create_tukey_test_plots(merged_data)
st.pyplot(tukey_test_fig)
