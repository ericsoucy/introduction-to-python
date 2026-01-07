class Movie:
    """Parent class representing a movie."""
    def __init__(self, title, year, director, duration):
        # Validation: Ensure the title is not empty or just whitespace
        if not title.strip():
            raise ValueError("Title cannot be empty")
        # Validation for year
        if year < 1895:
            raise ValueError("Year must be 1895 or later")
        # 3. Director Validation
        if not director.strip():
            raise ValueError("Director cannot be empty")
        # 4. Duration Validation
        if duration <= 0:
            raise ValueError("Duration must be positive")
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration
    def __str__(self):
        """Returns a summarized string representation of the movie."""
        return f"{self.title} ({self.year}) - {self.duration} min, {self.director}"

class TVSeries(Movie):
    """Child class representing an entire TV series."""
    def __init__(self, title, year, director, duration, seasons, total_episodes):
        # Pass the core data up to the Movie class for validation and assignment
        super().__init__(title, year, director, duration)
        # 2. Validate seasons
        if seasons < 1:
            raise ValueError("Seasons must be 1 or greater")
        # 3. Validate total_episodes
        if total_episodes < 1:
            raise ValueError("Total episodes must be 1 or greater")
        # Assign TV-specific attributes
        self.seasons = seasons
        self.total_episodes = total_episodes
    def __str__(self):
        """Returns a summarized string representation of the TV series."""
        return (f"{self.title} ({self.year}) - {self.seasons} seasons, "
                f"{self.total_episodes} episodes, {self.duration} min avg, "
                f"{self.director}")
class MediaCatalogue:
    """A catalogue that can store different types of media items."""
    def __init__(self):
        self.items = []
    def __str__(self):
        if not self.items:
            return 'Media Catalogue (empty)'
        # Organize items by calling our filtering methods
        movies = self.get_movies()
        series = self.get_tv_series()
        result = f'Media Catalogue ({len(self.items)} items):\n\n'
        # Add the MOVIES header only if there are movies present
        if movies:
            result += "=== MOVIES ===\n"
            for i, movie in enumerate(movies, 1):
                result += f'{i}. {movie}\n'
        # TV Series Section
        if series:
            result += "=== TV SERIES ===\n"
            for i, s in enumerate(series, start=1):
                result += f"{i}. {s}\n"
        return result
    def add(self, media_item):
        """Appends a new media item to the catalogue."""
        # Check if the item is a Movie or any subclass (like TVSeries)
        if not isinstance(media_item, Movie):
            raise MediaError("Only Movie or TVSeries instances can be added", media_item)
        self.items.append(media_item)
    def get_movies(self):
        """Returns a list of items that are strictly Movie instances."""
        return [item for item in self.items if type(item) is Movie]
    def get_tv_series(self):
        """Returns a list containing only TVSeries instances."""
        return [item for item in self.items if type(item) is TVSeries]
catalogue = MediaCatalogue()

class MediaError(Exception):
    """Custom exception for media-related errors."""
    def __init__(self, message, obj):
        # Initialize the base Exception with the error message
        super().__init__(message)
        # Store the problematic object for debugging purposes
        self.obj = obj

try:
    movie1 = Movie('The Matrix', 1883, 'The Wachowskis', 136)
    catalogue.add(movie1)
    movie2 = Movie('Inception', 2010, 'Christopher Nolan', 148)
    catalogue.add(movie2)
    series1 = TVSeries('pluribus',2025,'giligan',50,1,9)
    catalogue.add(series1)
    series2 = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
    catalogue.add(series2)
except ValueError as e:
    print(f"Validation Error: {e}")
except MediaError as e:
    print(f'Media Error: {e}')
    print(f'Unable to add {e.obj}: {type(e.obj)}')
