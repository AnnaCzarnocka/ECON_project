# [Requirements](https://github.com/doctor-phil/ECON323_2023_Fall/blob/main/final_project.md#requirements)

- 25% of final grade
- Involves **data analysis and visualisation**
- Practice of coding skills with **Python**
- Main grading criteria:
    - **Originality** and/or **innovativeness** of the idea.
    - Use of well-grounded programming techniques, either those learned in the course or that go above and beyond the course material.
    - **Clear communication of a lesson/message from the data, both in text and visualisation.**
    - Clarity and quality of the code, and readable text that explains each step.
- **Contents:**
    - Introduction that explains the research question in detail,
    - Analysis section,
    - Conclusions section that explains how we have used the analysis to answer our research question.
- **Length:**
    - e.g. **3-5 "pages**" of Jupyter notebooks,
    - no maximum limit to the length of notebooks, but we will not be awarded or penalised for a long notebook.

# Strategies

- Use knowledge and tools from DSCI 320 course - websites and materials.
- See [previous final projects](https://datascience.quantecon.org/theme/projects.html).
- We can build a new dataset - it could compensate for less interesting analysis and visualisation.
- OR: If we do a highly interactive visualisation, it could compensate for using a preexisting dataset. - **StreamLit and/or Shiny Python package**
- We can use the dashboard from my project from VIZ 320
- AND/OR: If we use some of the new machine learning techniques you learned in the class, you can get by with less interesting datasets. - YES

# Plan Friday

- Camilo has the code for the **EDA** and for **showing what team engine is dominant**, which will be either **Mercedes or Ferrari**. He’s working on this and is almost done.
- [x]  Once we find that either Mercedes or Ferrari is the dominant team engine, I think that the easiest way we can go is by **analysing all the teams that use Mercedes engines** for instance. So, we can:
    - using the “merge_data_f.csv” file
        - Camilo created this CSV that is the final_data.csv but with more columns that are useful for the analysis. So the analysis by teams could be done with this CSV
    - [x]  make graphs that show facts about the teams that use Mercedes engines.
        - [x]  That is what Gabor should think about.
        - [x]  What can be interesting to show for the analysis?
        - [x]  For example the number of wins across times,
        - [x]  The correlation between grid position and final position of all the races, etc.
        - [x]  For example, a graph that shows the number of wins for this group of teams across the years of analysis.
    - [x]  Once we have all these graphs, we can create the final dashboard and we will conclude with it.
- [x]  So Anna, Gabor and AV can focus on creating the graphs for the team Mercedes
- [x]  Whatever progress you guys make, can you please share it on the Whatsapp group chat so Ansh can work on it tomorrow?

# Plan Monday

# Do these visualisations:

## Clearing what I already made

- [ ]  0. Clean up my Github and Desktop folder.
- [ ]  1. Go to the Google Colab and see changes made.
- [ ]  2. Make sure the Contents are well divided:
    - *Introduction that explains the research question in detail,*
    - *Analysis section,*
    - *Conclusions section that explains how we have used the analysis to answer our research question.*
- [ ]  3. Clean up my code possibly, add code descriptions to each code line *(”Clear communication of a lesson/message from the data, both in text and visualisation.” , “Clarity and quality of the code, and readable text that explains each step.”).*
- [ ]  4. Upload to chat the materials merged from the DSCI 320 course.
- [ ]  5. Try adding quickly dashboard user interactions to the vizzes that I have in my dashboard - from the VIZ 320.
- [ ]  6. Keep the graphs with the nr of wins and total points. They show how Mercedes dominate other teams. Mercedes team also use Mercedes engines - it biases because its much higher.

## Add Ferrari

- [ ]  7. The same graphs as I already did - but for Ferrari, this time also with the “Grid Position vs …”.
- [ ]  8. Add interpretation to graphs I’ve already done.

## Bias - free

- [ ]  9. Do the same analysis as I did but for teams that use Mercedes engines but without Mercedes team.
- [ ]  10. The same analysis but for all teams with Ferrari engine without the Ferrari team.
- [ ]  11. Then we’ll see how engine selection correlates to everything else.

## Additional

- [ ]  12. Maybe play with the regression - add interactions, logs, ^2, coefficients etc - but it has to make sense; then add interpretations.
- [ ]  13. Quick clustering with points / engines.
- [ ]  14. See for other machine learning techniques from class - and from my R Pubs three unsupervised learning projects.

## Finalising

- [ ]  15. Once I’ve done this - pass the code to group chat.
- [ ]  16. Create a final dashboard with Camilo - StreamLit and/or Shiny Python package
- [ ]  17. Then we’ll add the final comments to that and conclusion.
- [ ]  18. Add my Github link to the project for the professor to see our work in progress: https://github.com/AnnaCzarnocka/ECON_project/tree/de40737445170884170d7f2d5c7ef33ac158c892
- [ ]  18. Camilo at the end will combine it all in the ipynb file and we’ll submit.
