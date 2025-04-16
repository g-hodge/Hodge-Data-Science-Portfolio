# MLStreamlitApp
## Summary
In this project, I develop an app that helps users understand machine learning. In the app, users can create and evaluate their own machine learning models. To personalize learning, users can upload their own datasets to train their models on. Additionally, they can also tune their models, allowing them to not just create a model but create the *best* model.

## Machine Learning Overview 




## Code Instructions ⌨️
To run the code, please import the following libraries (please see the bottom of this section for specific modules to bring in):

``pandas`` for data wrangling

``seaborn`` for visualizations

``streamlit`` for interactive app development

``matplotlib`` for visualizations``

``sklearn`` for machine learning

``numpy`` for computation

<details>
  <summary>Modules</summary>
  
  ``sklearn.model_selection``
  
  ``sklearn.preprocessing``

  ``sklearn.neighbors``

  ``sklearn.metrics``

  ``sklearn.linear_model``

  ``sklearn.model_selection``

  ``sklearn.metrics``
  
  ``matplotlib.pyplot``

</details>


*If you are having issues, please run ``!pip install`` followed by the library you are hoping to import.*



## Streamlit Instructions 📱
To access the deployed version of the app, [click here](https://hodge-data-science-portfolio-azyrfuf2jqbdjyuq2o2whg.streamlit.app/). Have fun!

To locally launch the app, please follow these steps:

1) Open your terminal

2) Check that the file *Home.py* is within your current working directory by running ``ls`` (if it isn't, use ``cd`` to navigate there.

3) Enter ``streamlit run Home.py``

4) Wait for a new browser window to open up, run the code, and start exploring!


## Sample Visualizations 🖼️


<p align="center">
  <img src="https://private-user-images.githubusercontent.com/195391117/434541050-a5d9980d-a5f6-4cab-83d6-5d69d5f84e39.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDQ4NDA0NzUsIm5iZiI6MTc0NDg0MDE3NSwicGF0aCI6Ii8xOTUzOTExMTcvNDM0NTQxMDUwLWE1ZDk5ODBkLWE1ZjYtNGNhYi04M2Q2LTVkNjlkNWY4NGUzOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQxNlQyMTQ5MzVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mODhiYjRlY2M3ZTk4NzJkNTAxMDgyM2MwM2U5MzE0ZjY3MWRhZTBjNjUxMDM0MWQwNGMwZGRmZWEwYmQxY2Q5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.BOR9gOoQgfmhRLRTsTElJ-pxmO1cYDniT42qieWboHg" width="45%" style="display:inline-block; margin-right: 10px;">
  <img src="https://private-user-images.githubusercontent.com/195391117/434541199-de43475c-c3fa-4544-83cc-34488f2724f7.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDQ4NDA1MTEsIm5iZiI6MTc0NDg0MDIxMSwicGF0aCI6Ii8xOTUzOTExMTcvNDM0NTQxMTk5LWRlNDM0NzVjLWMzZmEtNDU0NC04M2NjLTM0NDg4ZjI3MjRmNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNDE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDQxNlQyMTUwMTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zZmUyOTQzMGYxOTg3NjA0OTZjMzhhNDA3ZjI1ZWY5MDI0OGNjNzU4NDVhN2Y0YmQ3MzJhNjliOGFjMTIxNTEwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.yJySDKmESjQiO20Mp_gd0Ot6YvzNkWbGM2M0CQmIMu0" width="45%" style="display:inline-block;">
</p>

The visualization on the left showcases a confusion matrix for a K-Nearest Neighbor Model.

The visualization on the right plots a model's accuracy against its residuals.

## Sources 📚

📕 To develop a conceptual understanding, I read excerpts of [Grokking Machine Learning](https://www.manning.com/books/grokking-machine-learning) by Luis G. Serrano.

👷‍♂️ For app construction, I frequently visited Streamlit's ["Create a multipage app" page](https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app).
