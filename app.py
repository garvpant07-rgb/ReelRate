
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Movie collection
movies = [
    {
        "id": 1,
        "name": "Interstellar",
        "year": 2014,
        "genre": "Sci-Fi",
        "category": "Movies",
        "imdb": 8.7,
        "description": "A team of explorers travels beyond this galaxy to discover whether mankind has a future among the stars.",
        "poster": "posters/interstellar.jpg",
        "ratings": []
    },
    {
        "id": 2,
        "name": "Inception",
        "year": 2010,
        "genre": "Thriller",
        "category": "Movies",
        "imdb": 8.8,
        "description": "A skilled thief enters people's dreams to steal secrets and attempts an almost impossible mission.",
        "poster": "posters/inception.jpg",
        "ratings": []
    },
    {
        "id": 3,
        "name": "The Dark Knight",
        "year": 2008,
        "genre": "Action",
        "category": "Movies",
        "imdb": 9.0,
        "description": "Batman faces a dangerous criminal who wants to bring chaos to Gotham City.",
        "poster": "posters/dark_knight.jpg",
        "ratings": []
    },
    {
        "id": 4,
        "name": "Your Name",
        "year": 2016,
        "genre": "Romance",
        "category": "Anime",
        "imdb": 8.4,
        "description": "Two teenagers mysteriously begin switching bodies and try to find each other.",
        "poster": "posters/your_name.jpg",
        "ratings": []
    },
    {
        "id": 5,
        "name": "Spider-Man: Into the Spider-Verse",
        "year": 2018,
        "genre": "Animation",
        "category": "Movies",
        "imdb": 8.4,
        "description": "Miles Morales discovers a world of Spider-People from different dimensions.",
        "poster": "posters/spider_verse.jpg",
        "ratings": []
    },
    {
        "id": 6,
        "name": "Dune: Part Two",
        "year": 2024,
        "genre": "Sci-Fi",
        "category": "Movies",
        "imdb": 8.5,
        "description": "Paul Atreides joins the Fremen and seeks revenge while facing a destiny that could change the universe.",
        "poster": "posters/dune_part_two.jpg",
        "ratings": []
    },
    {
        "id": 7,
        "name": "The Batman",
        "year": 2022,
        "genre": "Crime",
        "category": "Movies",
        "imdb": 7.8,
        "description": "Batman investigates corruption in Gotham City while pursuing a mysterious serial killer.",
        "poster": "posters/the_batman.jpg",
        "ratings": []
    },
    {
        "id": 8,
        "name": "Parasite",
        "year": 2019,
        "genre": "Thriller",
        "category": "Movies",
        "imdb": 8.5,
        "description": "A poor family gradually becomes involved in the lives of a wealthy household.",
        "poster": "posters/parasite.jpg",
        "ratings": []
    },
    {
        "id": 9,
        "name": "Whiplash",
        "year": 2014,
        "genre": "Drama",
        "category": "Movies",
        "imdb": 8.5,
        "description": "A young drummer pushes himself to the limit under the demanding guidance of a music instructor.",
        "poster": "posters/whiplash.jpg",
        "ratings": []
    },
    {
        "id": 10,
        "name": "Arcane",
        "year": 2021,
        "genre": "Animation",
        "category": "Anime",
        "imdb": 9.0,
        "description": "Two sisters find themselves on opposing sides of a conflict between two cities.",
        "poster": "posters/arcane.jpg",
        "ratings": []
    },
    {
        "id": 11,
        "name": "Suzume",
        "year": 2022,
        "genre": "Fantasy",
        "category": "Anime",
        "imdb": 7.6,
        "description": "A young girl travels across Japan to close mysterious doors that threaten the world.",
        "poster": "posters/suzume.jpg",
        "ratings": []
    },
    {
        "id": 12,
        "name": "The Prestige",
        "year": 2006,
        "genre": "Mystery",
        "category": "Movies",
        "imdb": 8.5,
        "description": "Two rival magicians become obsessed with creating the ultimate stage illusion.",
        "poster": "posters/the_prestige.jpg",
        "ratings": []
    }
]


# Function to calculate ReelRate average
def calculate_average(ratings):

    if len(ratings) == 0:
        return 0

    total = 0

    for rating in ratings:
        total = total + rating

    average = total / len(ratings)

    return round(average, 1)


# Homepage
@app.route("/")
def home():

    search = request.args.get("search", "")
    category = request.args.get("category", "All")

    filtered_movies = []

    for movie in movies:

        name_matches = search.lower() in movie["name"].lower()

        category_matches = (
            category == "All"
            or movie["category"] == category
        )

        if name_matches and category_matches:
            filtered_movies.append(movie)

    return render_template(
        "index.html",
        movies=filtered_movies,
        search=search,
        category=category
    )


# Submit a movie rating
@app.route("/rate/<int:movie_id>", methods=["POST"])
def rate_movie(movie_id):

    rating = float(request.form["rating"])

    if rating >= 0 and rating <= 10:

        for movie in movies:

            if movie["id"] == movie_id:
                movie["ratings"].append(rating)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

