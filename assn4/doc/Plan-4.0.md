# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

Program creates fractal images and prints them to screen, this project should clean up the code and make it easy to follow and understand by eliminating code smells/bad practices. Code should be broken up into clear and logical classes, with no repeated or unused code. By the end the output and UI of the program should look exactly the same as when it started, but the code itself should be much neater.

I know how to:
- create a UML document to visualize how the parts of the program  interact
- create and utilize classes
- remove/consolodate redundant code 

potential difficulties:
- writing/modifying tests
- following the math maybe?

## Phase 1: System Analysis *(10%)*

```python
main.py
```
- takes in arguments from command line, prints error messages if wrong/no imput is given
- if no name is given it will print a list of all the fractal names, else it will call the needed functions to continue the program

general purpose: verify the arguments given from the command line


```python
julia_fractal.py
```
- julia_main takes in name of fractal to be printed from main.py, then makes a window and gets the info for the fractal from a dictionary and prints the fractal to the screen
- makePictureOfFractal is supposed to handle the dimensions and canvas object for the fractal. It takes in a dictionary of the fractal dimensions, a row of pixels, a photo object, a color, and the dimensions of the image. 
- getFractalConfigurationDataFromFractalRepositoryDictionary takes in a dictionary and key, then checks to see if that key is present in the dictionary and returns true/false accordingly. (note: is never used)
- getColorFromPalette takes in a set of coordinates in one variable, then determines the color of the pixel.
- contains a list of strings called grad that contains colors, as well as some constants that give names to color code strings
- contains a distionary of all the julia fractals

general purpose: create a picture object, find/get the relevant info about the fractal to be printed, and print the fractal

```python
mbrot_fractal.py
```
- mbrot_main takes in the name of the fractal to be displayed, times how long it takes to print the fractal, prints it, writes it to a png, and prints a report
- colorOfThePixel takes in a set of coordinates in one variable and a list (palette), and returns what color that pixel is, with an error message(?) if something goes wrong 
- paint takes in a dictionary containing dimensions/info for different fractals and the name of a fractal. It then figures out the bounds of the image in relation to the imaginary plane and displays the image to the screen.
- pixelsWrittenSoFar take in rows and cols, and prints out how many pixels have been output so far before returning the number (note: not used)
- contains a dictionary named images, which holds the dimensions for each mbrot fractal
- contains a list (palette) that contains strings of color, as well as several constants that are also color strings

general purpose: create a picture object, find/get the relevant info about the fractal to be printed, and print the fractal. Also print a report about how long the program took to run, how many pixels have been printed so far (?) or an error message if needed.

## Phase 2: Design *(30%)*

```python
Main.py
"""
check to make sure proper number of arguments were given
    if not, issue a usage message & print all fractal names
if given fractal name is not a valid fractal
    issue a usage message & print all fractal names
if a valid name is given, get fractal dimensions and pass into ImagePainter
"""
if len(sys.argv) < 2:
    print("not enough arguments")
    for name in fractalDictionary:
        print("\t{name}")
    sys.exit(1)
elif sys.argv[1] not in fractalDictionary:
    print("invalid fractal name")
    for name in fractalDictionary:
        print("\t{name}")
    sys.exit(1)
else:
    Julia = fractalDictionary['Julia']
    Mbrot = fractalDictionary['Mbrot']
    fracName = fractalDictionary[sys.argv[1]]
    if fracName in Julia:
        fracInfo = Julia[fracName]
        fracType = julia
    else:
        fracInfo = Mbrot[fracName]
        fracType = mbrot
    ImagePainter(fracInfo, fracName, fracType)


```
```python
FractalInformation.py
"""
contain dictionary of all fractal dimensions
"""
fractalDictionary = {'type' : {
                        'name' : {
                            'dimensions' : number,
                            'dimensions' : number,
                            ...},
                        'name' : {
                            'dimensions' : number,
                            'dimensions' : number,
                            ...},
                        ...
                        },
                    'type' : {
                        'name' : {
                            'dimensions' : number,
                            'dimensions' : number,
                            ...},
                        'name' : {
                            'dimensions' : number,
                            'dimensions' : number,
                            ...}
                        ...
                        },
                    ...
                    }

```
```python
def ImagePainter(fracInfo, fracName, fracType)
    """
    start timer
    create a Tk window and PhotoImage object 
    find boundaries of PhotoImage
    paint fractal into PhotoImage object one row of pixels at a time
    stop timer
    write the fractal to a PNG file
    print report
    """
    side = 512
    halfSide = side / 2
    before = time.time()
    window = Tk()
    image = PhotoImage(width=side, height=side)

    minX = fracInfo['centerX'] - (fracInfo['axisLen'] / 2.0)  	         	  
    maxX = fracInfo['centerX'] + (fracInfo['axisLen'] / 2.0)  	         	  
    minY = fracInfo['centerY'] - (fracInfo['axisLen'] / 2.0)
    pixelSize = abs(maxX - minX) / side

    canvas = Canvas(window, width=side, height=side, bg='#000000')
    canvas.pack()
    canvas.create_image((halfSide, halfSide), image=image, state="normal")

    for row in range(side, 0, -1):
        for col in range(side):
            x = minX + col * pixelSize
            y = minY + row * pixelSize
            if fracType = 'julia':
                point = Julia(complex(x,y))
            else:
                point = Mandelbrot(complex(x,y))
            color = Palette(point)
            image.put(color, (col, side - row))
        window.update()

    after = time.time()
    image.write(f"{fracName}.png")
    print(f"Done in {after - before: .3f} seconds!", file=sys.stderr)
    print(f"wrote image {fracName}.png")
    print("Close the image window to exit the program")
    mainloop()
```
```python
def Mandelbrot(point)
    """
    take in a coordinate on a complex plane
    return the iteration count if greater than 2
    else return max possible iteration
    """
    z = complex(0,0)
    for iteration in Palette.length():
        z = z * z + point
        if abs(z) > 2:
            z = float(2)
            return iteration
            sys.exit(1)
    return Palette.length()
```
```python
def Julia(point)
    """
    take in a coordinate on a complex plane
    return the iteration count if greater than 2
    else return max possible iteration
    """
    c = complex(-1.0, 0.0)

    for iteration in Palette.length():
        z = point * point + c
        if abs(z) > 2:
            return iteration
    return Palette.length()
```
```python
Palette.py
"""
declare an array of strings (colors)
"""
palette = ['#ffe4b5', '#ffe5b2', '#ffe7ae', ...]

def Palette(count)
    """
    take in an iteration count number
    make sure that count is not larger than length of array
        if ok, return the color
    """
    if count < len(palette):
        return palette[count]

def length()
"""
return the length of the palette array
"""
    return len(palette)
```


## Phase 3: Implementation *(15%)*

- put main into a function, made syntax edits to make everything callable
- added an argument to ImagePainter that specifies the fractal type
- filled out all of the name and dimension info for FractalInformation
- populated both palette arrays, made the julia palette the correct length

## Phase 4: Testing & Debugging *(30%)*

**test : ran w/o fractal name**
- did not print reminder prompt and list of fractals : had forgotten to actually call the main function
- was now printing the prompt, but printed the whole dictionary instead of just the names; I had organized the dictionary weird, ended up just making a list of all the fractal names for convinience and had it print the list of fractals from that 

**test: ran with 'lakes' name**
- still got messed up with the dictionary ; re-organized the dictionary in a more logical way that also eliminated a 'layer', made it easier to manipulate and get information from
- got an error from tk about not having enough parameters in my image.put() line ; the picture object was not returning properly (was returning None) due to an if tatement never being entered. Fixed the if statement and the error went away
- fractal window now shows up and gets printed to, but only in one shade of blue ; thought I had messed up the math itself, changed > to < but that only made it all yellow instead of blue. Eventually realized that I had replaced z with a different variable, which I think was preventing the math statement from being calculated right in the first place. Replaced the variable with z and picture now prints properly

**unit tests**
- tests palette to make sure it only contains strings
- one test for reach type to ensure palette is correct length
- test to make sure dictionary is correct length
- test to make sure each key in the dictionary has the needed information and dimensions 
- test to make sure the count function returns an int

## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance

**Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
Not sloppy, but I still think the math behind this is confusing. Other than that maybe it might be a bit annoying having to switch between files to follow the path of data through the program 
        *   Are there parts of your program which you aren't quite sure how/why they work?
        the math is a mystery, as is how the dimensions for each fractal have such a big impact
        *   If a bug is reported in a few months, how long would it take you to find the cause?
        maybe an hour? 
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        hopefully, there are descriptions for what each function does
        *   ...yourself in six month's time?
        yes
    *   How easy will it be to add a new feature to this program in a year?
    pretty easy
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        yes
        *   ...the operating system?
        yes
        *   ...to the next version of Python?
        yes (probably)
*   Fill out the Assignment Reflection on Canvas.
