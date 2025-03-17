# -----------0. Setting up workstation-----------

import streamlit as st                                  # for interactive app development
import pandas as pd                                     # for data manipulation

df_budget_clean_final_st = pd.read_csv("clean-data/df_budget_clean_final.csv")

df_budget_clean_final_st["Year"] = df_budget_clean_final_st["Year"].astype(str)

st.set_page_config(layout="wide")

#-----------1. Creating introduction-----------
st.title("US Federal R&D Budget")
st.subheader("1976 to 2017")


st.write("")

st.image("images/filename-captial-jpg.jpg")

st.write("Source: https://www.tripadvisor.com/Attraction_Review-g28970-d143718-Reviews-U_S_Capitol-Washington_DC_District_of_Columbia.html")

st.write("")

st.subheader("In this app, you can look through over 40 years of data! Included in the dataset is information on the R&D budgets for over 10 different federal agencies. For a complete dataset, please refer to the bottom of this page.")

st.write("")
st.write("")


#-----------2. Interactive 2-------------

st.subheader("Year-over-Year R&D Budget by Department in USD")

department_budget_selectbox = st.selectbox("Choose a department to filter by:",df_budget_clean_final_st["Department"].unique())

df_department_budget = df_budget_clean_final_st[df_budget_clean_final_st["Department"]
                                                 == department_budget_selectbox]

st.line_chart(df_department_budget[["Year", "Budget"]].set_index("Year"))

total_budget = df_department_budget["Budget"].sum() // 10**9

st.write(f"Across all years measured, the {department_budget_selectbox} budgeted {total_budget} billion USD to spend.")

st.write("")
st.write("")

#-----------3. Interactive 2-----------

st.subheader("R&D Spending by President")

df_presidents = {"Year": ["1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", 
             "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", 
             "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", 
             "2015", "2016", "2017"],
    "President": ["Ford", "Ford", "Carter", "Carter", "Carter", "Carter", "Carter", "Reagan", "Reagan", "Reagan", 
                  "Reagan", "Reagan", "Reagan", "Reagan", "Bush", "Bush", "Bush", "Bush", "Clinton", "Clinton", "Clinton", 
                  "Clinton", "Clinton", "Clinton", "Clinton", "Clinton", "Bush", "Bush", "Bush", "Bush", "Bush", "Bush", 
                  "Obama", "Obama", "Obama", "Obama", "Obama", "Obama", "Obama", "Obama", "Obama", "Obama"]}

df_presidents = pd.DataFrame(df_presidents)

col1, col2 = st.columns(2)

df_budget_president = pd.merge(df_presidents, df_budget_clean_final_st, left_on = "Year", right_on = "Year", how = "outer")

with col1:
    st.write("Do picture")
with col2:
    president_radio = st.radio("Select President:", df_presidents["President"].unique())

    president_selected = df_budget_president[df_budget_president["President"] == president_radio]
    president_budget = president_selected["Budget"].sum()  # Sum R&D budget for the selected president
    st.write(f"{president_radio} spent a total of ${president_budget // 10**9} billion on R&D.")

#-----------3. Complete dataset-----------
st.subheader("Dataset Containing Federal R&D Budget Information")

st.write("")

st.dataframe(df_budget_clean_final_st, width = 4000)
