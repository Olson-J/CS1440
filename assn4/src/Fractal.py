class Fractal:
    """
    template class
    empty count() method
    """
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def count(self, complex):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")


class mandelbrot(Fractal):
    """
    override count()
        take in complex number
        return int of iterations
    """
    def __init__(self, dictionary):
        super().__init__(dictionary)

    def count(self, c):
        z = complex(0.0, 0.0)
        for iteration in range(self.dictionary['iterations']):
            z = z * z + c
            if abs(z) > 2:
                return iteration
        return self.dictionary['iterations']


class julia(Fractal):
    """
    override count()
        take in complex number
        return int of iterations
    """
    def __init__(self, dictionary):
        super().__init__(dictionary)

    def count(self, z):
        c = complex(self.dictionary['creal'], self.dictionary['cimag'])
        for iteration in range(self.dictionary['iterations']):
            z = z * z + c
            if abs(z) > 2:
                return iteration
        return self.dictionary['iterations']


class burningShipJulia(Fractal):
    """
    override count()
        take in complex number
        return int of iterations
    """
    def count(self, z):
        c = complex(self.dictionary['creal'], self.dictionary['cimag'])
        for iteration in range(self.dictionary['iterations']):
            absZ = complex(abs(z.real), abs(z.imag))
            z = absZ * absZ + c
            if abs(z) > 2:
                return iteration
        return self.dictionary['iterations']
