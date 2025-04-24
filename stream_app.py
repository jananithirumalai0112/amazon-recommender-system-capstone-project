import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the final recommendations CSV
DATA_PATH = "C:/spark_output/final_recommendations.csv"
df = pd.read_csv(DATA_PATH)

st.set_page_config(page_title="Amazon Recommender App", layout="wide")
st.title("Amazon Recommender & Search App")

# Sidebar for search filters
st.sidebar.header("🔍 Search Filters")
search_title = st.sidebar.text_input("Search Title Contains")
selected_category = st.sidebar.selectbox("Select Category", ["All"] + sorted(df['Category'].dropna().unique()))
min_rating = st.sidebar.slider("Minimum Rating", 0.0, 10.0, 4.0)

# Filtered DataFrame
filtered_df = df.copy()
if search_title:
    filtered_df = filtered_df[filtered_df['Title'].str.contains(search_title, case=False, na=False)]
if selected_category != "All":
    filtered_df = filtered_df[filtered_df['Category'] == selected_category]
filtered_df = filtered_df[filtered_df['predicted_rating'] >= min_rating]

st.subheader("Filtered Products")
st.dataframe(filtered_df[['user_id_label', 'product_id_label', 'Title', 'Category', 'predicted_rating']])

# Divider
st.markdown("---")

# Recommendation section
st.header("User-Based Recommendations")
unique_users = df['user_id_label'].dropna().unique()
selected_user = st.selectbox("Select User ID to View Recommendations", sorted(unique_users))

user_recs = df[df['user_id_label'] == selected_user] \
    .sort_values(by='predicted_rating', ascending=False)

st.write(f"### Top Recommendations for `{selected_user}`")
st.dataframe(user_recs[['product_id_label', 'Title', 'Category', 'predicted_rating']])

# Plotting chart for ratings
st.subheader("Ratings Distribution")
fig, ax = plt.subplots()
user_recs.sort_values(by='predicted_rating', ascending=True).plot.barh(
    x='Title', y='predicted_rating', ax=ax, color='skyblue', edgecolor='black'
)
ax.set_xlabel("Predicted Rating")
ax.set_ylabel("Product Title")
st.pyplot(fig)
