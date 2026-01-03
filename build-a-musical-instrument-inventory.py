# In this workshop, you'll get some practice with Python's classes and objects by building a musical instrument inventory.

class MusicalInstrument:
    """
    A class representing a musical instrument.

    Attributes:
        name (str): The name of the musical instrument.
        instrument_type (str): The type or family of the musical instrument.

    Methods:
        play(): Prints a message indicating that the instrument is fun to play.
        get_fact(): Returns a string containing a fact about the instrument and its type.
    """
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type
    def play(self):
        """
        Plays the musical instrument and prints a message indicating that it is fun to play.

        This method does not take any parameters and does not return any value.
        """
        print(f'The {self.name} is fun to play!')
    def get_fact(self):
        """
        Returns a string that provides a fact about the instrument.

        The fact includes the name of the instrument and its type, formatted as:
        'THe {name} is part of the {instrument_type} family of instruments.'

        Returns:
            str: A descriptive fact about the instrument.
        """
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.'
instrument_1  = MusicalInstrument("Oboe","woodwind")
instrument_2  = MusicalInstrument("Trumpet","brass")
instrument_1.play()
print(instrument_1.get_fact())
instrument_2.play()
print(instrument_2.get_fact())
