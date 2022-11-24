# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

Program creates fractal images and prints them to screen, this project aims to apply object-oriented design principles to make the program easy to test and modify later on. The program should accept files in a standard format from the command line and run essentially the same as it did originally, but the code should now be reorganized to use the strategy and factory methods of design, inheritance, and polymorphic classes. Users will be able to choose which algorythm to use from the command line.

I know how to:
- reorganise code to use inheritance
- determine which algorythm to use based on user input
- how to create subclasses

potential difficulties: 
- understanding factory method and strategy designs
- error checking/handling

## Phase 1: System Analysis *(10%)*

imput comes from the command line and contains the name of the fractal configuration file and (optionally) the name of the palette to be used/produce. If the file name is misspelled or un-openable an error is thrown, and if an invalid palette is named the program exits with an error message. If no file name is provided the program creates a default fractal, and if no palette is given a default palette is created and used. 

The fractal configuration file is then converted into a dictionary, which will require some processing to clean up the data. If required items are not present, incorrect data types are provided, or a value is left blank  an error is thrown.

**abstract Fractal class:** will provide a template/structure for the classes that inherit from it. Will contain a placeholder count() method and can contain other methods or data members

**Julia, Mandelbrot, other classes:** inherits from Fractal, will override count() to take a complex number as input and return an int (number of iterations). Will need to have basic info stored with self

**Palette class:** provides a template/structure for subclasses. provides a placeholder getColor() method, and can contain other methods and data structures as needed. 

**two subclasses of Palette:** will provide alternate color palettes, the creation of which uses a user-specified number of iteration instead of hard-coded arrays of colors. getColor() will take an int as input, and return a string which represents a color in #RRGGBB format.

**FractalParser:** verifies the .frac file provided is correctly formatted and converts its contents into a dictionary. Will raise a runtime error if a problem occurs

**FractalFactory:** takes input from FractalParser, returns a concrete fractal object. If no input is given, produces a default fractal configuration object. If the fractal given is missing or inaccessible, open() will fail. If the fractal type is not recognized or the configuration file contains other errors, an error is raised

**PaletteFactory:** takes input from FractalParser, returns a concrete palette object. If no palette is selected on the command line, a default is used. If a non-existent palette is given, an error is raised.

**ImagePainter:** imports and uses tkinter, and takes input from FractalFactory and PaletteFactory. Outputs the image, pretty much like it did last sprint, only now the code is a class and does not use if/else statements to figure out what kind of fractal is being made.

## Phase 2: Design *(30%)*

```python
class main
"""
takes input from command line
call fractalparser (clean data + dictionary)
call palettefactory --> palette -->palette subclass (get palette object)
call fractalfactory --> fractal --> fractal subclass (get fractal object)
feed into imagepainter
"""
if len(sys.argv) = 1:                   #no filename given, defaults
    fractal = FractalFactory(FractalParser(''))
    palette = PaletteFactory('')

elif len(sys.argv) = 2:                 # filename, default palette
    fractal = FractalFactory(FractalParser(sys.argv[1]))
    palette = PaletteFactory('')

elif len(sys.argv) = 3:                 # no defaults
    fractal = FractalFactory(FractalParser(sys.argv[1]))
    palette = PaletteFactory(FractalParser(sys.argv[2]))

ImagePainter(fractal, palette)

```
```python
def isTypeConvertible(value, ofType):
    try:
        ofType(value)
        return True
    except ValueError:
        return False
```

```python
class FractalParser(filename)
"""
validify file/open file
clean up data
error checks
make dictionary and return
"""
#establish a default set of values
if filename == '':
    dictionary = {'type': 'mandelbrot', 
                'pixels':640,
                'axisLength': 4.0,
                'iterations': 100,
                'min':{'x':-2.0, 'y':-2.0},
                'max':{'x':2.0, 'y':2.0},
                'pixelsize':0.00625}
else:
    rec = 0
    dictionary = {}
    file = open(filename)
    for line in file:
        if '#' in line:             # skip line if comment
            readline() #file.readline? pass? idk
        if '' in line:              # blankline?
            pass
        line.strip()                # strip whitespace
        line.lower()                # make lowercase

        if 'type' in line:          # check for required info and types
            line.split(":")
            if isTypeConvertible(line[1], str):
                dictionary['type'] = line[1]
            else:
                raise error("incorrect data type for required info")
                sys.exit(1)
        if 'centerx' in line:          # check for required info and types
            line.split(":")
            rec++
            if isTypeConvertible(line[1], float):
                centerX = float(line[1])
            else:
                raise error("incorrect data type for required info")
                sys.exit(1)
        if 'centery' in line:          # check for required info and types
            line.split(":")
            rec++
            if isTypeConvertible(line[1], float):
                centerY = float(line[1])
            else:
                raise error("incorrect data type for required info")
                sys.exit(1)
        if 'axislength' in line:          # check for required info and types
            line.split(":")
            if isTypeConvertible(line[1], float):
                axisLength = float(line[1])
                dictionary['axisLength'] = float(line[1])
            else:
                raise error("incorrect data type for required info")
                sys.exit(1)
        if 'pixels' in line:          # check for required info and types
            line.split(":")
            if isTypeConvertible(line[1], int):
                pixels = int(line[1])
                dictionary['pixels'] = int(line[1])
            else:
                raise error("incorrect data type for required info")
                sys.exit(1)
        if 'iterations' in line:          # check for required info and types
            line.split(":")
            if isTypeConvertible(line[1], int):
                dictionary['iterations'] = int(line[1])
            else:
                raise error("incorrect data type for required info")
                sys.exit(1)
        if 'creal' in line:
            line.split
            if isTypeConvertible(line[1], float):
                dictionary['creal'] = float(line[1])
            else:
                raise error("incorrect data type for required info")
                sys.exit(1)
        if 'cimag' in line:
            line.split
            if isTypeConvertible(line[1], float):
                dictionary['cimag'] = float(line[1])
            else:
                raise error("incorrect data type for required info")
                sys.exit(1)

if rec = 2:
    minX = centerX - (axisLength / 2.0)
    minY = centerY - (axisLength / 2.0)
    dictionary['min'] = {'x':minX, 'y':minY}
    maxX = centerX + (axisLength / 2.0)
    maxY = centerY + (axisLength / 2.0)
    dictionary['max'] = {'x':maxX, 'y':maxY}

    pixelsize = float(axisLength / pixels)
    dictionary['pixelsize'] = pixelsize
else:
    raise error("missing required information")
    sys.exit(1)

# check all required data is present
if dictionary['type'] == 'julia' or dictionary['type'] == 'burningshipjulia':
    if 'creal' not in dictionary or 'cimag' not in dictionary:
        raise error("missing required information")
        sys.exit(1)

if 'type' not in dictionary or 'pixels' not in dictionary or 'axisLength' not in dictionary or 'iterations' not in dictionary or 'min' not in dictionary or 'max' not in dictionary or 'pixelsize' not in dictionary:
    raise error("missing required information")
    sys.exit(1)

file.close()
return dictionary
```

```python
class FractalFactory(dictionary)
"""
take in dictionary
check type
make object
error checks
"""
import fractal subclasses
if '' in dictionary:                #default
    return mandelbrot()
if dictionary['type'] == julia:
    return julia(dictionary['creal'], dictionary['cimag'])
if dictionary['type'] == mandelbrot:
    return mandelbrot()
if dictionary['type'] == burningshipjulia:
    return burningshipjulia(dictionary['creal'], dictionary['cimag'])
```


```python
class PaletteFactory(paletteName)
"""
take in dictionary from parse
if not parse, default
make palette object
error checks
"""
import palette subclasses

if paletteName == 'palette1' or paletteName == '':
    return palette1()
elif paletteName == 'palette2':
    return palette2()
else:
    raise NotImplementedError("Invalid palette requested")
```

```python
class Palette:
"""
template class
empty getColor() method
"""
    def getColor(int):
        raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")
```

```python
class palette1:
"""
overide getColor()
    make palette
    return String of #rrggbb
"""
    import color
    def getColor(int):
        return Color.get_hex_l(int)
```
```python
class palette2:
"""
overide getColor()
    make palette
    return String of #rrggbb
"""
    import color
    def getColor(int):
        return Color.get_hex_l(int)
```
```python
class Fractal(dictionary)
"""
template class
empty count() method
"""
def __init__(self, dictionary):
    self.fracInfo = dictionary
def count(complex):
    raise NotImplementedError("Concrete subclass of Fractal must implement count() method")

```

```python
class Julia(creal, cimag):
"""
override count()
    take in complex number
    return int of iterations
"""

    def count(z, iterations):
        c = complex(creal, cimag)
        for iteration in iterations:
            z = z * z + c
            if abs(z) > 2:
                return iteration
        return iterations
```

```python
class Mandelbrot:
"""
override count()
    take in complex number
    return int of iterations
"""

    def count(c, iterations):
        z = complex(0.0,0.0) 
        for iteration in iterations:
            z = z * z + c
            if abs(z) > 2:
                return iteration
        return iterations
```

```python
class burningshipjulia(creal, cimag):
"""
override count()
    take in complex number
    return int of iterations
"""
def count(z, iterations):
        c = complex(creal, cimag)
        for iteration in iterations:
            absZ = complex(abs(z.real), abs(z.imag))
            z = absZ * absZ + c
            if abs(z) > 2:
                return iteration
        return iterations
```

```python
class imagePainter(fractal, palette)
"""
take in objects from fractal and palette factories
loop of all pixels, find complex number
    give pixel value to object.count() (returns int)
    pass int to palette object.getColor() to get color string
"""
#before = time.time()
side = fractal.dictionary['pixels']
window = Tk()
image = PhotoImage(width = side, height = side)

canvas = Canvas(window, width = side, height = side, bg='#000000')
canvas.pack()
canvas.create_image((side / 2, side / 2), image=image, state="normal")

for row in range(side, 0, -1):
    for col in side:
        x = fractal.dictionary['minX'] + col * fractal.dictionary['pixelsize']
        y = fractal.dictionary['minY'] + row * fractal.dictionary['pixelsize']
        num = fractal.count(complex(x,y), fractal.dictionary['iterations'])
        color = palette.getColor(num)
        image.put(color, (col, side - row))
    window.update()

```

## Phase 3: Implementation *(15%)*

- added functions to classes rather than just having loose code in the classes
- will have to fix the error statements later
- lots of things being marked as uncallable

## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.

**ran with no parameters**
- would not call functions in classes properly; added __init__ functions to classes and subclasses, realized I was calling modules wrong 

**ran with filename**
- file was not opening correctly ; 
- raise error statements were causing errors (not the ones they were supposed to) ; 
- was not reading file correctly, wasn't skipping commented out lines or splitting the line on the : properly; made statements if/elif rather than all ifs, reassigned the value of line to the split statement so the changes actually did something

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
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   Fill out the Assignment Reflection on Canvas.
