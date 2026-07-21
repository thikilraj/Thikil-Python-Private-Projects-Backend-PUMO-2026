from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Movie data
movies = [
    "Avengers action superhero",
    "Iron Man action superhero",
    "Titanic romance drama",
    "The Notebook romance drama",
    "Interstellar science fiction space",
    "Inception science fiction thriller"
]

# Convert movie descriptions into numerical vectors
vectorizer = TfidfVectorizer()
movie_vectors = vectorizer.fit_transform(movies)

# Calculate similarity between movies
similarity = cosine_similarity(movie_vectors)

# Display movie list
print("Available Movies:")
for i, movie in enumerate(movies):
    print(i + 1, movie)

# Get user choice
choice = int(input("\nEnter movie number: ")) - 1

# Get similarity scores
similar_movies = list(enumerate(similarity[choice]))

# Sort by highest similarity
similar_movies = sorted(
    similar_movies,
    key=lambda x: x[1],
    reverse=True
)

print("\n----- RECOMMENDED MOVIES -----")

count = 0

for index, score in similar_movies:
    if index != choice:
        print(
            f"{movies[index]} "
            f"(Similarity: {score:.2f})"
        )

        count += 1

        if count == 3:
            break