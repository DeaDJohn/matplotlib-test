from random import randint

class Die:
    """Un dado de seis caras."""

    def __init__(self, num_sides=6):
        """Inicializa el dado con un número de caras."""
        self.num_sides = num_sides

    def roll(self):
        """Devuelve un número aleatorio entre 1 y el número de caras."""
        return randint(1, self.num_sides)