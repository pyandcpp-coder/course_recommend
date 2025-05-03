import pandas as pd

def load_data():
    users = pd.read_csv("data/user_profile.csv")
    courses = pd.read_csv("data/course_genre.csv")
    ratings = pd.read_csv("data/ratings.csv")
    return users, courses, ratings

