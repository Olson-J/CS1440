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

def cat(args):
    """
       make sure there is at least 1 filename given
       if not call usage and exit
       open files and make sure they are accessible, if not open() will raise an error
       print entire file line by line
       if more than one file, print '...' divider and repeat until done
       close file
       """
    if len(args) < 1:                                       # makes sure at least 1 file is given
        usage('Must provide at least 1 filename')
    i = 0
    while i < len(args):                                          # repeats for each filename given
        file = open(args[i], 'r')                           # opens file for reading, error if invalid
        for line in file.readlines():                       # splits file into lines
            print(line.strip())                                     # prints each line
        file.close()                                        # closes file
        i += 1


def tac(args):                                                      	         	  
    """
    make sure there is at least 1 filename given
    if not call usage and exit
    open files 
    if more than one file, print '...' divider and repeat until done
    print entire file line by line, backwards
    close file
    """
    if len(args) < 1:                                       # makes sure at least 1 file is given
        usage('Must provide at least 1 filename')
    i = 0
    while i < len(args):                                          # repeats for each filename given
        file = open(args[i], 'r')                           # open file
        fileLines = file.readlines()
        revFile = reversed(fileLines)
        for line in revFile:
            print(line.strip())
        file.close()                                        # closes file
        i += 1
