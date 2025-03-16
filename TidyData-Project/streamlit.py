import streamlit as st                                  # for interactive app development
import pandas as pd                                     # for data manipulation


df_budget_clean_final_st = pd.read_csv("clean-data/df_budget_clean_final.csv")

st.title("US Federal R&D Budget - 1978 to 2015")

st.subheader("In this app, you can look through over 35 years of data! Included in the dataset is information on the Federal R&D budget across 14 different departments as well as additional information on the country's GDP.")

st.write(df_budget_clean_final_st)
