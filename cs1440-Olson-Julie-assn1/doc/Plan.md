# Software Development Plan

## Phase 0: Requirements Specification *(10%)*
This program aims to provide the user with various tools to use on text files. These tools should be easy to use, and warn the user if any problems such as invalid input files or tool names arise. Summaries for the individual tools below.

**tt.py**
should collect and check the user's input to make sure it is valid, and pass to the appropriate toool
- good input:
    - checks the command line arguments, then passes them to the specified tool 
- bad input:
    - checks command line arguments, if empty/too few/invalid tool name, will call usage() with no arguments
- what I know:
    - how to check for valid input and tool names
- what I don't know:
    - how to pass only some of the arguments into the correct tool


**concat**
should concatenate two files into one output that is printed to the screen with a divider between files, but should not actually modify any of the provided files
- good input:
    - takes 1+ arguments, opens the files to read, prints them line by line to the screen in the order they were given, and closes the files
- bad input:
    - exits as soon as invalid/inaccessible/non-existent files are encountered
    - calls usage() if too few arguments are provided
- what I know:
    -  how to concatenate files
    - how to print files line by line
- what I don't know:
    - how to add the ... division between files


**wc**
should count and print the number of lines, words, and characters present in the given text file. Lines are separated by EOL sequences, words by whitespace, and characters are 1 byte each. If multiple files are given then the total of all given files should be printed
- good input:
    - should count the number of lines/words/characters in all given files, then print the output in columns (all numeric data in clear, distinct columns followed by a column for filenames)
- bad input:
    - exits as soon as an unusable file is encountered (invalid/inaccessible/non-existant), lets open() raise the exception
    - calls usage() if too few arguments are given (must be at least 1)
- what I know:
    - how to divide a file up by lines / whitespace / characters
    - how to track the number of each and format print statements
- what I don't know/potential problems:
    - I use windows so the character count is probably going to be confusing and not match the examples

**head**
should print the first 10 lines of files. Can be given a different number of lines to print by using -n as an argument
- good input:
    - determines the number of lines to be printed. If not default (10), converts the given argument into a number
    - prints the first lines of the file
    - if more than one file is given, divides up the output with banners before each file's content
- bad input:
    - exit as soon as an unusable file is encountered (invalid/inaccessible/non-existent) 
    - exit if too few arguments are provided (must be at least 1)
    - alert the user if the -n argument is used with no number or an invalid number (not an integer)
- what I know:
    - how to convert an argument to an integer
    - how to print a given number of lines from a file
    - how to print banners
- what I don't know:
    - how to print the banners between the files

**grep**
should search the given files for a specified pattern, and print either all lines that match the pattern or all files that do not match the pattern (if -v is used)
- good input:
    - search the files for any occurances of the pattern
    - print either the matches or non-matches depending on whther or not -v was used
- bad input:
    - exit as soon as an unusable file is encountered (invalid/inaccessible/non-existent) 
    - exit when no search term 
    - exit when no filename is provided
- what I know:
    - how to search files for terms
    - how to add matching and non-matching terms to appropriate lists
- what I don't know:
    - if searching for a term anywhere in the line is different than searching for the first few characters of the line

**tail**
should print the final lines of the file. Defaults to 10 lines, but can be given a custom number with the -n argument. If multiple files are given, separate the contents of each with a banner when printing
- good input:
    - determines the number of lines to be printed. If not default (10), converts the given argument into a number
    - prints the last lines of the file
    - if more than one file is given, divides up the output with banners before each file's content
- bad input:
    - exit as soon as an unusable file is encountered (invalid/inaccessible/non-existent) 
    - exit if too few arguments are provided (must be at least 1)
    - alert the user if the -n argument is used with no number or an invalid number (not an integer)
- what I know:
    - how to convert an argument to an integer
    - how to print a given number of lines from a file
    - how to print banners
- what I don't know:
    - how to print the banners between the files

**sort**
should use python's sorting functions to print the contents of files in lexical order (alphabetical but based on ASCII, so it includes punctuation and non-letter characters). If multiple files are given, the results should be mixed together and not separated by file when sorted
- good input:
    - should sort the contents of all files given into lexical order, and then print the results
- bad input:
    - exits as soon as an unusable file is encountered (invalid/inaccessible/non-existent) 
    - call usage() if too few arguments are given (must be at least 1)
- what I know:
    - how to sort a file by ASCII values
- what I don't know:
    - how to mix the results of multiple files

**tac**
should function the same as cat, but print each line of the files in reverse order while keeping the files themselves in the same order they were given in
- good input:
    - takes 1+ arguments, opens the files to read, prints them line-by-line in reverse order while maintaining the original order of the files themselves
- bad input:
    - exits as soon as invalid/inaccessible/non-existent files are encountered
    - calls usage() if too few arguments are provided
- what I know:
    - how to concatenate files
    - how to print files line by line
- what I don't know:
    - how to print the lines in reverse order

**cut**
should extract fields of data from a single CSV file, split the lines up by commas, and print the 1st field by default. The -f flag can be used to specify which field to extract by number (starts with 1, not 0)
- good input:
    - extract fields from file and split lines up by commas
    - print the specified fields in ascending order, even if multiple fields are given  
- bad input:
    - if the given field number is larger than the actual number of fields, the fields should be treated as if they are empty and NOT raise an index error
    - exits as soon as invalid/inaccessible/non-existent files are encountered
    - calls usage() if too few arguments are provided
    - reports an error if the -f switch is not given an argument, or if it is given a negative/invalid input
- what I know:
    - how to split files by commas
    - how to call errors
    - how to format print statements
- what I don't know/potential problems:
    - how to always print the fields in ascending order

**paste**
should join lines from 2+ files together with a comma to separate them. If only one file is given then function behaves like cat
- good input:
    - open all the given files and store the resulting file object in a list, which is then used to print the results. One line from each file is read and printed with commas taking the place of the newline characters. This list is looped over until all files are exhausted, with any missing fields being empty strings.
    - if the > operator is used, the results will be redirected into a new file (data/people.csv)
- bad input:
    - exits as soon as invalid/inaccessible/non-existent files are encountered
    - calls usage() if too few arguments are provided
- what I know:
    - how to read lines from a file and return a file object to a list
    - how to print a list and format it
- what I don't know:
    - how to redirect into a new file


## Phase 1: System Analysis *(10%)*

**inputs:**
- tool name; comes from the command line, gets checked in tt.py and then called if ok
- flag/formatting argument; from command line, checked in tt.py, then passed into the specified tool
- file names; from command line, through tt.py, passed into tool

**output**
- formatted print statement(s), which are different for each tool 
- error messages, if needed. These are the same for the whole program and will only change based upon the type of error thrown

**algorithms needed**
- input check
- algorithm to open and read file(s) and close them later
- split file(s) into lines, and print specified lines 
- split into lines/words/characters, and print in a formatted statement 
- search them for a sequence of characters, sort the output into mathcing or non-matching lists, and print whichever list was specified
- sort the contents into lexical order and print
- get data from a CSV file, split it up by commas, and print in ascending order
- get data from multiple files and print certain pieces next to each other, separated by commas

## Phase 2: Design *(30%)*

**Deliver:**
*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.

```python 
def tt.py(args):
    """
    check that at least 2 arguments have been given
    if less than 2 exit and call usage() for error message
    else check which tool was called and forward remaining arguments
    if not a valid tool name, call usage
    """
if len (sys.argv) < 2:
    usage()
else:
    args = argv[2:]
    if sys.argv[1] = "cat":
        return cat(args)
    elif sys.argv[1] = "tac":
        return tac(args)
    elif sys.argv[1] = "cut":
        return cat(args)
    elif sys.argv[1] = "paste":
        return paste(args)
    elif sys.argv[1] = "grep":
        return grep(args)
    elif sys.argv[1] = "head":
        return head(args)
    elif sys.argv[1] = "tails":
        return tails(args)
    elif sys.argv[1] = "sort":
        return sort(args)
    elif sys.argv[1] = "wc":
        return wc(args)
    usage(Invalid tool name)

```

```python
def cat(args):
    """
    make sure there is at least 1 filename given
    if not call usage and exit
    open files and make sure they are accessible, if not open() will raise an error
    print entire file line by line 
    if more than one file, print '...' divider and repeat until done
    close file
    """
if (len(args) < 1):                             # makes sure at least 1 file is given
    usage(Must provide at least 1 filename)
for i in args:                                  # repeats for each filename given
    file = open(args[i], 'r')                   # opens file for reading, error if invalid 
    for line in file.readlines():               # splits file into lines
        print(line)                             # prints each line
    if (len(args) > 1):                         # checks if there is more than one file
        print("...")                            # if yes prints divider between outputs
    file.close()                                # closes file
```

```python
def wc(files):
    """
    make sure at least 1 filename was provided
    if not call usage and exit
    for each file provided:
        open file for reading
        split file into lines, find number of lines
        split file into words, find number of words
        split file into charcters, find number of characters
        print line #, word #, char #, and filename
        close file
    """
if (len(args) < 1):                             # makes sure at least 1 file is given
    usage(Must provide at least 1 filename)
for i in args:                                  # repeats for each filename given
    file = open(args[i], 'r')                   # opens file for reading, error if invalid 
    lineCount = 0
    wordCount = 0
    charCount = len(file)                       # counts chars in file
    for line in file.readlines():               # splits file into lines
        lineCount += 1                          # counts number of lines
    for j in file.split():                      # splits file by whitespace
        wordCount += 1                          # counts number of words
    
    print(f"{lineCount}   {wordCount}   {charCount}   " + args[i])
    file.close()
```

```python
def head(args):
    """
    make sure at least 1 filename was provided
    if not call usage and exit
    check if -n argument was used
    if yes:
        convert given number to an integer (make sure is valid, call usage if not)
        print warning if no number was given
        for each file provided:
            if more than 1 file was provided:
                print banner with filename
            open file for reading
            split file into lines
            print first n lines
            close file
    if not:
        for each file provided:
            if more than 1 file was provided:
                print banner with filename
            open file for reading
            split file into lines
            print first 10 lines
            close file
    """
if (len(args) < 1):                             # makes sure at least 1 file is given
    usage(Error: Too few arguments)
if args[0] = "-n":
    if (len(args) < 2):                             # makes sure at least 1 file is given
    usage(Error: Too few arguments)
    n = args[1]
    if not n.isdigit():
        Usage(Error: Number of lines required)
    n = int(n)
    for i in args[2:]:                                  # repeats for each filename given
        if (len(args[2:]) > 1):                         # banner if multiple files
            print("==> " + args[i] + " <==") 
        file = open(args[i], 'r')                       # opens file for reading, error if invalid 
        file = file.readlines()                         # splits file into lines
        j = 0
        while j < n:                                    # prints n lines
            print(file[j])
            j++
        file.close()
else:
    for i in args[]:                                  # repeats for each filename given
        if (len(args) > 1):                         # banner if multiple files
            print("==> " + args[i] + " <==") 
        file = open(args[i], 'r')                       # opens file for reading, error if invalid 
        file = file.readlines()                         # splits file into lines
        j = 0
        while j < 10:                                    # prints 10 lines
            print(file[j])
            j++
        file.close()
    
```

```python
def grep(args):
    """
    make sure at least 1 filename and a search term was provided
    if not call usage and exit
    make empty match list
    make empty non-match list
    if -v argument was used:
        for each file provided:
        open the file for reading
        split file into lines
        search each line for the given pattern
        put each line in either the match or non-match list
        close file
        print the non-matching list
    else:
        for each file provided:
        open the file for reading
        split file into lines
        search each line for the given pattern
        put each line in either the match or non-match list
        close file
        print the matching list
    """
if (len(args) < 2):                             # makes sure at least 1 file and a pattern is given
    usage(Error: Please provide a pattern and at least one filename)
match = []                                      # create empty lists
noMatch = []
if args[0] = "-v":                              # if -v arg was used then the next argument is the pattern
    for i in args[2:]:                          # for each file listed
        file = open(args[i], 'r')                   # open
        for line in file.readlines():               # split into lines and search for pattern
            if args[1] in line:                     # sort into lists
                match.append(line)
            else:
                noMatch.append(line)
        file.close()                                # close file
        for i in noMatch:                           # print list
            print(noMatch[i])
else:
    for i in args[1:]:                          # first arg is pattern, repeat for each file listed
    file = open(args[i], 'r')                   # open
    for line in file.readlines():               # split into lines and search for pattern
        if args[0] in line:
            match.append(line)                  # sort into lists
        else:
            noMatch.append(line)
    file.close()                                # close file
    for i in match:                             # print list
        print(match[i])
```

```python
def tail(args):
    """
    make sure at least 1 filename was provided
    if not call usage and exit
    check if -n argument was used
    if yes:
        convert given number to an integer (make sure is valid, call usage if not)
        print warning if no number was given
        for each file provided:
            if more than 1 file was provided:
                print banner with filename
            open file for reading
            split file into lines
            print last n lines
            close file
    if not:
        for each file provided:
            if more than 1 file was provided:
                print banner with filename
            open file for reading
            split file into lines
            print last 10 lines
            close file
    """
if (len(args) < 1):                             # makes sure at least 1 file is given
    usage(Error: Too few arguments)
if args[0] = "-n":
    if (len(args) < 2):                             # makes sure at least 1 file is given
    usage(Error: Too few arguments)
    n = args[1]
    if not n.isdigit():
        Usage(Error: Number of lines required)
    n = int(n)
    n = n - (n * 2)                                     # makes n negative
    for i in args[2:]:                                  # repeats for each filename given
        if (len(args[2:]) > 1):                         # banner if multiple files
            print("==> " + args[i] + " <==") 
        file = open(args[i], 'r')                       # opens file for reading, error if invalid 
        file = file.readlines()                         # splits file into lines
        j = 0
        while j > n:                                    # prints n lines
            print(file[j])
            j--
        file.close()
else:
    for i in args[]:                                  # repeats for each filename given
        if (len(args) > 1):                         # banner if multiple files
            print("==> " + args[i] + " <==") 
        file = open(args[i], 'r')                       # opens file for reading, error if invalid 
        file = file.readlines()                         # splits file into lines
        j = -10
        while j < 0:                                    # prints 10 lines
            print(file[j])
            j++
        file.close()
    
```

```python
def sort(args):
    """
    make sure at least 1 filename was provided
    if not call usage and exit
    for ever file given:
        open file for reading
        split into lines
        add lines into a total list
        close file
    sort file into lexical order
    print sorted list
    """
if (len(args) < 1):                             # makes sure at least 1 file is given
    usage(Must provide at least 1 filename)
total = []
for i in args:                                  # repeats for each filename given
    file = open(args[i], 'r')                   # opens file for reading, error if invalid 
    for line in file.readlines():               # splits file into lines
        total.append(line)                      # adds all lines to one list
    file.close()                                # close file
total.sort()                                    # sort list 
for i in total:                                 # print list
    print(i)
```

```python
def tac(args):
    """
    make sure there is at least 1 filename given
    if not call usage and exit
    open files 
    if more than one file, print '...' divider and repeat until done
    print entire file line by line, backwards
    close file
    """
if (len(args) < 1):                             # makes sure at least 1 file is given
    usage(Must provide at least 1 filename)
for i in args:                                  # repeats for each filename given
    file = open(args[i], 'r')                   # open file
    x = len(file.readlines())                   # finds number of lines in file
    while x > 0:                                # prints each line, starting with the last
        print(file[x])
        x--
    if (len(args) > 1):                         # checks if there is more than one file
        print("...")                            # if yes prints divider between outputs
    file.close()                                # closes file
```

```python
def cut(args):
    """
    make sure at least one file is given
    if not call usage
    if -f flag used:
        make sure number was given, if not call usage
        make empty list for numbers
        for each number given:
            convert number into an int, make sure positive and valid and add to list
        sort list 
        for each number in list:
            for each file listed:
                open file
                split file into lines
                for each line:
                    split lines by commas
                    if field blank:
                        print(\n)
                    else:
                        print(first field)
                close file
    else:
        for each file listed:
            open file
            split file into lines
            for each line:
                split lines by commas
                if field blank:
                    print(\n)
                else:
                    print(first field)
            close file
    """
if (len(args) < 1):                                 # makes sure at least 1 file is given
    usage(Error: Too few arguments)
if args[0] = "-f":
    if (len(args) < 2):                             # makes sure at least 1 file is given
        usage(Error: Too few arguments)
    field = args[1].split(",")                      # splits the listed fields by commas
    order = []
    for i in field:                                 # for each field listed
        f = field[i]
        if not f.isdigit():                         # error if not a valid number
            Usage(Error: A comma-separated field specification is required)
        f = int(f)                                  # make into an int
        if f < 0:                                   # error if negative
            Usage(Error: A comma-separated field specification is required)
        order = order.append(f)                     # add checked number into list
    order = sorted(order)                           # sort list, numbers now in ascending order
    for i in order:                                 # for each field in the list
        for j in args[2:]:                          # repeats for each filename given
            file = open(args[j], 'r')               # open file
            for line in file.readlines():           # splits file into lines
                file = line.split(",")              # splits each line by commas
                if file[f] = NULL:                  # if empty field print newline
                    print("\n")
                else:                               # else print field
                    print(file[f])
            file.close()
else: 
    for i in args[2:]:                          # repeats for each filename given
        file = open(args[i], 'r')               # open file
        for line in file.readlines():           # splits file into lines
            file = line.split(",")              # splits each line by commas
            if file[1] = NULL:                  # if empty field print newline
                print("\n")
            else:                               # else print field
                print(file[1])
        file.close()
```

```python
def paste(args):
    """
    check at least one file was given
    if not call usage
    for each file given:
        open file
        break into lines
        add each line to a fileList
        then add the fileList to a masterList, creating a 2D array
        close files
    for i in (len of longest list):
        if number of files > 1:
            if field blank:
                print(",")
            else:
                print(field) from list each fileList, end = ","
        else:
            print(field) from list

    """
if (len(args) < 1):                                 # makes sure at least 1 file is given
    usage(Error: Too few arguments)
oneListToRuleThemAll = []
count = 0
for i in args:
    listCount = 0                                   # will keep track of how many lines are in each file
    file = open(args[i], 'r')                       # open file
    babyList = []
    for line in file.readlines():                   # split into lines, repeat for each line
        babyList.append(line)                       # adds lines to a list
        listCount++
    oneListToRuleThemAll.append(babyList)           # creates a 2D array of the file lists
    if (count < listCount):                         # will keep track of the longest file length
        count = listCount
    file.close()

for i in count:                                     # repeats until the end of the longest file list
    if len(args) > 1:                               # if more than one file was provided
        for j in len(oneListToRuleThemAll):         # will repeat for correct field in each file list
            if oneListToRuleThemAll[j][i] = NULL:   # if the field is empty just print a comma
                print(",")
            else:
                print(oneListToRuleThemAll[j][i], end = ",")   # if not empty print the element
    else:                                           # if only one file is provided
        print(oneListToRuleThemAll[0][i])           # print the field 
```


## Phase 3: Implementation *(15%)*

**tt.py**
- replaced all = with ==
- since the source code isn't actually a function took out all return statements
- added quotes around the error message in usage call


**cat**
- added quotes to usage call


**wc**
- had "Expected type 'Sized', got 'TextIO' instead" warning on opened file object when I tried to find the length of it, fixed it (it wasn't reading the file first)
- realized that I passed args into the function but the function then called it files, changed the argument name in the function to args for consistency


**head**
- minor format editing


**grep**
- minor formatting edits
- unexpected type 'str' error in print statements, not sure why 


**tail**
- minor format edits


**sort**
- minor format edits


**tac**
- minor format edits


**cut**
- minor format edits
- getting warning that variable might be used before assignment, not sure why as its defined earlier in the loop


**paste**
- minor format edits
- two warnings about "Expected type 'collections.Iterable', got 'int' instead", not sure why or how to fix it right now


## Phase 4: Testing & Debugging *(30%)*

**test: ./scripts/testUsage.sh**
- everything looks ok until it hit just after wc, then there was a traceback error because I had argv in the code instead of sys.argv ; was not actually a problem in wc, it was in tt.py and I'm surprised it managed to print as much as it did. I fixed it so it now says sys.argv
- now got through just as much of the output as last time, but now the traceback errors say usage is not defined ; I forgot to import usage in all of the tool programs, I fixed it and now the test results in a long output that seems to be testing my error statements?
- occasionally it will print along the lines of "Error: Error: ...", not sure why error is printing twice ; I forgot that the usage() print statement already says error and had written some of the error messages with an additional error. I removed the error bit of the messages and it fixed itself


**test: .scripts/testCat.sh**
- printed error correctly when cat was called with no arguments, but had a problem with data/let3 because the for loop was trying to open files to a string element instead of an int ; changed the for loop to a while loop so everything involved in the process is now an int
- got farther this time, made it to a test with multiple files but printed an error message at the end of the output chunk ; realized that since the tt.py was not actually a function and I removed all the return statements the code fell through to the end of the if/else/elif statements that check for tool names. Changed the invalid tool name error to be in an else statement instead of being the fallthrough 
- found out the different file outputs were not actually supposed to be separated by ...; took that chunk of code out of both cat and tac
- printed a blank line between each line of the output ; I think the problem might have been because I use windows and the end of file sequence is \r\n instead of just \n. I stripped the string before printing and it fixed it


**test: ./scripts/testTac.sh
- same problem with the for loop as cat ; also changed it to a while loop
- got a typeError when I tried to print a file from the array ; changed how I reversed the array of lines in the file, now uses the reverse function
- same extra line problem as cat ; added .strip()

**test: ./scripts/testWC.sh**
- had same problem with indices as cat ; changed for loop to while loop
- got type error when trying to find word count, I was trying to split the whole file instead of lines ; I was missing a tab in a for loop
- line and word count variables were not getting incremented, the for loops were not ever being called ; got rid of the for loops, used len, read, and split to determine values
- output formatting was not in consistent lines ; now has a more rigid format that uses .format()

**test: ./scripts/testHead.sh**
- list indices error ; changed for loop to a while loop
- printed extra lines ; used .strip()
- in loop to print 10 default lines got an index out range error ; added an additional if statement and while loop to check the number of files before printing as many as possible or the default of 10
- type error with indices ; added an additional variable 
- issues with index range and typeErrors ; added new variables and rearranged the loops to keep things from overlapping and getting overridden

**test: ./scripts/testTail.sh**
- raised invalid tool name error for every test file ; I had written 'tails' instead of 'tail' in the toolname check in tt.py
- same issue with indices as the last few tools ; added another counting variable to prevent overwriting
- list index out of range for some files, printed extra lines for others ; now uses .strip() and added another variable and if statement to prevent index errors. Also now uses reversed() to print the lines backwards because it's more efficient than what I had before


**test: ./scripts/testSort.sh**
- same indices problem and extra lines (noticing a theme here lol) ; added another count variable to prevent overwriting, uses strip('\n') to get rid of newlines but not the formatting whitespace on some of the quote documents


**test: ./scripts/testPaste.sh**
- indices problem again, added another count variable
- couldn't iterate through an int ; changed for loop to while loop
- NULL not defined ; put it in single quotes, no longer thinks NULL is a constant variable
- formatting of output was weird, newlines and commas didn't look right ; messed around with the print statements and added some more if statements to determine where and how everything should print 
- was only printing one line of output for each test, even though there was more data in the files ; messed around with stuff and kept making it worse, decided to scrap the second half of the program and ended up rewriting it 
- would only print a comma once even if it was printing two empty fields. was not actually printing anything for any of the empty fields ; because I used essentially a ragged array the program was not registering that the fields were empty because they just didn't exist. I added a for loop that adds filler values to each list until they are the same length as the longest file list, and adjusted the print statements slightly so the commas wouldn't show up on the end of the output lines


**test: ./scripts/testCut.sh**
- fileNotFound error in cat, no file '-f' ; accidentally wrote cat instead of cut in tt.py
- noneType object was causing several errors ; didn't understand how to use .append() properly when I wrote it, reformatted it to use it properly
- was not printing anything other than the occasional error message ; decided to rewrite it using a skeleton from paste
- output not formatted correctly ; I tried man idk whats wrong with it


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

    *   What parts of your program are sloppily written and hard to understand?
    the cut and paste tools both turned out... not great
        *   Are there parts of your program which you aren't quite sure how/why they work?
        the print part of paste is confusing, and it's a small miracle the print part of cut works at all, even if it's not perfect
        *   If a bug is reported in a few months, how long would it take you to find the cause?
        if it was in any tool other than cut/paste, maybe an hour. if it was in paste maybe 1.5? I don't think I'd be able to find it in cut
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        hopefully on everything other than cut/paste yes. Not even I really understand what happened with cut 
        *   ...yourself in six month's time?
        same as above
    *   How easy will it be to add a new feature to this program in a year?
    depending on where it gets added to either fairly easy or nearly impossible
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        it should
        *   ...the operating system?
        it should
        *   ...to the next version of Python?
        hopefully? idk
*   Fill out the Assignment Reflection on Canvas.
