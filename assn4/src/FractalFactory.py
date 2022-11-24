from Fractal import julia, mandelbrot, burningShipJulia
import sys


class FractalFactory:

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def factory(self):
        """
        take in dictionary
        check type
        make object
        """
        if self.dictionary['type'] == 'julia':
            return julia(self.dictionary)
        elif self.dictionary['type'] == 'mandelbrot':
            return mandelbrot(self.dictionary)
        elif self.dictionary['type'] == 'burningshipjulia':
            return burningShipJulia(self.dictionary)
        else:
            print("invalid fractal type")
            sys.exit(1)
