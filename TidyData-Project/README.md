# TidyData-Project
## Summary
In this project, I apply the Tidy data principles to a dataset containing information on U.S. Federal Research and Development (R&D) budgets from 1976 to 2017. In addition to applying the principles, I create visualizations, pivot tables, and an interactive app. I also provide cleaned versions of the data in both .csv and .xlsx forms. 

<hr>
<p align="center">
  <img src="https://github.com/user-attachments/assets/3c438aca-273f-4684-b10b-3613b76b3063" style="width: 100%;" />
<hr>

## Data

The data leveraged in this project is a modified version of **jonthegeek**'s [Federal Research and Development Spending by Agency](https://pages.github.com/). Spanning from 1976 to 2017, the modified version contains R&D budget information from across 13 agencies (in addition to another agency containing all other R&D expenditures!). 

After cleaning, the four variables in the dataset are...

``Budget``*: Funds alloted to R&D work in dollars

``Department``**: Organizations within the U.S. Federal Government 

``GDP``*: Gross domestic product (GDP) of the U.S. in dollars

``Year``: Fiscal year (runs from Sept. 1st to the following Oct. 31st)

*All dollar amounts have been adjusted for inflation and are in USD


<details>
<summary>**Select to see a list of all departments included</summary>


**DHS** is Department of Homeland Security 🚔

**DOC** is Department of Commerce 📈

**DOD** is Department of Defense 🪖

**DOE** is Department of Energy ⚡️

**DOT** is Department of Transportation ✈️

**EPA** is Environmental Protection Agency 🌳

**HHS** is Department of Health and Human Services ⛑️

**Interior** is Department of the Interior 🦬

**NASA** is National Aeronautics and Space Administration 🚀

**NIH** is National Institutes of Health 💉

**NSF** is National Science Foundation 🧪

**USDA** is U.S. Department of Agriculture 🌾

**VA** is Department of Veteran Affairs 🎖️
</details>


## Instructions
Before running the code, please download the dataset ``fed_rd_year&gdp.csv`` located in the ``data`` folder.

After downloading the dataset, please import the following libraries*:

``pandas``

``seaborn``

``matplotlib.pyplot``

``numpy``

*If you are having issues, it may be necessary to run the command ``!pip install`` followed by the desired library.


## Process

When cleaning the data, I applied Hadley Wickham's three [Tidy data principles](https://vita.had.co.nz/papers/tidy-data.pdf). These principles include...

1) Each variable must have its own column
  
2) Each observation must have its own row
  
3) Each value must have its own cell

The purpose of having Tidy data is to facilitate easier consumption and analysis, allowing for stakeholders to use your data to make a **real, tangible impact on the world.**

To support my work, I also utilized [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) to help with data wrangling.

## Sample Visualizations


<p align="center">
  <img src="https://github.com/g-hodge/Hodge-Data-Science-Portfolio/blob/main/TidyData-Project/images/barchart-r&d.png?raw=true" width="35%" style="display:inline-block; margin-right: 10px;">
  <img src="https://github.com/g-hodge/Hodge-Data-Science-Portfolio/blob/main/TidyData-Project/images/linechart-gdp.png?raw=true" width="45%" style="display:inline-block;">
</p>

⬅️ On the left is a bar graph illustrating how much each department studied budgeted for R&D expenses over all years measured

➡️ On the right is a line graph showcasing year-over-year growth in GDP


## Streamlit Instructions
To access the app coded for in ``streamlit.py``, please follow these instructions:


1) Download the file ``df_budget_clean_final.csv`` nested within ``clean_data``

2) Open your terminal

3) Enter ``streamlit run streamlit.py``

4) Wait for a new browser window to open up, run the code, and have fun!


## Sources

*Tidy data: https://vita.had.co.nz/papers/tidy-data.pdf*

*Pandas Cheat Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf*

*Washington, DC Image: https://vastphotos.com/photo/washington-monument-jefferson-memorial-sunrise-ii-by-tim-lo-monaco*
