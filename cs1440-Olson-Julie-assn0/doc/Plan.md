# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

The DuckieDecrypter is an algorythim that decrypts DuckieCrypt, which encodes files given by the user by replacing the first 95 ASCII characters with various characters. DuckieDecrypter will be given a file and decrypt any encoded characters within it while still preserving newlines and ignoring any unencrypted/invalid characters, and will print the decoded message.

The user will be asked to provide a relative path to the file they wish to have decoded
    
- if the given file path is invalid the program will exit and print a 
    warning
- if path is valid
    - program will read through the file character by character,  
        decrypting any any valid DuckieCrypt characters it finds. Invalid 
        characters will be glossed over and produce no output in the final 
        message
    - if the file contains no valid characters the final message will 
        consist of only the file's newlines



A good solution will be easily readable and straightforward to use, and will not crash even if given bad input. The program will warn the user in the case of bad input, and will not modify the user's files while decrypting. It will provide the user with the decoded message in a format true to the original file when printing.

 I know how to:

- check if given file path is good, and exit with a warning message if
        not
- open and read/search files for certain characters, and skip over/
        ignore others
- return a string that contains the desired characters and formatting

I don't know how to/ potential problems:

- will have to figure out how to distinguish punctuation from letters,
        and how to accomodate that when searching for encoded characters
- punctuation seems to have a letter and a number after the 
        distinguishing symbol, program can't only look for the number part of the code

## Phase 1: System Analysis *(10%)*

Input:
- file path, given by the user in an interactive prompt
- the contents of the file, from the file specified in the path

Output
- if file path or file is invalid the output will be a warning message 
        explaining that the program quit and why
- output will be a string which is added to character by character as 
        the message is decoded, and it will be printed out once fully decoded

Algorithms needed:
- algorithm to scan for DuckieCrypt flags
- algorithm(s) to determine what character the code represents, and 
decode it before adding it to the final string
- algorithm to get filename from user


## Phase 2: Design *(30%)*

```python 
def getFile():
"""
    prompt the user for a file path
    check if path is valid
    if valid                            # lines switched places after edit
        return the opened file
    print error message and exit
"""
#file = input("Enter a file path: ")
#if file is invalid:                     # edited: reformatted and now opens file immediately
#    print("Error: invalid file path")
#    exit()
#return open(file, 'r')

print(f"You are located at {os.getcwd()}")
textFile = input("Please select a text file to parse: ")
#if not os.access(textFile, os.R_OK):           # reformatted again
#    print("Error: invalid file path")
#    sys.exit(1)
#return open(textFile, 'r')
if os.access(textFile, os.R_OK):
    return open(textFile, 'r')
#print("Error: invalid file path")              # replaced with a call of sendError()
#sys.exit(1)
sendError(f"Invalid file path")
```

```python
def flagScanner(file): #decryptLine in source code
"""
    #find start of opened file      #removed in edit
    #get file as string
    split file into lines
    check each "word" for a first character of a DuckieCrypt flag (^, _, or +)
    if ^
        pass encryption into whatBigLetter()
    if _
        pass encryption into whatLittleLetter()
    if +
        pass encryption into whatChar()
    return result string
    #if newline character                               # removed; unnecessary
    #    add newline to result string and move on
    # if end of file
    #    print result string (decrypted message) and exit
    #if no flag found/invalid flag                      # removed, redundant
    #    ignore word and continue on
"""
filename.seek(0)
#reading = filename.read()          # removed
test = reading.split()              # changed from reading to filename
for i in test:
    if i[0] == "^":
        result + whatBigLetter(i[1:])       # edited to add char to end string
    elif i[0] == "_":
        result + whatLittleLetter(i[1:])    # edited to add char to end string
    elif i[0] == "+":
        result + whatChar(i[1:])            # edited to add char to end string
#    elif i[0] == 10:
#        result.append(i)
#    elif i[0] == 'NULL':
#        print(result)
#        sys.exit()
#    else:                                  # redundant, removed
#        return ''

```

```python
def whatBigLetter(characterCode)    #convertToUpper in source code
#"""        # rewritten below after edits
#    add 65 to character_code
#    covert from ASCII code to letter
#    return/add letter to result string //CHANGED
#    return decoded letter
#"""
"""
check for characters to decrypt
if characters exist and are in valid range
    add 65 to character_code
    covert from ASCII code to letter and return
else return empty string
"""
#num = characterCode + 65           # rewritten as below
# result.append(chr(num))
#return chr(num)
if charCode == '':
    return ""
elif int(charCode) >= 0 and int(charCode) <= 25:
    num = int(charCode) + 65
    return chr(num)
else:
    return ""
```

```python
def whatLittleLetter(characterCode) #convertToLower in source code
#"""            #rewritten after edits
#    add 97 to character_code
#    covert from ASCII code to letter
#    return/add letter to result string //CHANGED
#    return decoded letter
#"""
"""
check for characters to decrypt
if characters exist and are in valid range
    add 65 to character_code
    covert from ASCII code to letter and return
else return empty string
"""
#num = characterCode + 97           # rewritten as below
# result.append(chr(num))
#return chr(num)
if charCode == '':
    return ""
elif int(charCode) >= 0 and int(charCode) <= 25:
    num = int(charCode) + 97
    return chr(num)
else:
    return ""
```

```python
def whatChar(characterCode) #convertToSpecialChar in source code
#"""                                  # changed along with edits, rewritten below
#    determine what letter the first character of the code is
#    if A:
#        add 32 to the number part of the character_code
#        convert from ASCII code to printable character
#        return/add letter to result string //CHANGED
#    return decoded letter
#    if B:
#        add 91 to the number part of the character_code
#        convert from ASCII code to printable character
#        return/add letter to result string //CHANGED
#        return decoded letter
#    if C:
#        add 123 to the number part of the character_code
#        convert from ASCII code to printable character
#        return/add letter to result string //CHANGED
#        return decoded letter
#"""
"""
determine what letter the first character of the code is
if A:
    make sure there are characters to decode
    if characters exist and are in valid range
        add 32 to the number part of the character_code
        convert from ASCII code to printable character and return
    else return empty string
if B:
    make sure there are characters to decode
    if characters exist and are in valid range
        add 91 to the number part of the character_code
        convert from ASCII code to printable character and return
    else return empty string
if C:
    make sure there are characters to decode
    if characters exist and are in valid range
        add 123 to the number part of the character_code
        convert from ASCII code to printable character and return
    else return empty string
else return empty string
"""
for i in characterCode:
    if i[0] == "A":
        #num = characterCode + 32
        if charCode[1:] == '':              #added in later edit
            return ""
        #num = i[1:] + 32                   #edited at debugging stage, rewritten
        # result.append(chr(num))
        #return chr(num)
        elif int(charCode[1:]) >= 0 and int(charCode[1:]) <= 32:
            num = int(charCode[1:]) + 32
            return chr(num)
        else:
            return ""
    elif i[0] == "B":
        #num = characterCode + 91
        if charCode[1:] == '':
            return ""
        #num = i[1:] + 91                   #edited at debugging, rewritten
        # result.append(chr(num))
        #return chr(num)
        elif int(charCode[1:]) >= 0 and int(charCode[1:]) <= 5:
            num = int(charCode[1:]) + 91
            return chr(num)
        else:
            return ""
    elif i[0] == "C":
        #num = characterCode + 123
        if charCode[1:] == '':
            return ""
        #num = i[1:] + 32                   #edited at debugging, rewritten
        # result.append(chr(num))
        #return chr(num)
        elif int(charCode[1:]) >= 0 and int(charCode[1:]) <= 3:
            num = int(charCode[1:]) + 123
            return chr(num)
        else:
            return ""
    else:                                   # added after original draft
        return ""
```

## Phase 3: Implementation *(15%)*

Completely forgot that there were already named functions in the source code, 
went through and renamed my functions to fit those provided. 

Changed the letter decoding functions to return the letter instead of adding it to the result string

Edited the whatChar/convertToSpecialChar function, added in a for loop to read individual characters and consider only the 2nd/3rd characters of the input character code when adding (was originally trying to add to the whole input code, which included a letter)

Edited getFile and flagScanner to open the file immediately after confirming the user's path, also now splits the file by newlines instead of by spaces. Reformatted getFile for clarity and ease of understanding. Edit: flagScanner does not need to split the file by lines, went back to original plan of splitting the given string by spaces

edited flagScanner/decryptLine to now add the decrypted character to the output string

removed the decryptCharacter() from the source code because it was redundant with how I made the other functions- it's intended job was done by the decryptLine program and convert functions


## Phase 4: Testing & Debugging *(30%)*

**test file: lower.txt**

- tried to concatenate int and str; changed the int number into a string before concatenation
- program would run and not print an error message or the decoded message; fixed missing assignment operator so the result was actually recorded

**test file: specialChars.txt**

- issue with converting the special character codes into ints for math and back into chars for printing?; problem was actually an unnecessary for loop that was trying to read characters sperately before additional decoding, which was causing the program to crash. Removed the for loop and the problem was resolved

**test file: invalid0.txt**

- typeError, couldn't concatenate NoneType to str when decrypting; added an else statement to the if/elif statement that now has the statement return an empty string if the character code is invalid
- program was not registering invalid charCodes (number was too high to be in the specified by the flag, program would process it anyway and end up with the wrong character) ; added in an additional if statement to the convert functions that establishes an upper and lower limit to the recognized charCode numbers, and numbers outside the limit are now correctly considered invalid 
- program counted "++1" as a valid code; made the if statements more specific [instead of returning a char if the code doesn't meet these disqualifying specifications, it is now **only** return a char if the code meets the required specifications]. Default is now return nothing if the program gets confused, instead of returning a character by default

**test file: invalid2.txt**

- invalid literal for int():'' [program was crashing because there was no character code to decrypt]; added if statements to the convertToSpecialChar function to check if there was any characters left to be decrypted. If not the function returns an empty string, if there is then the program continues on normally

## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Review the project to ensure that all required files are present and in correct locations.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
    *   Run through your test cases to avoid nasty surprises.


## Phase 6: Maintenance

**What parts of your program are sloppily written and hard to understand?**
I don't think any of my code is particularly hard to understand, but the convertToSpecialChar function could probably be more compact/efficient.

**Are there parts of your program which you aren't quite sure how/why they work?**
I'm still a little shaky on how os.access and os.R_OK work.

**If a bug is reported in a few months, how long would it take you to find the cause?**
If I could see the input that caused the bug, maybe 30-40 mins?

**Will your documentation make sense to
anybody besides yourself?**
Hopefully, I tried to keep notes of any changes I made and not make it too convoluted

**yourself in six month's time?**
yes

**How easy will it be to add a new feature to this program in a year?**
I'd say between medium and easy difficulty? It would probably take a bit to refamiliarize myself with how the program works, but after that it should be pretty straightforward to add an additional function or something

**Will your program continue to work after upgrading
your computer's hardware?**
I can't think of why it wouldn't

**the operating system?**
Again, can't think of why not but to be fair I don't have a great grasp on the specific differences between common operating systems

**to the next version of Python?**
Yes unless they get rid of functions like int() or chr()
