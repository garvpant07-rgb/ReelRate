
# ReelRate 🎬

**Discover. Rate. Repeat.**

ReelRate is a movie and anime rating website built using Python and Flask. It allows users to explore titles, compare IMDb ratings, and submit their own ratings.

## Features

- Browse a collection of movies and anime.
- Search titles by name.
- Filter titles by category.
- View movie details and descriptions.
- Compare IMDb ratings with ReelRate user ratings.
- Submit ratings on a scale of 0–10.

## Tech Stack

- Python
- Flask
- HTML5
- CSS3
- Jinja2

## Project Structure

```text
ReelRate/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── posters/
```

## Installation and Setup

1. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate into the project:

   ```bash
   cd ReelRate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open `http://127.0.0.1:5000` in your browser.

## How It Works

The application uses Flask to handle routes and movie data. HTML templates display the collection, while CSS handles the interface. Users can submit ratings, which are used to calculate the ReelRate average.

**Note:** Ratings are currently stored in memory and reset when the Flask server restarts.

## Screenshots

Screenshots of the application will be added here.

## Future Improvements

- Database integration for permanent ratings.
- User accounts and authentication.
- Movie sorting and genre filters.
- Live deployment.

---

**Developed as a student project.**
