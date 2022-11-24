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
from Usage import usage


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
    if len(args) < 1:                                       # makes sure at least 1 file is given
        usage('Too few arguments')
    if args[0] == "-n":
        if len(args) < 2:                                   # makes sure at least 1 file is given
            usage('Too few arguments')
        n = args[1]
        if not n.isdigit():
            Usage('Number of lines required')
        n = int(n)
        count = 1
        for i in args[2:]:                                  # repeats for each filename given
            count += 1
            if len(args[2:]) > 1:                           # banner if multiple files
                print("==> " + args[count] + " <==")
            file = open(args[count], 'r')                   # opens file for reading, error if invalid
            fileLines = file.readlines()                    # splits file into lines
            j = 0
            while j < n:                                    # prints n lines
                print(fileLines[j].strip())
                j += 1
            file.close()

    else:
        i = 0
        while i < len(args):                                # repeats for each filename given
            if len(args) > 1:                               # banner if multiple files
                print("==> " + args[i] + " <==")
            file = open(args[i], 'r')                       # opens file for reading, error if invalid
            fileLines = file.readlines()                    # splits file into lines
            length = len(fileLines)
            j = 0
            if length > 10:                                 # if file is longer than 10 lines just print 10
                while j < 10:                               # prints 10 lines
                    print(fileLines[j].strip())
                    j += 1
            else:
                while j < length:                           # if shorter just print all lines
                    print(fileLines[j].strip())
                    j += 1
            file.close()
            i += 1


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
    if len(args) < 1:                                       # makes sure at least 1 file is given
        usage('Too few arguments')
    if args[0] == "-n":
        if len(args) < 2:                                   # makes sure at least 1 file is given
            usage('Too few arguments')
        n = args[1]
        if not n.isdigit():                                 # error if invalid number
            Usage('Number of lines required')
        n = int(n)
        count = 2
        for i in args[2:]:                                  # repeats for each filename given
            if len(args[2:]) > 1:                           # banner if multiple files
                print("==> " + args[count] + " <==")
            file = open(args[count], 'r')                   # opens file for reading, error if invalid
            fileLines = file.readlines()                    # splits file into lines
            revFile = reversed(fileLines)                   # reverses the order of the lines
            j = 0
            for line in revFile:                            # prints n lines
                if j < n:
                    print(line.strip())
                    j += 1
            file.close()
            count += 1
    else:
        count = 0
        for i in args:                                      # repeats for each filename given
            if len(args) > 1:                               # banner if multiple files
                print("==> " + args[count] + " <==")
            file = open(args[count], 'r')                   # opens file for reading, error if invalid
            fileLines = file.readlines()                    # splits file into lines
            revFile = reversed(fileLines)                   # reverses the order of the lines
            length = len(fileLines)                         # finds number of lines in file
            j = 0
            if length > 10:                                 # if file is longer than 10 lines just print 10
                for line in revFile:
                    if j < 10:
                        print(line.strip())
                        j += 1
            else:
                for line in revFile:                        # if shorter than 10 just print all lines
                    if j < length:
                        print(line.strip())
                        j += 1
            file.close()
            count += 1
