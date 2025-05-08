#-----------0. Workstation-----------

import streamlit as st          # for streamlit
import pandas as pd             # for data wrangling
import numpy as np                   # for computation
import matplotlib.pyplot as plt      # for plotting
from sklearn.preprocessing import StandardScaler   # for scaling
from sklearn.cluster import KMeans   # for KMeans
from sklearn.decomposition import PCA     # for PCA
import random                   # for creating numbers
from sklearn.metrics import silhouette_score

#-----------1. Introduction----------

st.title("Clustering: KMeans")
st.divider()

col1, col2, col3 = st.columns([.8,.1,1])

## providing overview of page

with col1:
    st.write("**Page Overview**")
    st.write("In this part of the app, you will explore clustering through a KMeans model. This model applies labels to observations with similar attributes.")
    st.write("You can adjust the model based on one hyperparameter: K. In this model, K represents the number of clusters the model will predict.")
    st.write("A common way to plot the results is through a scatter plot. When you have over two variables, it is necessary to apply a dimension reduction model, which the example to the right leverages.")

with col2:
    st.write("")

## creating example graph based on fake data

with col3:
    st.write("**Example Graph**")
    clustering_example_viz_numbers_1 = random.sample(range(0,50), 50) ## creating four different variables, with 50 values ranging from 0 to 50
    clustering_example_viz_numbers_2 = random.sample(range(0,50), 50)
    clustering_example_viz_numbers_3 = random.sample(range(0,50), 50)
    clustering_example_viz_numbers_4 = random.sample(range(0,50), 50)

    clustering_example_viz_df = pd.DataFrame({"1": clustering_example_viz_numbers_1, # creating dataframe containing the four variables
                                              "2": clustering_example_viz_numbers_2,
                                              "3": clustering_example_viz_numbers_3,
                                              "4": clustering_example_viz_numbers_4})

    scaler = StandardScaler() # creating scaler
    X_std_example_viz = scaler.fit_transform(clustering_example_viz_df) # scaling dataframe clustering_example_viz_df

    clustering_example_viz_k = KMeans(n_clusters=2, random_state=42) # creatign kmeans model where # of clusters is 2
    clustering_example_viz_cluster_labels = clustering_example_viz_k.fit_predict(X_std_example_viz) # running kmeans model over data

    pca = PCA(n_components=2) # setting up pca model where # of components is 2
    clustering_example_viz_X_pca = pca.fit_transform(X_std_example_viz) # using pca model to reduce datasets to 2 components

    fig, ax = plt.subplots(figsize = (8, 6)) # creating canvas for plot to go on
    ax.scatter(clustering_example_viz_X_pca[clustering_example_viz_cluster_labels == 0, 0], 
               clustering_example_viz_X_pca[clustering_example_viz_cluster_labels == 0, 1],
               c="navy", s = 125, edgecolor = "black", label = "Cluster A") # plotting points on scatter plot, where cluster a is navy blue, has black edges, and size is 125
    ax.scatter(clustering_example_viz_X_pca[clustering_example_viz_cluster_labels == 1, 0],
               clustering_example_viz_X_pca[clustering_example_viz_cluster_labels == 1, 1],
               c = "red", s = 125, edgecolor =  "black", label = "Cluster B") # plotting remaining points on scatter plot, where cluster b has the same attributes as a but the points are red
    ax.set_title("Example Clustering Results")
    ax.set_xlabel("Component 1")
    ax.set_ylabel("Component 2")
    ax.legend()
    ax.grid(False) # turning off grid

    st.pyplot(fig) # making plot visible on streamlit
    
    st.write("*To see another example, refresh the page!*")


st.divider()

## transferring df from home page

if "df" in st.session_state:     ## carrying over df from home page
    df = st.session_state.df
else:
    st.warning("Please revisit the home page to upload the database you would like to run through the KMeans model.")  # creating warning that appears when users fail to upload a csv file
    st.divider()
    st.stop() # stopping streamlit app from running when no csv file is uploaded


#-----------2. Model Setup-----------

st.subheader("Model Setup")
st.divider()

X_std_clustering = scaler.fit_transform(df) # scaling data to all be on the same unit (i.e., standard deviations), as is encouraged for unsupervised machine learning

col1, col2, col3 = st.columns([.8,.1,1])

with col1:
    st.write("")
    st.write("")
    k = st.slider("Please choose the number of clusters (k):",
                min_value = 2, max_value = 20, step = 1, value = 2) # creating slider ranging from 2 to 20 with interval of 1
    st.write(f"Your model will have {k} clusters.") # writing number of clusters for additional clarity
    
with col2:
    st.write("")

with col3:
    st.write("Please use the slider to the left to adjust the number of clusters that will be used in the model.")
    st.write("You can adjust this value later. After the next section, you can visually analyze a graph to determine the best K value for your model.")


#-----------3. Plotting--------------

## introduction to section
st.divider()
st.subheader("Results & Visualization")
st.divider()

st.write("**Visualization Overview**")
st.write("The following graph visualizes the results of the model you made! It is using the data entered on the home page of this app.")
st.write("To make a 2D visualization possible, a Principal Component Analysis (PCA) model was applied to the data. Luckily, this app also covers PCA models! Please visit the **Dimension Reduction page** to learn more.")
st.divider()

## creating model

clustering = KMeans(n_clusters = k, random_state = 42) # creating model, where # of clusters is dependent upon slide bar
clustering_labels = clustering.fit_predict(X_std_clustering) # running model

pca_clustering_viz = PCA(n_components = 2) # preparing pca when components = 2
clustering_pca = pca_clustering_viz.fit_transform(X_std_clustering) # using pca model to reduce variables to two

## visualizing model

fig, ax = plt.subplots(figsize=(10, 6)) # creating canvas for graph
scatter = ax.scatter(clustering_pca[:, 0], clustering_pca[:, 1], c = clustering_labels, cmap = "plasma",
                     s = 120, edgecolor = "black") # creating scatter graph for data that went through pca

legend = [plt.Line2D([0], [0], marker = "o", color = "w", # creating a legend that is customizable to each cluster created by the model
               label = f'Cluster {chr(65 + i)}', # making it so the cluster names go letter by letter
               markerfacecolor = scatter.cmap(scatter.norm(i)), # aligning cluster color on graph and cluster color on legend
               markersize = 10, markeredgecolor = "black")for i in range(k)] # repeating for each cluster, with the cluster number being based on the slider
ax.legend(handles=legend) # placing the custom legend on the canvas

ax.set_title('Clustering Results')
ax.set_xlabel("Component 1")
ax.set_ylabel("Component 2")
ax.grid(False) # turning off grid for aesthetics

st.pyplot(fig) # plotting fig on canvas

#-----------4. Evaluation------------

st.divider()
st.subheader("Evaluation")
st.divider()

## setting up evaluation based on silhouette score

col1, col2, col3 = st.columns([1,.1,1])

with col1:
    silhouette_scores = [] # creating list to hold silhouette score

    k_silhouette = range(2, 20) # definign range for map, based on max and min of slider
    
    for k in k_silhouette: # looping over each value of k on the slider
        kmeans_silhouette = KMeans(n_clusters = k, random_state=42) # running model, where clusters is dependent upon the value of k
        labels = kmeans_silhouette.fit_predict(X_std_clustering) # fitting model
        silhouette_scores.append(silhouette_score(X_std_clustering, labels)) # calculating silhouette scores
        fig, ax = plt.subplots() # preparing to create graph visualizing scores
    
    fig, ax = plt.subplots(figsize = (10, 6)) # preparing canvas for graph
    ax.plot(k_silhouette, silhouette_scores, marker = "o", color = "navy", linestyle= "--") # plotting scores, which will be navy blue circles connected by a dashed line
    ax.set_title("Optimal K: Silhouette")
    ax.set_xlabel("Number of Clusters")
    ax.set_ylabel("Silhouette Score")
    plt.xticks(np.arange(min(k_silhouette), max(k_silhouette)+2, 2)) # refining increments of ticks on x-axis to be 2
    ax.grid(False) # turning off grid lines

    st.pyplot(fig) # plotting fig on canvas

    with col2:
        st.write("")
    
    with col3:
        st.write("**Silhouette Score**")
        st.write("One method to find the optimal K (i.e., the best number of clusters) is through visually analyzing the model's silhouette score.")
        st.write("The best K value is the point with the highest corresponding silhouette score.")

## setting up evaluation based on elbow method

st.divider()

col1, col2, col3 = st.columns([1,.1,1])

with col1:
    st.write("**Elbow Method**")
    st.write("An alternative method is the elbow method.")
    st.write("When using this method, the optimal K value is the point in which the curve begins to flatten.")

with col2:
    st.write("")

with col3:
    st.write("")

    wcss = [] # creating list to hold wcss

    k_elbow = range(2, 20) # setting range of k_elbow to mirror max and min of slider

    for k in k_elbow:
        kmeans_elbow = KMeans(n_clusters = k, random_state=42) # creating kmeans model where # of clusters is based on k
        labels = kmeans_elbow.fit_predict(X_std_clustering) # fitting model to data
        wcss.append(kmeans_elbow.inertia_) # appending each k's intertia, which is a measurement of distance from the nearest cluster centroid

    fig, ax = plt.subplots(figsize=(10, 6)) # creating canvas for plot
    ax.plot(k_elbow, wcss, marker = "o", color = "red", linestyle = "--") # plotting values, making points red circles connected by a hashed line
    ax.set_xlabel('Number of clusters')
    ax.set_ylabel('WCSS')
    ax.set_title('Optimal K: Elbow Method')
    plt.xticks(np.arange(min(k_silhouette), max(k_silhouette)+2, 2)) # adjusting increments between ticks to 2 units
    ax.grid(False) # turning off grid lines

    st.pyplot(fig) # plotting fig on canvas

st.divider()
