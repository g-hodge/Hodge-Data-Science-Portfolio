# MLUnsupervisedApp
## Summary 📚
This project includes an app that helps users **own their learning experience and create an upservised machine learning model.** 
Users can choose from either a Principal Component Analysis or KMeans model.
After creating their model, they can evaluate it, loop back, and make any desired adjustments to the hyperparameters.
By doing so, they can create a product they are proud of and understand.

## Unsupervised Machine Learning Overview
The goal of machine learning is to create models that replicate how humans go about making decisions. Machine learning comes in three different types: **supervised**, **unsupervised**, and **reinforcement learning**.
This app will help users learn about unsupervised machine learning.

In this type of machine learning, models are run over data without labels.
The questions unsupervised learning attempts to address are ones of similarity.
 

 Two models will be accessible to users in the app. They are **Principal Component Analysis** and **KMeans** models.

 ## Model Overview 💻

 **Principal Component Analysis** models are a type of dimension reduction model.
 Dimension reduction models aim to combine variables into components based on similar attributes. This means the model focuses on how columns--not rows--are similar.
 In this app, users have the ability to determine how many different components they would like to create out of the variables in their dataset.

 **KMeans** models are a type of clustering model. Clustering focuses on assigning labels to observations. Unlike dimension reduction models, these types of models focus on finding similarities between observations within a dataset.
 In the app, users have the capacity to define how many clusters they would like to be formed. KMeans can be combined with Principal Component Analysis for visualization.
 As they progress through the page on the clustering model, users can engage with a plot that uses Principal Component Analysis to easily visualize the results of a KMeans model.

## Code Instructions
Users should import the following libraries to run the code (specific libraries to be imported are included later in this section):

``pandas`` for data wrangling

``streamlit`` for interactive app development

``matplotlib`` for visualizations``

``sklearn`` for machine learning

``numpy`` for computation

``random`` for number generation

<details>
  <summary>Modules</summary>
  
  
  ``matplotlib.pyplot``

  ``sklearn.preprocessing``

  ``sklearn.cluster``

  ``sklearn.decomposition``

  ``sklearn.metrics``


</details>

*If issues come up when importing libraries, try to run ``!pip install`` followed by the library name.*

## Streamlit App Instructions 🎮
To access the deployed version of the app, [click here](https://hodge-data-science-portfolio-mfbuk54479kmakhns8bvum.streamlit.app/). Have fun!

To locally launch the app, please follow these steps:

1) Open your terminal

2) Check that the file *Home.py* is within your current working directory by running ``ls`` (if it isn't, use ``cd`` to navigate there)

3) Enter ``streamlit run Home.py``

4) Wait for a new browser window to open up, run the code, and start exploring!

## Visualization Samples 🎨

<p align="center">
  <img src="https://github.com/user-attachments/assets/9ebbaba5-bce9-4595-91e1-aea7a70dc872" width="25%" style="display:inline-block; margin-right: 10px;">
  <img src="https://github.com/user-attachments/assets/6c997c70-ecb5-4f19-99e2-2ccab75cabe9" width="30%" style="display:inline-block;">
  <img src="https://github.com/user-attachments/assets/0e7bba83-4228-4a6a-8aa2-87cd94f90bb2" width="20%" style="display:inline-block; margin-left: 10px">

  ⬅️ The visualization to the left is an example of the results of a KMeans model. In this graph, there are two clusters. The data used to run this model includes four variables, meaning a Principal Component Analysis model was also used to simplify the dataset for visualization purposes.

  ⬆️ The graph in the middle is used to evaluate KMeans models. This graph is used for the "elbow method" of choosing an optimal K value (i.e., the number of clusters).
  The optimal number is when the gradient of the curve becomes drastically more shallow, which is at 6 clusters.

  ➡️ The plot to the right is a tool used in Principal Component Analysis model evaluation. 
  This barplot highlights the proportion of variance explained by each component created in the process of running the model over a dataset.
</p>

## Sources

📕 To learn about unsupervised machine learning, I read parts of Luis G. Serrano's [Grokking Machine Learning](https://www.manning.com/books/grokking-machine-learning).

🖼️ To design graphs, I referenced matplotlib's ["Quick start guide"](https://matplotlib.org/stable/users/explain/quick_start.html).

👷‍♂️ To build the app, I used Streamlit's ["Create a multipage app"](https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app).
