import fresh_tomatoes
import media

# my six movies, defined via "media"
before_sunrise = media.Movie("Before Sunrise",
    "One night in Paris ...",
    "https://upload.wikimedia.org/wikipedia/en/d/da/Before_Sunrise_poster.jpg",
    "https://www.youtube.com/watch?v=25v7N34d5HE",
    "http://www.imdb.com/title/tt0112471/")

better_than_chocolate = media.Movie("Better Than Chocolate",
    "Love, honesty, family, and chocolate",
    "https://upload.wikimedia.org/wikipedia/en/3/3a/Better_Than_Chocolate_%28film%29.jpg",
    "https://www.youtube.com/watch?v=6hcvuF5DWyY",
    "http://www.imdb.com/title/tt0168987/")

monsters_inc = media.Movie("Monsters, Inc",
    "Work-a-day monsters meet a potential invader",
    "https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",
    "https://www.youtube.com/watch?v=6tCxnHCqqxg",
    "http://www.imdb.com/title/tt0198781/")

rudy = media.Movie("Rudy",
    "A kid, a football team and a dream",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Rudy2.jpg",
    "https://www.youtube.com/watch?v=Xm0pTMbDaMI",
    "http://www.imdb.com/title/tt0108002/")

strictly_ballroom = media.Movie("Strictly Ballroom",
    "Love and competition on the dancefloor",
    "https://upload.wikimedia.org/wikipedia/en/0/04/StrictlyBallroom.jpg",
    "https://www.youtube.com/watch?v=7dtfxf3FFx4",
    "http://www.imdb.com/title/tt0105488/")

thelma_and_louise = media.Movie("Thelma and Louise",
    "Two ladies get away from it all",
    "https://upload.wikimedia.org/wikipedia/en/d/de/Thelma_%26_Louiseposter.jpg",
    "https://www.youtube.com/watch?v=2iBFmKlO4BY", 
    "http://www.imdb.com/title/tt0103074/")

# array needed to run fresh.tomatoes function
movies = [before_sunrise, better_than_chocolate, monsters_inc,
          rudy, strictly_ballroom, thelma_and_louise]

# generates the movie page
fresh_tomatoes.open_movies_page(movies)
