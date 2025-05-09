#-----------0. Workstation-----------

import streamlit as st  # for streamlit
import pandas as pd     # for data wrangling
from sklearn.preprocessing import StandardScaler   # for scaling
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt      # for plotting
import numpy as np ## for calculations

#-----------1. Introduction----------

## providing page overview

st.title("Dimension Reduction: Principal Component Analysis (PCA)")
st.divider()

st.write("**Page Overview**")
st.write("In this part of the app, you'll dive into dimension reduction through building a PCA model.")
st.write("PCA is used to combine variables in a dataset. The combined variables are called components. Although reductive, it can yield great benefits.")
st.write("For example, by reducing the number of variables, you also reduce the number of values, which allows for faster and more efficient analyses.")

if "df" in st.session_state:     # carrying over df from home page
    df = st.session_state.df
else:
    st.warning("Please revisit the home page to upload the database you would like to run through the PCA model.")
    st.divider()
    st.stop() # stopping code if csv file has not been uploaded


#-----------2. Model Setup-----------

## setting up model for fitting and evaluation

st.divider()
st.subheader("Model Setup")
st.divider()

col1, col2, col3 = st.columns([.7,.1,1])

with col1:
    st.write("Please use the slider to the right to select the number of components you would like returned.")
    st.write("For additional insights into what number you should pick, please visit the following section.")

with col2:
    st.write("")

with col3:
    st.write("")
    st.write("")
    c = st.slider("Please choose how many components you would like:",
                  min_value = 2, max_value = df.shape[1], step = 1, value = 2) # creating slider that ranges from 2 to the number of variables in the dataset
    st.write(f"Your model will have {c} components.") # listing out number of components for visibility

scaler = StandardScaler() # creating scaler
X_std_dr = scaler.fit_transform(df) # scaling dataframe

pca = PCA(n_components = c) # creating pca model where components is equal to slider value
X_pca = pca.fit_transform(X_std_dr) # fitting AND transforming data so it can be presented in tabular form


#-----------3. Results---------------

## providing users with the opportunity to preview their transformed data prior to evaluation

st.divider()
st.subheader("Results")
st.divider()
st.write("In this section, you can see a dataframe containing your newly transformed data.")
st.write("To switch the dataframe from the original to the new one, click the button labelled *Transformed Data*.")

df_pca = pd.DataFrame(X_pca, 
                      columns = [f"Component{i + 1}" for i in range(c)]) # creating dataframe for newly transformed data, where each component is given the name "Component" and the number in the order it is

st.button("Original Data", type = "secondary") # creating button with "Original Data"
if st.button("Transformed Data", type = "secondary"): # creating button with "Transformed Data" that switches dataframe
    st.dataframe(df_pca.head()) # if transformed is selected, users can view the first 5 rows of data
else:
    st.dataframe(df.head()) # if transformed is not selected, the original data will appear

#-----------4. Evaluation------------

## creating section for evaluation that will contain multiple plots to help users understand the number of components they should choose

st.divider()
st.subheader("Evaluation")
st.divider()

st.write("The evaluation section contains two scree plots. Both aim to visualize how much of the variance in the dataset can be explained by each component.")

col1, col2, col3 = st.columns([1,.1,1])

with col1:
    st.write("**Cumulative Explained Variance**")
    pca_full = PCA(n_components=df.shape[1]) # creatting pca model where components is equal to total number of variables in the chosen dataset
    X_pca_full = pca_full.fit(X_std_dr) # applying pca model
    cumulative_variance = np.cumsum(X_pca_full.explained_variance_ratio_) # calculating cumulative variance using numpy

    fig = plt.figure(figsize=(8, 8))
    plt.plot(range(1, len(cumulative_variance) + 1), # creating plot where the value of a point is the component's variance plus preceeding components
             cumulative_variance, marker = "o", 
             color = "red", linestyle= "--" ) # line is hashed and red
    plt.xlabel("Number of Components")
    plt.ylabel("Cumulative Explained Variance")
    plt.title("Cumulative Explained Variance from PCA")
    plt.xticks(range(1, len(cumulative_variance) + 1)) # creating range that includes all component variables requested by the user
    plt.grid(False) # turning off grid lines

    st.pyplot(fig) # making plot visible on streamlit

with col2:
    st.write("")

with col3:
    st.write("**Variance Explained by Each Component**")
    
    fig = plt.figure(figsize=(8, 8))
    components = range(1, len(pca_full.explained_variance_ratio_) + 1) # making a range of components that match the number of components possible for the pca analysis based on the dataset
    plt.bar(components, pca_full.explained_variance_ratio_,  # creating bar chart where column's height is the amount of variance the component explains
            color = "white", edgecolor =  "navy", hatch = "//") # where columns are white with blue hashes
    plt.xlabel("Component")
    plt.ylabel("Explained Variance")
    plt.title("Variance explained by each component from PCA")
    plt.xticks(components) # making ticks the components
    plt.grid(False) # turning off grid lines
    st.pyplot(fig) # showing plot on streamlit appp

st.write("To choose the ideal number of components, you should look for when the gradient of the curve on the left begins to shallow. The graph on the right illustrates how much of the variance each component explains.")
st.divider()