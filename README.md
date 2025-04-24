# Amazon Recommender System

A data analytics engine that enables advanced product search and personalized recommendations using real Amazon product metadata and user reviews.

##  Features
- **Search Engine**:
  - Search by Title, Category, Rating, Review Count
  - Filters: `>=`, `<=`, `=`, and more
  - Best-sellers by category
- **Recommendation Engine**:
  - **Collaborative Filtering (ALS)** for personalized recommendations
  - **Frequent Pattern Growth (FP-Growth)** for co-purchase pattern mining

##  Technologies Used
- **Apache Spark (PySpark)**
- **Streamlit** for web UI
- **Pandas**, **Matplotlib**
- Dataset: [Amazon Metadata (Stanford SNAP)](http://snap.stanford.edu/data/amazon-meta.html)

##  Deployment
Live app hosted on **Streamlit Cloud**.

To run locally:
```bash
pip install -r requirements.txt
streamlit run stream_app.py
