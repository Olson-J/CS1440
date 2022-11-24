# Code Smells Report

## Instructions

Edit this file and include it in your submission.

For each code smell found in the starter code:

*	Note where you found it (filename + relative information to locate the smell)
*	Copy the offensive code
*	Explain why the smell is a problem
*	Describe how you can fix


### These are some of the code smells you may find in the starter code:

0.  "Magic" numbers
    *   Numeric literals that appear in critical places but without any apparent meaning
    *   "When I see the number `214` here, does it have the same meaning as the `214` over there?"
1.  Global variables
    *   A global is being used to avoid passing a parameter into a function
    *   A global is being used to return an extra value from a function
2.  Poorly-named variables
    *   Variables with one-letter long names are okay to use in special contexts; otherwise, they should be avoided
        *   For example, a counter called `i` or `j` used in a `for` loop that is but a few lines long
        *   Variables from well-known math formulae should match the textbook (i.e. `a`, `b` and `c` are familiar in a quadratic or Pythagorean formula)
    *   Variables with really, really long names can make code *less* easy to read
    *   If a programmer is not careful, variables can accidentally override or "shadow" other identifiers in a program
        *   Builtin Python functions such as `input`, `len`, `list`, `max`,
            `min` and `sum` are especially susceptible to this
    *   Variable names should strike a good balance between brevity and descriptiveness
3.  Comments that share too much information
    *   A function or method is filled with many explanatory comments
    *   This is often done because the variable names and function names are poorly chose
    *   Rather, let the code speak for itself
4.  Comments that lie to you
    *   A comment which may have once been helpful, but no longer accurately describes the code
    *   A comment that is straight-up misleading, perhaps written by a developer without a clue
5.  Parameter list that is too long
    *   More than three or four parameters for a method
    *   Parameters that are passed in but left unused
6.  Function/Method that is too long
    *   A method contains too many lines of code
    *   Typically this happens because the method has too many different responsibilities
    *   Generally, any method longer than ten lines should make you ask the question "what if I split this into smaller, more focused pieces?"
7.  Overly complex decision trees
    *   Overly long or deeply nested trees of `if/elif/else`
    *   Are all of the branches truly necessary?
    *   Are all of the branches possible to reach?
    *   Have all of the branches been tested?
8.  Spaghetti code
    *   Lots of meandering code without a clear goal
    *   Many functions/objects used in inconsistent ways
    *   All code is contained in one giant function/method with huge `if/else` branches
    *   "It would be easier to rewrite this than to understand it"
9.  Redundant code
    *   When you see a line of code that is repeated, ask whether it makes any difference to be run more than once.
10. Dead code
    *   A variable, parameter, field, method or class is no longer used (usually because it is obsolete)
    *   Big blocks of commented-out code that serve no purpose and clutter up the file

Other code smells may be present; list them as well.

## Code Smells

0.  `src/main.py`, [lines 36-41, at the very start]
        * [What kind of code smell is this?] **lying comment**
        * [Why is the smell a problem?] it is misleading, the code does the opposite of what the comment says it does
    *   Code Snippet:
```python 
# quit when too many arguments are given 	         	  
if len(sys.argv) < 2:  	         	  
    print("Please provide the name of a fractal as an argument")  	         	  
    for i in JULIAS + MBROTS:  	         	  
        print(f"\t{i}")  	         	  
    sys.exit(1)  	
```
    *   How the code smell was fixed:
        *   [Explain what you changed]] changed the comment to say that the program would quit if too few arguments are given
        


1. `src/main.py`, [lines 55-61, at the end]
        * [What kind of code smell is this?] **lying comment and poorly named variables**
        * [Why is the smell a problem?] the comment suggests that the code will quit with an error message reminding the user how to run the program, but it actually calls the functions needed to 'run' the program. The variable names are bad because sys.argv[1] is put into two different variables, and only one of the variables is actually used.
    *   Code Snippet:
```python 
    # Otherwise, quit with an error message to help the user learn how to run it  	         	  
else:  	         	  
    # fractal is the 1st argument after the program name  	         	  
    fracal = sys.argv[1]  	         	  
    if sys.argv[1] in JULIAS:  	         	  
        julia.julia_main(sys.argv[1])  	         	  
    elif sys.argv[1] in MBROTS:  	         	  
        fratcal = sys.argv[1]  	         	  
        mbrot_fractal.mbrot_main(fratcal)  	
```
    *   How the code smell was fixed:
        *   [Explain what you changed]]remove the redundant variable names and replace with one correctly spelled variable, change the comment to better explain what the code does



2. `src/julia_fractal.py`, [lines 266-270, at the beginning of julia_main()]
        * [What kind of code smell is this?] **global variables, poorly named variables, parameter list is too long, comments that lie, and comments that share too much information**
        * [Why is the smell a problem?] there isn't a need for the variables to be global, they are used and defined in the function, and the comments just take up space without really saying anything useful, or say something that could have been conveyed in a better variable name
    *   Code Snippet:
```python 
    # Look, I  know globals are bad, but I don't know how else to use those  

    # variables in here if I don't do it this way.  I didn't take any fancy CS  	
    # classes, sue me  	         	  
    global tkPhotoImage  	         	  
    global win  	
    # Note the time of when we started so we can measure performance improvements  	         	  
    b4 = time()  	         	  
    # Set up the GUI so that we can display the fractal image on the screen  	         	  
    win = Tk()  	         	  

    # the size of the image we will create is 512x512 pixels  	         	  
    s = 512  	         	  
    # construct a new TK PhotoImage object that is 512 pixels square...  	         	  
    tkPhotoImage = PhotoImage(width=512, height=512)  	         	  
    # ... and use it to make a picture of a fractal  	         	  
    # TODO - should I have named this function "makeFractal()" or maybe just "makePicture"?  	         	  
    makePictureOfFractal(f[i], i, ".png", win, grad, tkPhotoImage, GREY0, 512)
    
    # Write out the Fractal into a .gif image file  	         	  
    tkPhotoImage.write(i + ".png")  	         	  
    print(f"Done in {time() - b4:.3f} seconds!", file=sys.stderr)  
```
    *   How the code smell was fixed:
        *   [Explain what you changed]] make the variables not global, and delete the uneeded comments and the comments that can be replaced by descriptive variable names, fix the .gif comment to say the correct file type. Also rename the function like the comment suggests, and take out some of the uneeded parameters.




3. `src/julia_fractal.py`, [lines 300-319, end of the file]
        * [What kind of code smell is this?] **comment shares too much information**
        * [Why is the smell a problem?] its a huge block of code that is not used, it just takes up space 
    *   Code Snippet:
```python 
    ## This is some weird Python thing... but all of the tutorials do it, so here we go  	         	  
#if __name__ == '__main__':  	         	  
#    # Process command-line arguments, allowing the user to select their fractal  	         	  
#    if len(sys.argv) < 2:  	         	  
#        print("Please provide the name of a fractal as an argument")  	         	  
#        for i in f:  	         	  
#            print(f"\t{i}")  	         	  
#        sys.exit(1)  	         	  
#  	         	  
#    elif sys.argv[1] not in f:  	         	  
#        print(f"ERROR: {sys.argv[1]} is not a valid fractal")  	         	  
#        print("Please choose one of the following:")  	         	  
#        for i in f:  	         	  
#            print(f"\t{i}")  	         	  
#        sys.exit(1)  	         	  
#  	         	  
#    else:  	         	  
#        fratcal_config = getFractalConfigurationDataFromFractalRepositoryDictionary(f, sys.argv[1])  	         	  
#        julia_main(fratcal_config)  	         	  

```
    *   How the code smell was fixed:
        *   [Explain what you changed]] delete the commented out code 



4. `src/julia_fractal.py`, [line 99 - 176, makePictureOfFractal()]
        * [What kind of code smell is this?] **parameter list is too long, poorly named variables, method too long, spaghetti code, comments share too much info** 
        * [Why is the smell a problem?] half the variables passed in are never used, variable names are too vague or too long, lines of code are repeated, more comments than needed. All in all the code is confusing and too long, could be split into smaller pieces. 
    *   Code Snippet:
```python 
def makePictureOfFractal(f, i, e, w, g, p, W, s):  	         	  
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	         	  
    Assumes the image is 640x640 pixels."""  	         	  

    # Correlate the boundaries of the PhotoImage object to the complex  	         	  
    # coordinates of the imaginary plane  	         	  

    # Compute the minimum coordinate of the picture  	         	  
    min = ((f['centerX'] - (f['axisLength'] / 2.0)),  	         	  
           (f['centerY'] - (f['axisLength'] / 2.0)))  	         	  

    # Compute the maximum coordinate of the picture  	         	  
    # The program has only one axisLength because the images are square  	         	  
    # Squares are basically rectangles except the sides are equal instead of different  	         	  
    max = ((f['centerX'] + (f['axisLength'] / 2.0)),  	         	  
           (f['centerY'] + (f['axisLength'] / 2.0)))  	         	  

    # Display the image on the screen  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object = Canvas(win, width=s, height=s, bg=W)  	         	  

    # pack the canvas object into its parent widget  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  	         	  
    # TODO: Sometimes I wonder whether some of my functions are trying to do  	         	  
    #       too many different things... this is the correct part of the  	         	  
    #       program to create a GUI window, right?  	         	  

    # Create the TK PhotoImage object that backs the Canvas Objcet  	         	  
    # This is what lets us draw individual pixels instead of drawing things like rectangles, squares, and quadrilaterals  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.create_image((s/2, s/2), image=p, state="normal")  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # This seems repetitive  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # But it is how Larry wrote it the tutorial  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Larry's a smart guy.  I'm sure he has his reasons.  	         	  

    # Total number of pixels in the image, AKA the area of the image, in pixels  	         	  
    area_in_pixels = 640 * 640  	         	  

    # pack the canvas object into its parent widget  	         	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Does this even matter?  	         	  
    # At this scale, how much length and height of the  	         	  
    # imaginary plane does one pixel cover?  	         	  
    size = abs(max[0] - min[0]) / s  	 
```
    *   How the code smell was fixed:
        *   [Explain what you changed]] get rid of the variables that are passed in and never used and rename the single letter variables, delete all the repeated code and break up the function into smaller, more concise pieces, get rid of the unecessary comments 



5. `src/julia_fractal.py`, [line 145-176, in makePictureOfFractal]
        * [What kind of code smell is this?] **magic numbers, poorly-named variables, comments that give too much information**
        * [Why is the smell a problem?] uses numbers that are not explained and could be put into variables for easier reading, comments take up way to much space and are not straight to the point, uses single letter variable names which is confusing
    *   Code Snippet:
```python 
fraction_of_pixels_writtenSoFar = int(s / 64)  	         	  

    # for r (where r means "row") in the range of the size of the square image,  	         	  
    # but count backwards (that's what the -1 as the 3rd parameter to the range() function means - it's the "step"  	         	  
    # You can actually put any number there that you want, because it defaults to "1" you usually don't have to  	         	  
    # but I have to here because we're actually going BACKWARDS, which took me  	         	  
    # a long time to figure out, so don't change it, or else the picture won't  	         	  
    # come out right
    for r in range(s, 0, -1):
        # for c (c == column) in the range of pixels in a square of size s  	         	  
        for c in range(s):
            # calculate the X value in the complex plane (I guess that's  	         	  
            # actually the REAL number part, but we call it X because  	         	  
            # GRAPHICS... whatev)
            x = min[0] + c * size
            y = 0
            # get the color of the pixel at this point in the complex plain  	         	  
            c2 = getColorFromPalette(complex(x, y))  	         	  
            # calculate the X value in the complex plane (but I know this is  	         	  
            # really the IMAGINARY axis that we're talking about here...)  	         	  
            y = min[1] + r * size
            # TODO: do I really need to call getColorFromPalette() more than once?  	         	  
            #       It feels like that might be kinda slow...  	         	  
            #       But, if it aint broken, don't repair it, right?  	         	  
            # get the color of the pixel at this point in the complex plain  	         	  
            c2 = getColorFromPalette(complex(x, y))
            # put the color c2 into the  	         	  
            p.put(c2, (c, s - r))
            # get the color of the pixel at this point in the complex plain  	         	  
            c2 = getColorFromPalette(complex(x, y))  # does it matter if  	         	  
        w.update()  # display a row of pixels  	         	  
        fraction_of_pixels_writtenSoFar += 640  # update the number of pixels output so far  	         	  

```
    *   How the code smell was fixed:
        *   [Explain what you changed]] rename variables, either explain what the magic numbers do and refer to or put them into a variable, get rid of or shorten the comments



6. `src/julia_fractal.py`, [lines 68-94]
        * [What kind of code smell is this?] **global variables, dead code, repeated code, overly complex decision tree, comments share too much information**
        * [Why is the smell a problem?] global does not need to be global and one is not used, repeated code and extra comments just take up space, could be simplified to make it easier to read, some code cannot be reached
    *   Code Snippet:
```python 
    global grad  	         	  
    global win  	         	  

    # Here 76 refers to the number of colors in the palette  	         	  
    for i in range(78):  	         	  
        z = z * z + c  # Iteratively compute z1, z2, z3 ...  	         	  
        if abs(z) > 2:  	         	  
            return grad[i]  # The sequence is unbounded  	         	  
            z += z + c  	         	  
    # TODO: One of these return statements makes the program crash sometimes  	         	  
    return grad[77]         # Else this is a bounded sequence  	         	  
    return grad[78]

def getFractalConfigurationDataFromFractalRepositoryDictionary(dictionary, name):  	         	  
    """Make sure that the fractal configuration data repository dictionary  	         	  
    contains a key by the name of 'name'  	         	  

    When the key 'name' is present in the fractal configuration data repository  	         	  
    dictionary, return its value.  	         	  

    Return False otherwise  	         	  
    """  	         	  
    for key in dictionary:  	         	  
        if key in dictionary:  	         	  
            if key == name:  	         	  
                value = dictionary[key]  	         	  
                return key  	   
```
    *   How the code smell was fixed:
        *   [Explain what you changed]] get rid of global variables, delete repeated and unused/unreachable code, replace the decision tree with 'if key in dictionary: return key' and get rid of the comments, it is self explanatory
