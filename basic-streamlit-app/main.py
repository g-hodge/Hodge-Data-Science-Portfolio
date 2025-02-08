# Set up
import streamlit as st # importing streamlit, following by running terminal command "streamlit run main.py"
import pandas as pd # importing pandas, which is funny as we're looking at penguins!
df = pd.read_csv("data/penguins.csv") # pulling in the data set using relative path
df = df.rename(columns={"id" : "Identifier", "species" : "Species", "island" : "Island", 
                        "bill_length_mm" : "Bill length (mm)", "bill_depth_mm" : "Bill depth (mm)", 
                        "flipper_length_mm" : "Flipper length (mm)", "body_mass_g" : "Body mass (g)", 
                        "sex" : "Sex", "year" : "Year"}) # renaming columns to make them more user friendly

st.title("Penguin Paradise: Palmer Archipelago") # placing a title
st.subheader("Hello penguin lovers! In this app, you can learn more about the pernicuously pontificating yet perfectly passive and playful penguins of the paradise known as Palmer Archipelago. Have fun!") # giving a little bit more information through a subheader

st.write("Now, here's a *not so little* table to introduce you to the crew of 344 penguins we'll be learning about today...") # giving user context about the table they're about to look at
st.dataframe(df)

# creating drop down list for species

st.write("Do you want to learn about one species of penguins? Well, so do I! Click below to filter by species...")

species = st.selectbox("Pick a species, any species...", df["Species"].unique())
df_filtered_species = df[df["Species"] == species]
st.write(f"Penguins that are {species}:")
st.dataframe(df_filtered_species)

# creating buttoms for island

st.write("Well, that's cool, but what matters to me are where they live. Click the button of the island you want to explore...")

island = st.radio("Click below to learn about the island of your dreams (no pun intended):", df["Island"].unique())
df_filtered_island = df[df["Island"] == island]
st.write(f"Penguins that live on {island}:")
st.dataframe(df_filtered_island)

# creating slider for variables related to bills

st.write("Ok ok, I get it, you want to learn about the penguins themselves. Let's learn about those bills...")
columns = ["Bill metric"]
data = ["Length", "Depth"]
df_bill = pd.DataFrame(data, columns=columns) # creating a dataframe to allow for user to switch between length and depth
bill = st.selectbox("Here are some options...pick wisely:", df_bill["Bill metric"].unique())
if bill == "Length":
   bill_length = st.slider("Swipe to explore bill lengths:", min_value=df["Bill length (mm)"].min(), max_value=df["Bill length (mm)"].max())
   df_filtered_bill_length = df[df["Bill length (mm)"] <= bill_length] # returned observations will be less than or equal to selected value
   st.dataframe(df_filtered_bill_length)
elif bill == "Depth":
   bill_depth = st.slider(f"Swipe to explore bill depths:", min_value=df["Bill depth (mm)"].min(), max_value=df["Bill depth (mm)"].max())
   df_filtered_bill_depth = df[df["Bill depth (mm)"] <= bill_depth] # returned observations will be less than or equal to selected value
   st.dataframe(df_filtered_bill_depth)

# creating slider for flippers

st.write("Bills aren't your thing? Ok, let's look at some flippers...")
flipper_length = st.slider("Swipe to explore flipper lengths:", min_value=df["Flipper length (mm)"].min(), max_value=df["Flipper length (mm)"].max())
df_filtered_flipper_length = df[df["Flipper length (mm)"] <= flipper_length] # returned observations will be less than or equal to selected value
st.dataframe(df_filtered_flipper_length)

# creating button for sex

st.write("But wait, there's more! Feel free to filter the penguins by sex...")

sex = st.radio("Click below to learn about the sexes of the penguins:", df["Sex"].dropna().unique()) # excluding observations with no data to make for a cleaner UI
df_filtered_sex = df[df["Sex"] == sex]
st.write(f"Penguins that are {sex}:")
st.dataframe(df_filtered_sex)

# creating slider for year
st.write("One last thing before we go! Now you can look into when the information was collected on all of our lovely penguins...")
year = st.slider("Swipe to learn when information was collected:", min_value=df["Year"].min(), max_value=df["Year"].max())
df_filtered_year = df[df["Year"] <= year] # returned observations will be less than or equal to selected value
st.dataframe(df_filtered_year)

st.write("Alright friends, I think you know enough about penguins now! Thank you for visiting :)") # saying goodbye!