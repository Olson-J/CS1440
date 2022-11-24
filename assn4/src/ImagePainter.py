from tkinter import Tk, Canvas, PhotoImage, mainloop


class ImagePainter:
    def __init__(self, fractal, palette):
        self.fractal = fractal
        self.palette = palette

    """
    take in objects from fractal and palette factories
    loop of all pixels, find complex number
        give pixel value to object.count() (returns int)
        pass int to palette object.getColor() to get color string
    """
    def picture(self):
        side = self.fractal.dictionary['pixels']
        window = Tk()
        image = PhotoImage(width = side, height = side)

        canvas = Canvas(window, width = side, height = side, bg='#000000')
        canvas.pack()
        canvas.create_image((side / 2, side / 2), image=image, state="normal")

        for row in range(side, 0, -1):
            for col in range(side):
                min = self.fractal.dictionary['min']
                x = min['x'] + col * self.fractal.dictionary['pixelsize']
                y = min['y'] + row * self.fractal.dictionary['pixelsize']

                num = self.fractal.count(complex(x, y))
                color = self.palette.getColor(num)
                image.put(color, (col, side - row))
            window.update()
        mainloop()
