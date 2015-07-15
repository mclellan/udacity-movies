import fresh_tomatoes
import media

# List of movies
movies = []

# Appends movies to list 'movies'
def generate_movie_list():
    movies.append(
        media.movie("Last Life in the Universe",
              "http://ia.media-imdb.com/images/M/MV5BMTgxMzc3OTMyM15BMl5BanBnXkFtZTcwMDM2NjYyMQ@@._V1_.jpg",
              "https://www.youtube.com/watch?v=qObuMyu3NHQ",
              7.7,
              "Tadanobu Asano, Sinitta Boonyasak, Laila Boonyasak"))
    movies.append(
        media.movie("Mad Max: Fury Road",
              "http://ia.media-imdb.com/images/M/MV5BMTUyMTE0ODcxNF5BMl5BanBnXkFtZTgwODE4NDQzNTE@.jpg",
              "https://www.youtube.com/watch?v=hEJnMQG9ev8",
              8.4,
              "Tom Hardy, Charlize Theron, Nicholas Hoult"))
    movies.append(
        media.movie("Porco Rosso",
              "http://ia.media-imdb.com/images/M/MV5BOTQ5MzI1ODgyNF5BMl5BanBnXkFtZTgwOTUyMDk2MjE@.jpg",
              "https://www.youtube.com/watch?v=awEC-aLDzjs",
              7.8,
              "Shuichiro Moriyama, Tokiko Kato, Sanshi Katsura"))
    movies.append(
        media.movie("Brotherhood of the Wolf",
              "http://ia.media-imdb.com/images/M/MV5BMTczMzAwNjA1M15BMl5BanBnXkFtZTcwNDc5NTEyMQ@@.jpg",
              "https://www.youtube.com/watch?v=D7DTv2uBA7I",
              7.1,
              "Samuel Le Bihan, Mark Dacascos, Jacques Perrin"))

# Run all the functions we have defined
def main():
  generate_movie_list()
  fresh_tomatoes.create_movie_tiles_content(movies)
  fresh_tomatoes.open_movies_page(movies)

main()
