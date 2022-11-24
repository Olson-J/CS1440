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
    match = []                                                              # create empty lists
    noMatch = []
    if len(args) < 2:                                                       # makes sure at least 1 file and a pattern is given
        usage('Please provide a pattern and at least one filename')
        if args[0] == "-v":                                                 # if -v arg was used then the next argument is the pattern
            for i in args[2:]:                                              # for each file listed
                file = open(args[i], 'r')                                   # open
                for line in file.readlines():                               # split into lines and search for pattern
                    if args[1] in line:                                     # sort into lists
                        match.append(line)
                    else:
                        noMatch.append(line)
                file.close()                                                # close file
                for j in noMatch:                                           # print list
                    print(noMatch[j])
    else:
        for i in args[1:]:                                                  # first arg is pattern, repeat for each file listed
            file = open(args[i], 'r')                                       # open
            for line in file.readlines():                                   # split into lines and search for pattern
                if args[0] in line:
                    match.append(line)                                      # sort into lists
                else:
                    noMatch.append(line)
            file.close()                                                    # close file
            for j in match:                                                 # print list
                print(match[j])
