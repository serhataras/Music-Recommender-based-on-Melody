import pandas as pd 
import numpy as np

# Read dataset
col_names = pd.read_csv("movieDataset/ratings.csv", nrows=0).columns
types_dict = {"userId":np.int32, "movieId":np.int32, "rating":np.float, "timestamp":str}
df = pd.read_csv("movieDataset/ratings.csv", sep=",", dtype=types_dict)
df.columns = ["userId", "movieId", "rating", "timestamp"]

col_names = pd.read_csv("movieDataset/movies.csv", nrows=0).columns
types_dict = {"movieId":np.int32, "title":str, "genres":str}
df2 = pd.read_csv("movieDataset/movies.csv", sep=",", dtype=types_dict)
df2.columns = ["movieId", "title", "genres"]

dataMatrix = pd.merge(df, df2, on = "movieId")

# Compute average rating & number of ratings for each movie
ratings = pd.DataFrame(dataMatrix.groupby("title")["rating"].mean())
ratings["numRatings"] = dataMatrix.groupby("title")["rating"].count()

# Construct the "item vs user" matrix & ratings
movieUserMatrix = dataMatrix.pivot_table(index="userId", columns="title", values="rating").fillna(0)
ratings = ratings.sort_values("numRatings", ascending=False)

# Find similar items
AFO = movieUserMatrix["Air Force One (1997)"]
similarAFO = movieUserMatrix.corrwith(AFO).sort_values(ascending=False)
print(similarAFO.head(10))