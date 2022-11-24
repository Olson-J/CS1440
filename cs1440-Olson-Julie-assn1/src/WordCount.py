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

def wc(args):
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
    if len(args) < 1:                                                       # makes sure at least 1 file is given
        usage('Must provide at least 1 filename')
    i = 0
    while i < len(args):                                                    # repeats for each filename given
        file = open(args[i], 'r')                                           # opens file for reading, error if invalid
        strFile = file.read()
        lineCount = len(strFile.split('\n')) - 1                            # counts newlines, not counting the eof
        wordCount = len(strFile.split())                                    # splits file by whitespace
        charCount = len(strFile)                                            # counts chars in file
        print('{:>8d}{:>8d}{:>8d}  {:<4s}'.format(lineCount, wordCount, charCount, args[i]))
        file.close()
        i += 1
