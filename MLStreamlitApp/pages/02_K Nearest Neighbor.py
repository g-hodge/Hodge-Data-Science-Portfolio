#-----------0. Setting up workstation-----------

import streamlit as st    ## for app
import pandas as pd       ## for data wrangling
import numpy as np        ## computing

from sklearn.model_selection import train_test_split                                 ## for data splitting tool for training and testing
from sklearn.preprocessing import StandardScaler                                     ## for scaling         
from sklearn.neighbors import KNeighborsClassifier                                   ## for k-nearest neighbor model
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report  ## for evaluation
import matplotlib.pyplot as plt                                                      ## for plotting
import seaborn as sns                                                                ## for visualization
plt.rcParams.update({'font.family': 'sans-serif', 'font.size': 12})

#-----------1. Introduction to KNN--------------

st.title("K-Nearest Neighbors Model")
st.divider()
column1, column2 = st.columns([.5,.3])
with column1:
    st.write("On this page, you'll construct and evaluate a K-Nearest Neighbor model.")
    st.write("You have chosen to work with a K-Nearest Neighbor model as your target variable is categorical.")
with column2:
    st.image("images/istockphoto-453035943-612x612.jpg")

st.divider()

#-----------2. Input----------------------------

if "df" in st.session_state:     ## carrying over df from home page
    df = st.session_state.df
else:
    st.write("Head back to the home page! You still need to upload a dataset.")
    st.stop()

st.write("Here's a quick look at your dataset:")
st.write(df.head())

st.divider()
st.subheader("*Model building time*")
st.divider()

numerical_columns = df.select_dtypes(include=["number"]).columns.tolist()         ## creating list of numerical variables
categorical_columns = df.select_dtypes(exclude=["number"]).columns.tolist()       ## creating list of categorical variables

column1, column2 = st.columns([1, 1])
with column1:
    X_select = st.multiselect("Please select your feature variable(s):",          ## allowing user to select multiple numerical variables
                              numerical_columns)
with column2:
    st.write("")
    st.write("")
    st.write(f"**Feature Variable(s):** {', '.join(X_select)}")

column1, column2 = st.columns([1, 1])
with column1:
    y_select = st.selectbox("Please select your target variable:",                ## allowing user to select one categorical variable
                            categorical_columns)
with column2:
    st.write("")
    st.write("")
    st.write(f"**Target Variable:** {y_select}")
scale = st.radio("Please select whether you would like to scale your data:", ["Yes", "No"])   ## creating button to decide if data is scaled or not

k = st.slider("Please choose the number of neighbors (i.e., k):", min_value=1,                ## creating sldier to alter k-values
              max_value=20, step=2, value=1)

#-----------3. Model Training and Evaluation----

if X_select and y_select:                       ## creating if statement; if both feature and target are chosen, the rest of the code will appear
    X = df[X_select]
    y = df[y_select]

    feature_names = X.columns                   ## preserving column names

    X_train, X_test, y_train, y_test = train_test_split(X, y,               ## training to have X predict y
                                                        test_size = 0.2,    ## 20% testing-80% training split
                                                        random_state = 42)  ## keeping same random state

    if scale == "Yes":
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)  ## scaling training data
        X_test = scaler.transform(X_test)        ## scaling testing data
    
    knn = KNeighborsClassifier(n_neighbors = k)  ## initializing k-nearest neighbors model
    knn.fit(X_train, y_train)                    ## fitting k-nearest neighbors model
    y_pred = knn.predict(X_test)                 ## using model to make predictions

    st.divider()
    st.subheader("*Let's review the model*")
    st.divider()

    st.write("Below is a table containing information that can be leveraged to evaluate the model.")

    report = classification_report(y_test, y_pred, output_dict = True)     ## creating object for classification report
    df_report = pd.DataFrame(report).transpose()

    st.dataframe(df_report.style.format("{:.2f}"), use_container_width = True)  ## converting report to dataframe

    st.divider()

    column1, column2, column3, column4 = st.columns([1,1,1,1])
    with column1:
        st.write("**Precision**")
        st.write("Precision measures how many of the positive predictions are a true positive.")
    with column2:
        st.write("**Recall**")
        st.write("Recall measures how many of the true positives are predicted to be positive.")
    with column3:
        st.write("**F1 Score**")
        st.write("F1 Score is a measure that incorporates both precision and recall.")
    with column4:
        st.write("**Support**")
        st.write("Support is a count of all the true positives for a class.")

    st.divider()
    st.write("However, like with Linear Regression models, K-Nearest Neighbor models can be evaluated visually too.")
    st.write("On the left is a *confusion matrix*. This matrix illustrates how well a model predicts the class of a datapoint.")
    st.write("On the right is a graph plotting *K values against accuracy*. This graph visually indicates the optimal number of neighbors when considering accuracy. The most optimal model will have its K be tuned to be the same as the highest point on the graph.")
    st.divider()

    column1, column2, column3 = st.columns([1, .1, 1])
    with column1:
        cm = confusion_matrix(y_test, y_pred)
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt = "d", cmap = "Oranges", ax=ax)
        ax.set_title("K-Nearest Neighbor Confusion Matrix", fontsize = 16)
        ax.set_xlabel("Predicted", fontsize = 14)
        ax.set_ylabel("Actual", fontsize = 14)
        st.pyplot(fig)
    with column2:
        st.write("")
    with column3:
        k_values = range(1, 21, 2)
        accuracies_scaled = []
        
        for k in k_values:
            knn_temp = KNeighborsClassifier(n_neighbors=k)
            knn_temp.fit(X_train, y_train)
            y_pred_temp = knn_temp.predict(X_test)
            accuracy_temp = accuracy_score(y_test, y_pred_temp)
            accuracies_scaled.append(accuracy_temp)
        fig_accuracy, ax_accuracy = plt.subplots(figsize=(8, 6))
        ax_accuracy.plot(k_values, accuracies_scaled, marker="o", color="Orange", label="Accuracy")
        ax_accuracy.set_xlabel("# of Neighbors (k)", fontsize = 14)
        ax_accuracy.set_ylabel("Accuracy Score", fontsize = 14)
        ax_accuracy.set_xticks(k_values)
        ax_accuracy.set_title("Number of Neighbors (K) versus Accuracy", fontsize = 16)
        ax_accuracy.legend(loc = "best", fontsize = 12)
        st.pyplot(fig_accuracy)
    st.divider()
        
    
else:
    st.warning("Please select your target and feature variables to continue to train the model.")

