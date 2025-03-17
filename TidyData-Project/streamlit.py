# -----------0. Setting up workstation-----------

import streamlit as st                                                                # for interactive app development
import pandas as pd                                                                   # for data manipulation

df_budget_clean_final_st = pd.read_csv("clean-data/df_budget_clean_final.csv")        # reading csv

df_budget_clean_final_st["Year"] = df_budget_clean_final_st["Year"].astype(str)       # converting "Year" values to str for style on graph

st.set_page_config(layout="wide")                                                     # making page have a "wide" layout

#-----------1. Creating introduction-----------
# creating title
st.title("US Federal R&D Budget")
st.subheader("1976 to 2017")


st.write("")

# uploading image and adding source
st.image("images/filename-captial-jpg.jpg")

st.write("Source: https://www.tripadvisor.com/Attraction_Review-g28970-d143718-Reviews-U_S_Capitol-Washington_DC_District_of_Columbia.html")

st.write("")

# adding subtitle for additional context
st.subheader("In this app, you can look through over 40 years of data! Included in the dataset is information on the R&D budgets for over 10 different federal agencies. For a complete dataset, please refer to the bottom of this page.")

st.write("")
st.write("")


#-----------2. Interactive 2-------------
# creating interactive graph that plots each department's year-over-year spend
st.subheader("Year-over-Year R&D Budget by Department in USD")

department_budget_selectbox = st.selectbox("Choose a department to filter by:",df_budget_clean_final_st["Department"].unique()) # creating selectbox for department

df_department_budget = df_budget_clean_final_st[df_budget_clean_final_st["Department"]                                          # creating object that filters based on the selected department
                                                 == department_budget_selectbox]

st.line_chart(df_department_budget[["Year", "Budget"]].set_index("Year"))                                                       # plotting departments

total_budget = df_department_budget["Budget"].sum() // 10**9

st.write(f"Across all years measured, the {department_budget_selectbox} budgeted {total_budget} billion USD for R&D.")         # printing department's total R&D budget for additional context

st.write("")
st.write("")

#-----------3. Interactive 2-----------
# creating radio interactive that list each president's R&D budget
st.subheader("R&D Spending by President")

st.write("")

# creating database with presidents and associated years
df_presidents = {"Year": ["1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", 
             "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", 
             "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", 
             "2015", "2016", "2017"],
    "President": ["Ford", "Ford", "Carter", "Carter", "Carter", "Carter", "Carter", "Reagan", "Reagan", "Reagan", 
                  "Reagan", "Reagan", "Reagan", "Reagan", "Bush", "Bush", "Bush", "Bush", "Clinton", "Clinton", "Clinton", 
                  "Clinton", "Clinton", "Clinton", "Clinton", "Clinton", "Bush", "Bush", "Bush", "Bush", "Bush", "Bush", 
                  "Obama", "Obama", "Obama", "Obama", "Obama", "Obama", "Obama", "Obama", "Obama", "Obama"]}

df_presidents = pd.DataFrame(df_presidents)

df_budget_president = pd.merge(df_presidents, df_budget_clean_final_st, left_on = "Year",                                     # merging database based on "Year" using an outer bind
                               right_on = "Year", how = "outer")

column1, column2, column3, column4 = st.columns([.25,2,.25, 2])                                                               # dividing page into four parts with various widths

with column1:
    st.write("")
with column2:
    st.image("images/presidents_club.webp")
    st.write("Source: https://www.seattletimes.com/nation-world/nation-politics/in-the-presidents-club-carter-was-the-odd-man-out/")
with column3:
    st.write("")
with column4:
    president_radio = st.radio("Select President:", df_presidents["President"].unique())                                       # creating radio with list of presidents

    president_selected = df_budget_president[df_budget_president["President"] == president_radio]                              # creating object that filters based on president selected
    president_budget = president_selected["Budget"].sum()                                                                      # sum R&D budget for the selected president
    st.write(f"President {president_radio} budgeted a total of ${president_budget // 10**9} billion for R&D.")                 # printing sum of yearly budgets for each presidents and presenting in billions of USD

st.write("")
st.write("")

#-----------3. Complete dataset-----------
st.subheader("Dataset Containing Federal R&D Budget Information")

st.write("")

st.dataframe(df_budget_clean_final_st, width = 4000)                                                                           # inserting dataframe and expanding for readability
