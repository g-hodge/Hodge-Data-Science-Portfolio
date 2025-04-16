#-----------0. Setting up workstation-----------

import streamlit as st  ## for streamlit
import pandas as pd     ## for data wrangling

#-----------1. Creating introduction-------------

st.title("Are you ready for machine learning?")
st.subheader("*Ready or not...here it comes...*")
st.divider()

column1, column2 = st.columns([.3,.5])
with column1:
    st.image("images/shutterstock_1097793092-scaled.jpg", use_column_width = True)

with column2:
    st.write("Through this app, you will have the opportunity to build and evaluate supervised machine learning models.")

    st.write("When learning, you will have the option to upload your own file, allowing you to have a personal connection with your learning.")
    st.write("After uploading, all null values will take the median value of the variable.")

st.divider()
column1, column2 = st.columns([.3,.5])
with column1:
    st.image("images/istockphoto-170462856-612x612.jpg", use_column_width = True)

with column2:
    st.write("If you are struggling to find a dataset, please visit:")
    st.markdown("""
    - [Kaggle Datasets](https://www.kaggle.com/datasets)
    - [Google Dataset Search](https://datasetsearch.research.google.com/)
    - [UCI Machine Learning Repository](https://archive.ics.uci.edu/)
    """)
#-----------2. File Upload-----------------------

st.divider()
st.subheader("*Time to upload a file*")
st.divider()

file = st.file_uploader("" , type = ["csv"])     ## creating placde to upload ONLY csv files

if file is not None:
    df = pd.read_csv(file)
    df = df.fillna(df.median(numeric_only=True)) ## filling null values with the median for simplicity
    st.session_state.df = df                     ## making it possible to access df across pages
    st.balloons()
    st.success("You have uploaded a CSV file! Missing values have been filled with the the variable's median value.")
    st.write("Dataset preview:")
    st.dataframe(df.head())
else:
    st.warning("Please upload a CSV file to continue!")

#-----------3. Model Selection-------------------

st.divider()
st.subheader("*Let's choose a model*")
st.divider()

column1, column2 = st.columns([.5,.5])
with column1:
    st.write("Now it is time to choose a model. You will either train a **Linear Regression** or **K-Nearest Neighbors model**.")
    st.write("If you're using *categorical data* for the target variable (i.e., the variable you're predicting), we recommend using K-Nearest Neighbors model.")
    st.write("If it is *numerical data*, we recommend using a Linear Regression model.")
    st.write("Regardless of the model that you choose, your feature variables (i.e., the variables you're asking the model the use to predict an outcome) should be *numerical data*.")
    st.write("Now that you know what to do, please go to the side bar and click the tab with the model we recommend using.")
with column2:
    column1, column2, column3 = st.columns([.5, 2, .25])
    with column2:
        st.image("images/360_F_227570924_A3T5Zw5EYnW3cAPeSphGMPh23zGCnFan.jpg", use_column_width=True)
    st.divider()
    column1, column2, column3 = st.columns([.5, 2, .25])
    with column2:
        st.image("images/istockphoto-1049887368-612x612.jpg", use_column_width=True)

st.divider()

st.write("*Please visit ")

