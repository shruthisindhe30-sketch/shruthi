import json
import os

class Movie:
    def __init__(self, title, director, genre, year):
        self.title = title
        self.director = director
        self.genre = genre
        self.year = year

    def to_dict(self):
        return self.__dict__

class MovieManager:
    def __init__(self, filename='movies.json'):
        self.filename = filename
        self.movies = self.load_movies()

    def load_movies(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return [Movie(**m) for m in json.load(f)]
        return []

    def save_movies(self):
        with open(self.filename, 'w') as f:
            json.dump([m.to_dict() for m in self.movies], f)

    def add_movie(self, title, director, genre, year):
        movie = Movie(title, director, genre, year)
        self.movies.append(movie)
        self.save_movies()
        print(f"Added: {title}")

    def view_movies(self):
        for i, m in enumerate(self.movies, 1):
            print(f"{i}. {m.title} ({m.year}) - {m.director} ({m.genre})")

    def search(self, query):
        results = [m for m in self.movies if query.lower() in m.title.lower() or query.lower() in m.director.lower()]
        for m in results:
            print(f"{m.title} by {m.director}")

# Usage example
manager = MovieManager()
while True:
    cmd = input("Command (add/view/search/quit): ")
    if cmd == 'quit': break
    elif cmd == 'add':
        title = input("Title: ")
        director = input("Director: ")
        genre = input("Genre: ")
        year = input("Year: ")
        manager.add_movie(title, director, genre, year)
    elif cmd == 'view':
        manager.view_movies()
    elif cmd == 'search':
        query = input("Search: ")
        manager.search(query)
