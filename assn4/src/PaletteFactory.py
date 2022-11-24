from Palette2 import palette1, palette2


class PaletteFactory:
    def __init__(self, paletteName, dictionary):
        self.name = paletteName
        self.dictionary = dictionary

    def makePalette(self):
        """
        take in dictionary from parse
        if not parse, default
        make palette object
        error checks
        """

        if self.name == 'palette1' or self.name == '':
            return palette1(self.dictionary)
        elif self.name == 'palette2':
            return palette2(self.dictionary)
        else:
            raise NotImplementedError("Invalid palette requested")
