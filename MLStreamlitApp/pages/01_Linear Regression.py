#-----------0. Setting up workstation-----------

import streamlit as st    ## for app
import pandas as pd       ## for data wrangling

from sklearn.linear_model import LinearRegression                                   ## for linear regression
from sklearn.model_selection import train_test_split                                ## for data splitting tool for training and testing
from sklearn.preprocessing import StandardScaler                                    ## for scaling
from sklearn.metrics import mean_squared_error, root_mean_squared_error, r2_score   ## for linear regression evaluation metrics
import matplotlib.pyplot as plt                                                     ## for plotting
import seaborn as sns                                                               ## for visualization
plt.rcParams.update({'font.family': 'sans-serif', 'font.size': 12})                 ## for changing plot font to streamlit's font

#-----------1. Introduction to LR---------------

st.title("Linear Regression Model")
st.divider()
column1, column2 = st.columns([.5,.3])
with column1:
    st.write("On this page, you'll construct and evaluate a Linear Regression model.")
    st.write("You have chosen to work with a Linear Regression model as your target variable is numerical. If possible, please choose a *continuous* numerical variable.")
with column2:
    st.image("images/1.webp")

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
st.subheader("*Time to build your model*")
st.divider()

numerical_columns = df.select_dtypes(include=['number']).columns.tolist()                     ## creating list of numerical variables

column1, column2 = st.columns([1, 1])
with column1:
    X_select = st.multiselect("Please select your feature variable(s):", numerical_columns)   ## allowing users to select multiple numerical variables
with column2:
    st.write("")
    st.write("")
    st.write(f"**Feature Variable(s):** {', '.join(X_select)}")

column1, column2 = st.columns([1, 1])
with column1:
    y_select = st.selectbox("Please select your target variable:", numerical_columns)        ## allowing users to select one numerical variable
with column2:
    st.write("")
    st.write("")
    st.write(f"**Target Variable:** {y_select}")

scale = st.radio("Please select whether you would like to scale your data:", ["Yes", "No"])   ## creating button to decide if data is scaled or not

st.divider()
st.subheader("*Let's review and evaluate the model*")
st.divider()

#-----------3. Model Training and Evaluation----

## In this section, I will train a Linear Regression model. To do so, I will take the inputs and divide them into two groups: train and test. These two groups will be used to create and evaluate my linear regression model. I will also--if requested by the user--scale my data. Scaling puts all of the variables in the same units (i.e., standard deviations), which makes it easier to apply the model's results.


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

    lin_reg = LinearRegression()        ## initializing linear regression
    lin_reg.fit(X_train, y_train)       ## fitting linear regresion model

    y_pred = lin_reg.predict(X_test)    ## using model to make predictions
    coefficients = lin_reg.coef_        ## grabbing coefficients

    st.write("One of the most important aspects of a Linear Regression model is the coefficients. They tell us how much the target variable changes for every one unit change in the predictors.")
    st.write("**The coefficient(s) for the model:**")
    for feature, coef in zip(feature_names, coefficients):
        st.write(f"For every 1.00 unit increase in feature {feature}, there is a {coef:.2f} unit change in {y_select}.")
    
    ## The output of this section will be a list of coefficients. These coefficients represent the predicted change in the target variable when the feature variable changes by 1 unit.

    st.divider()
    
    ## I will also provide an opportunity to evaluate the model visually. To do so, I will plot the predicted values against the residual values. This helps me and the user understand if the model is a fit for the data. If it is a strong fit, the datapoints will appear to be randomly distributed around the graph, with the only clustering occuring around the y-axis value of "0". If it does not appear as I described, another model may be better. For instance, if it clusters at one of the ends, a non-linear model may be a better fit.

    column1, column2 = st.columns([.6,1])
    with column1:
        st.write("")
        st.write("Another way to understand and evaluate a model is through visualizations. One example is plotting residual against predicted values.")
        st.write("The *ideal plot* has points scattered around the residual value of 0. The points should not be clustered at a particular end of the graph either.")
        st.write("A plot like that is ideal as it illustrates the errors of the model are evenly distributed.")
    with column2:
        residual = y_test - y_pred                         ## calculating residuals
        plt.figure(figsize=(6,5))                          ## painting plot
        sns.scatterplot(x=y_pred, y=residual)              ## plotting predicted values against residuals
        plt.axhline(0, color="blue", linestyle="dotted")
        plt.xlabel("Predicted Values")
        plt.ylabel("Residual Values")
        plt.title("Residual Values versus Predicted Values")
        st.pyplot(plt)

    ## In the end, the graph produced will have two axes. The x-axis will be labelled "predicted values," while the y-axis will take on the label "residuals." There will also be a dotted blue line cutting the graph in half. This line has a formula of y = 0 (therefore, it has a gradient of 0).

    st.divider()

    ## Additional metrics will be provided after the visualization. These include MSE, RMSE, and R^2. The role of these metrics in evaluation is described within the app for easy access by the user.

    st.write("However, you can also go beyond visualizations. For Linear Regression models, you can leverage three main metrics used in evaluation.")
    
    column1, column2, column3 = st.columns([1,1,1])
    with column1:
        st.write("**1. The Mean Squared Error (MSE)**")
    with column2:
        st.write("**2. Root Mean Squared Error (RMSE)**")
    with column3:
        st.write("**3. R-Squared (R²)**")

    column1, column2, column3 = st.columns([1,1,1])
    with column1:
        st.write("The Mean Squared Error tells us the average error between the actual and predicted values.")
    with column2:
        st.write("The Root Mean Squared Error tells us a similar thing. However, when taking the square root of the MSE, we put both the predictor and target variables in the same units for better comparison.")
    with column3:
        st.write("The R² helps tells us how much of the variance in the target variable can be explained by the predictors As the R² approaches 1, the model explains the variance in the target better.")


    column1, column2, column3 = st.columns([1,1,1])
    with column1:
        mse_lin = mean_squared_error(y_test, y_pred)         ## calculating mse
        st.write(f"**MSE Value:** {mse_lin:.2f}")
    with column2:
        rmse_lin = root_mean_squared_error(y_test, y_pred)   ## calculating rmse
        st.write(f"**RMSE Value:** {rmse_lin:.2f}")
    with column3:
        r2_lin = r2_score(y_test, y_pred)                    ## calculating r^2
        st.write(f"**R² Value:** {r2_lin:.2f}")

else:
    st.warning("Please select your target and feature variables to continue to train the model.")

st.divider()