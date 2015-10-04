# needed for show_trailer()
import webbrowser

class Movie():
    # class __doc__
    """This class provides a way to store movie related information"""

    # class variable
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # constructor
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, imdb_ref):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb_url = imdb_ref

    # instance method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
