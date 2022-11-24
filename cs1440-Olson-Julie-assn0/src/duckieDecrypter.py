#!/usr/bin/env python
#                         ~
#                        (o)<  DuckieCorp Software License
#                   .____//
#                    \ <' )   Copyright (c) 2022 Erik Falor
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# Permission is NOT granted, to any person who is NEITHER an employee NOR
# customer of DuckieCorp, to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the
# following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

# Feel free to start from scratch, or repurpouse any of these suggested functions! The world is yours. 
#   Well, maybe that was a bit of an over exaggeration. The world isn't only *yours*, but this text file sure is. 

import sys
import os
# msg can just be an fString
def sendError(msg=None):
    '''
Exits the program after displaying `msg` as an error message. If no string
input is provided, the default message is "Error! An error was encountered, so
the program is quitting."
    '''
    # Dear Future Dev,
    # The code below is fine. Your work is not needed on `sendError`.
    # You are more than welcome to edit the string literal, especially to make
    # a more vocal and unique quack.
    if msg is None:
        msg = "Error! An error was encountered, so the program is quitting."
    print(f"""\
!!!QUACK!!!
================================================================================
{msg}
================================================================================
!!!QUACK!!!
""")
    sys.exit(1)

def convertToLower(charCode):
    """
    add 97 to character_code
    covert from ASCII code to letter
    return decoded letter
    """
    if charCode == '':
        return ""
    elif int(charCode) >= 0 and int(charCode) <= 25:
        num = int(charCode) + 97
        return chr(num)
    else:
        return ""

def convertToUpper(charCode):
    """
    add 65 to character_code
    covert from ASCII code to letter
    return/add letter to result string
    """
    if charCode == '':
        return ""
    elif int(charCode) >= 0 and int(charCode) <= 25:
        num = int(charCode) + 65
        return chr(num)
    else:
        return ""

def convertToSpecialChar(charCode):
    if charCode[0] == "A":
        if charCode[1:] == '':
            return ""
        elif int(charCode[1:]) >= 0 and int(charCode[1:]) <= 32:
            num = int(charCode[1:]) + 32
            return chr(num)
        else:
            return ""
    elif charCode[0] == "B":
        if charCode[1:] == '':
            return ""
        elif int(charCode[1:]) >= 0 and int(charCode[1:]) <= 5:
            num = int(charCode[1:]) + 91
            return chr(num)
        else:
            return ""
    elif charCode[0] == "C":
        if charCode[1:] == '':
            return ""
        elif int(charCode[1:]) >= 0 and int(charCode[1:]) <= 3:
            num = int(charCode[1:]) + 123
            return chr(num)
        else:
            return ""
    else:
        return ""


def getFile():
    """
    prompt the user for a file path
    check if path is valid
    if not
        print error message and exit
    else return the opened file
    """
    print(f"You are located at {os.getcwd()}")
    textFile = input("Please select a text file to parse: ")
    if os.access(textFile, os.R_OK):
        return open(textFile, 'r')
    sendError(f"Invalid file path")

def decryptLine(line):
    """
    find start of opened file
    get file as string
    split file into lines
    check each "word" for a first character of a DuckieCrypt flag (^, _, or +)
    if ^
        pass encryption into whatBigLetter()
    if _
        pass encryption into whatLittleLetter()
    if +
        pass encryption into whatChar()
    """
    output = ""
    test = line.split()                             # split line into "words"
    for i in test:                                  # check each word for a flag
        if i[0] == "^":                             # signifies uppercase, decode remaining charCode
            output = output + (convertToUpper(i[1:]))
        elif i[0] == "_":                           # signifies lowercase, decode remaining charCode
            output = output + convertToLower(i[1:])
        elif i[0] == "+":                           # signifies special char, decode remaining charCode
            output = output + convertToSpecialChar(i[1:])
    return output

if __name__ == '__main__':
    file = getFile()
    for line in file.readlines():
        print(decryptLine(line))
    file.close()