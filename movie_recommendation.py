import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = {
    "Movie": [
        "Avatar",
        "Titanic",
        "Avengers",
        "Iron Man",
        "Frozen"
    ],
    "Genre": [
        "Action Adventure Sci-Fi",
        "Romance Drama",
        "Action Superhero",
        "Action Superhero",
        "Animation Family"
    ]
}

df = pd.DataFrame(movies)

vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(df["Genre"])

similarity = cosine_similarity(genre_matrix)

movie_name = "Avengers"

index = df[df["Movie"] == movie_name].index[0]

scores = list(enumerate(similarity[index]))
scores = sorted(scores, key=lambda x: x[1], reverse=True)

print("Recommended Movies:")

for i in scores[1:4]:
    print(df.iloc[i[0]]["Movie"])