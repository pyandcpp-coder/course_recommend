# import streamlit as st
# from recommenders import content_user_profile, content_similarity, clustering, knn_cf, svd_cf, nmf_cf
# from utils import preprocessing
# import pandas as pd

# # Load data
# users, courses, ratings = preprocessing.load_data()

# st.title("🎓 Course Recommendation System")

# # Sidebar
# method = st.sidebar.selectbox("Select Recommendation Method", 
#     ["Content-Based: User Profile", 
#      "Content-Based: Course Similarity", 
#      "Content-Based: User Clustering",
#      "Collaborative Filtering: KNN", 
#      "Collaborative Filtering: SVD", 
#      "Collaborative Filtering: NMF"]
# )

# user_id = st.selectbox("Choose User", users['user'].unique())

# # Recommendation logic
# if st.sidebar.button("Get Recommendations"):
#     if method == "Content-Based: User Profile":
#         recs = content_user_profile.get_recommendations(user_id, users, courses, ratings)
#     elif method == "Content-Based: Course Similarity":
#         recs = content_similarity.get_recommendations(user_id, courses, ratings)
#     elif method == "Content-Based: User Clustering":
#         recs = clustering.get_recommendations(user_id, users, courses, ratings)
#     elif method == "Collaborative Filtering: KNN":
#         recs = knn_cf.get_recommendations(user_id, ratings)
#     elif method == "Collaborative Filtering: SVD":
#         recs = svd_cf.get_recommendations(user_id, ratings)
#     elif method == "Collaborative Filtering: NMF":
#         recs = nmf_cf.get_recommendations(user_id, ratings)

#     st.subheader("Top Recommended Courses")
#     st.table(recs)

# # Optional: Display Flowchart
# st.sidebar.markdown("---")
# if st.sidebar.checkbox("Show Method Flowchart"):
#     st.image(f"assets/flowcharts/{method.replace(':', '').replace(' ', '_').lower()}.png", use_column_width=True)
import streamlit as st
import pandas as pd
from recommenders import content_user_profile, content_similarity, clustering, knn_cf, svd_cf, nmf_cf
from utils import preprocessing

# Load data
users, courses, ratings = preprocessing.load_data()

# App Configuration
st.set_page_config(page_title="🎓 Course Recommender", layout="wide")
st.markdown("<h1 style='text-align: center;'>🎓 Course Recommendation System</h1>", unsafe_allow_html=True)
st.write("")

# Sidebar - Select Method
method = st.sidebar.selectbox("🔍 Select Recommendation Method", [
    "Content-Based: User Profile", 
    "Content-Based: Course Similarity", 
    "Content-Based: User Clustering",
    "Collaborative Filtering: KNN", 
    "Collaborative Filtering: SVD", 
    "Collaborative Filtering: NMF"
])

# Sidebar - Flowchart Option
# st.sidebar.markdown("---")
# if st.sidebar.checkbox("📊 Show Method Flowchart"):
#     image_path = f"assets/flowcharts/{method.replace(':', '').replace(' ', '_').lower()}.png"
#     st.sidebar.image(image_path, use_column_width=True)

# User Selection
user_id = st.selectbox("👤 Choose User", users['user'].unique())

# Helper: Pretty Course Cards
def display_recommendations(course_ids):
    recommended_df = courses[courses['COURSE_ID'].isin(course_ids)]

    if recommended_df.empty:
        st.warning("No recommendations found for this user.")
        return

    for _, row in recommended_df.iterrows():
        st.markdown(f"""
        <div style="padding: 15px; border: 1px solid #444; border-radius: 12px; margin-bottom: 10px; background-color: #1e1e1e;">
            <b style="font-size: 18px;">{row.get('COURSE_NAME', row['COURSE_ID'])}</b><br>
            <i>{row.get('CATEGORY', 'General')}</i><br>
            <code>{row['COURSE_ID']}</code>
        </div>
        """, unsafe_allow_html=True)

# Recommendation Button
if st.sidebar.button("🎯 Get Recommendations"):
    if method == "Content-Based: User Profile":
        recs = content_user_profile.get_recommendations(user_id, users, courses, ratings)
    elif method == "Content-Based: Course Similarity":
        recs = content_similarity.get_recommendations(user_id, courses, ratings)
    elif method == "Content-Based: User Clustering":
        recs = clustering.get_recommendations(user_id, users, courses, ratings)
    elif method == "Collaborative Filtering: KNN":
        recs = knn_cf.get_recommendations(user_id, ratings)
    elif method == "Collaborative Filtering: SVD":
        recs = svd_cf.get_recommendations(user_id, ratings)
    elif method == "Collaborative Filtering: NMF":
        recs = nmf_cf.get_recommendations(user_id, ratings)

    st.subheader("📚 Top Recommended Courses")
    display_recommendations(recs)

