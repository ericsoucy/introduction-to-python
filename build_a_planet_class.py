class Planet:
    """
    A class representing a planet.

    Attributes:
        name (str): The name of the planet.
        planet_type (str): The type of the planet (e.g., terrestrial, gas giant).
        star (str): The name of the star that the planet orbits.
    """
    def __init__(self, name, planet_type, star):
        if not (isinstance(name, str) and isinstance(planet_type, str) and isinstance(star, str)):
            raise TypeError("name, planet type, and star must be strings")
        if not (name and planet_type and star):
            raise ValueError("name, planet_type, and star must be non-empty strings")
        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

planet_1 = Planet("Earth", "terrestrial", "Sun")
planet_2 = Planet("Jupiter", "gas giant", "Sun")
planet_3 = Planet("Proxima Centauri b", "terrestrial", "Proxima Centauri")

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
