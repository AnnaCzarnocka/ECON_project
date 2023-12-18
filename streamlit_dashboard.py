import altair as alt
import pandas as pd

engdf = pd.read_csv("engine_data.csv")

merged_data = engdf
def win(x):
  try:
    x = int(x)
  except:
    x = 0
  if x == 1:
    x = 1
  else:
    x = 0
  return x

merged_data['W'] = merged_data['RACE'].apply(win)

# Filter data for teams using Mercedes engines, handling NA values in the condition
mercedes_teams = merged_data[merged_data['ENGINE'].str.contains("Mercedes", na=False)]

# Wins by team and year chart (Line Chart)
wins_by_team_year = mercedes_teams.groupby(['Team', 'Year'])['W'].sum().reset_index()
mercedes_team_wins_over_time_alt = alt.Chart(wins_by_team_year).mark_line(point=True).encode(
    x=alt.X('Year:O', axis=alt.Axis(title='Year')),
    y=alt.Y('W:Q', axis=alt.Axis(title='Number of Wins')),
    color=alt.Color('Team:N', legend=alt.Legend(title="Teams")),
    tooltip=['Team', 'Year', 'W']
).properties(
    title='Number of Wins per Team Using Mercedes Engines Over Years',
    width=600,
    height=400
)

# Correlation between grid position and final race position chart (Scatter Plot)
grid_race_corr_chart = alt.Chart(mercedes_teams).mark_point().encode(
    x=alt.X('GRID POS:Q', axis=alt.Axis(title='Grid Position')),
    y=alt.Y('RACE:Q', axis=alt.Axis(title='Final Race Position')),
    color=alt.Color('Team:N', legend=alt.Legend(title="Teams")),
    tooltip=['GRID POS', 'RACE', 'Team']
).properties(
    title='Grid Position vs Final Race Position for Mercedes Teams',
    width=600,
    height=400
)

# Total points per team and year chart (Stacked Bar Chart)
points_by_team_year_bar_chart = alt.Chart(mercedes_teams).mark_bar().encode(
    x=alt.X('Year:O', axis=alt.Axis(title='Year')),
    y=alt.Y('sum(PTS):Q', axis=alt.Axis(title='Total Points')),
    color=alt.Color('Team:N', legend=alt.Legend(title="Teams")),
    tooltip=['Year', 'sum(PTS)', 'Team']
).properties(
    title='Total Points per Team Using Mercedes Engines Across Years',
    width=600,
    height=400
)

# Total points per team and year chart (Area Chart)
points_by_team_year_area_chart = alt.Chart(mercedes_teams).mark_area(opacity=0.5).encode(
    x=alt.X('Year:O', axis=alt.Axis(title='Year')),
    y=alt.Y('sum(PTS):Q', axis=alt.Axis(title='Total Points')),
    color=alt.Color('Team:N', legend=alt.Legend(title="Teams")),
    tooltip=['Year', 'sum(PTS)', 'Team']
).properties(
    title='Total Points Distribution Over Years (Area Chart)',
    width=600,
    height=400
)

# Concatenate the charts in a dashboard
dashboard = alt.vconcat(
    mercedes_team_wins_over_time_alt,
    grid_race_corr_chart,
    points_by_team_year_bar_chart,
    points_by_team_year_area_chart
).configure_concat(
    spacing=20
)

# Display the dashboard
dashboard

import streamlit as st

# Display the charts in Streamlit
st.title("Mercedes Engine Performance Analysis")

st.header("Number of Wins per Team Over Years")
st.altair_chart(mercedes_team_wins_over_time_alt, use_container_width=True)

st.header("Grid Position vs Final Race Position")
st.altair_chart(grid_race_corr_chart, use_container_width=True)

st.header("Total Points per Team Across Years")
st.altair_chart(points_by_team_year_bar_chart, use_container_width=True)

st.header("Total Points Distribution Over Years")
st.altair_chart(points_by_team_year_area_chart, use_container_width=True)