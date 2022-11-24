import colour


class Palette:
    """
    template class
    generate color lists for subclasses
    empty getColor() method
    """
    def __init__(self, dictionary):
        pick = colour.Color("white")
        self.colors = list(pick.range_to(colour.Color("black"), dictionary['iterations'] + 1))
        self.colors2 = list(pick.range_to(colour.Color("green"), dictionary['iterations'] + 1))

    def getColor(self, num):
        raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")


class palette1(Palette):
    """
    overide getColor()
        make palette
        return String of #rrggbb
    """
    def __init__(self, dictionary):
        super().__init__(dictionary)

    def getColor(self, num):
        return self.colors[num]


class palette2(Palette):
    """
    overide getColor()
        make palette
        return String of #rrggbb
    """
    def __init__(self, dictionary):
        super().__init__(dictionary)

    def getColor(self, num):
        return self.colors2[num]
