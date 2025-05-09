#-----------0. Workstation-----------

import streamlit as st  # for streamlit
import pandas as pd     # for data wrangling

#-----------1. Introduction----------

st.title("Quick, nobody's looking!")
st.subheader("*An interactive introduction to unsupervised machine learning*")
st.divider()
st.subheader("App Overview")
st.divider()

col1, col2, col3 = st.columns([.5,.1,1])

with col1:
    st.write("**Welcome to unsupervised machine learning!**")
    st.write("In this app, you will explore unsupervised machine learning, a form of machine learning that is used for data without labels.")
    st.write("You will have the chance to work with three different types of models in this app. The first model is a clustering model, while the other is a dimension reduction model.")

    model_select = st.radio("Choose your model type:", ["Clustering", "Dimension Reduction"]) # making interactive button for users to pivot between clustering and dimension reduction information pages

with col2:
    st.write("")

with col3:
    if model_select == "Clustering":
        st.write("Clustering helps us understand how various observations fit together. These models giving labels to observations, grouping them together based on shared attributes.")
        
        clustering_example_before = {"Length": [5.4, 7.1, 4.3, 8.6, 6.9],
                                    "Width": [12.3, 9.8, 10.5, 15.2, 13.7]} # creating fake dataset to represent what a dataset may look like before clustering
        clustering_example_after = {"Cluster": [1, 2, 1, 2, 2],
                                    "Length": [5.4, 7.1, 4.3, 8.6, 6.9],
                                    'Width': [12.3, 9.8, 10.5, 15.2, 13.7]} # creating fake dataset to show what a dataset may look like after clustering (divided into 2 clusters)
        clustering_example_before_df = pd.DataFrame(clustering_example_before)
        clustering_example_after_df = pd.DataFrame(clustering_example_after)
        
        col1, col2 = st.columns([.9,1])

        with col1:
            st.write("*Before clustering*")
            st.dataframe(clustering_example_before_df, hide_index = True) # table with no indices
        
        with col2:
             st.write("*After clustering*")
             st.dataframe(clustering_example_after_df, hide_index = True) # table with no indices
        
        st.write("The insights and labels derived from clustering can help us leverage the same dataset in the context of supervised machine learning.")
    
    else:
        st.write("Dimension reductions creates simpler datasets, allowing for more efficient analysis. These models search for similarities between variables, grouping together ones that share similar stories.")
        
        dr_example_before = {"Length": [5.4, 7.1, 4.3, 8.6, 6.9],
                             "Height": [12.3, 9.8, 10.5, 15.2, 13.7],
                             "Width": [18.1, 16.5, 15.2, 19.4, 17.3],
                             "Depth": [7.2, 5.9, 6.8, 8.1, 6.5]}      # creating fake dataset to illustrate what a dataset may look like prior to dimension reduction
        dr_example_after = {"Component A": [2.4, 1.7, 2.1, 2.9, 2.3],
                            "Component B": [0.5, -0.2, 0.3, 0.7, 0.4]} # creating fake dataset to showcase what a dataset may look like after dimension reduction (into 2 components)
        
        dr_example_before_df = pd.DataFrame(dr_example_before)
        dr_example_after_df = pd.DataFrame(dr_example_after)

        col1, col2 = st.columns([1,.9])

        with col1:
            st.write("*Before dimension reduction*")
            st.dataframe(dr_example_before_df, hide_index = True) # making table with no indices
       
        with col2:
             st.write("*After dimension reduction*")
             st.dataframe(dr_example_after_df, hide_index = True) # making table with no indices
        
        st.write("By using dimension reduction, we can unlock insights with great efficiency, allowing us to do more while limiting the burden of our work on servers and the environment.")

#-----------3. File Upload-----------

st.divider()
st.subheader("File Upload")
st.divider()

col1, col2 = st.columns([1,.5])

with col1:
    file = st.file_uploader("" , type = ["csv"]) # creating file upload spot that only accepts csv files

    if file is not None:
        df = pd.read_csv(file) # reading uploaded file
        df = df.fillna(df.mode().iloc[0]) # filling null values with mode
        df = df.select_dtypes(include=['number']) # dropping columns with non-numeric data
        st.session_state.df = df # preserving df across pages
        st.balloons() # launching balloons when file is successfuly uploaded
        st.success("You have uploaded a CSV file! Missing values have been filled with the the variable's mode value; variables containing non-numerical values have also been dropped; after this page, the data uploaded will be scaled for standardization purposes.") # notifying user dataset is uploaded and altered

    else:
        st.warning("Please upload a CSV file to continue!") # notifying users who have not uploaded a file to do so

with col2:
    st.write("")
    st.write("")
    st.write("If you are struggling to find a dataset, please visit:")
    st.markdown("""
    - [Kaggle Datasets](https://www.kaggle.com/datasets)
    - [Google Dataset Search](https://datasetsearch.research.google.com/)
    - [UCI Machine Learning Repository](https://archive.ics.uci.edu/)
    """)

#-----------4. Data Check------------
st.divider()
if file is not None:
    st.subheader("Data Check")
    st.divider()
    st.write("*Please take a moment to familiarize yourself with your data and confirm it has been correctly uploaded.*")

    col1, col2, col3 = st.columns([1,.1,1])

    with col1:
        st.write("**Dataset Preview**")
        st.dataframe(df.head(7), hide_index = True) # creating preview of uploaded dataset with no indices
    
    with col2:
        st.write("")

    with col3:
        st.write("**Dataset Description**")
        st.write(f"*Observations:* {df.shape[0]}") # printing number of observations (i.e., rows), as indicated by [0]
        st.write(f"*Variables:* {df.shape[1]}") # printing number of variables (i.e., columns), as indicated by [1]
        st.write("*Variable Names:*")
        with st.expander("Click to see variable names"): # creating drop down to see full list of variables
            for col in df.columns: # using for loop to iterate over column names and return each one
                st.write(col)
    
    st.divider()
    st.write("#### Now it's time to incorporate your dataset into your learning!")
    st.write("*Please navigate to the tab on the left side of the app and select the type of model you'd like to explore.*")
    st.divider()

else:
    st.write("")
