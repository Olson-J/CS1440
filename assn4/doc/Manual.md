# Fractal Visualizer User Manual

To run this program, first open a command line and navagate to the correct directory. You now have several options for how to proceed.

1. run '$ python src/main.py' to create a default fractal and color palette

2. provide only the name of the fractal file you wish to use, which will result in the defualt color palette being used. Example command: '$ python src/main.py data/fulljulia.frac'

3. provide both the fractal file and color palette you wish to use, such as in the example '$ python src/main.py data/funnel-down.frac ColorCube' where funnel-down.frac is the fractal file and ColorCube is the palette. NOTE: fractal files are not required to end in .frac.

For fractal names you can choose between 'mandelbrot', 'julia', or 'burningship'. The availible palettes are called 'palette1' and 'palette2'.

If an invalid or unreachable file or palette name is provided, the program will exit with an error message specifying what went wrong.

A TK window will be opened on your monitor, which is where the program will print the fractal. This will take a few seconds, so don't worry when the full picture does not show up immediately.

Once the picture is printed the program will continue to run until you close the tk image window. At which point you can repeat the process with another fractal name if you would like to.
