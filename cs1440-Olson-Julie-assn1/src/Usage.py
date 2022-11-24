# Usage instructions and descriptions for each tool                 	         	  
#                                                                   	         	  
# DO NOT EDIT THIS FILE                                             	         	  

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



CAT = """tt.py cat|tac FILENAME...                                  	         	  
    Concatenate and print files in order or in reverse"""           	         	  


CUT = """tt.py cut [-f LIST] FILENAME...                            	         	  
    Remove comma-separated sections from each line of files         	         	  
    -f  List of comma-separated integers indicating fields to output (default is LIST=1)"""


PASTE = """tt.py paste FILENAME...                                  	         	  
    Merge lines of files into one comma-separated text"""           	         	  


GREP = """tt.py grep [-v] PATTERN FILENAME...                       	         	  
    Print lines of files matching PATTERN                           	         	  
    -v  Invert matching; print lines which DO NOT match PATTERN"""  	         	  


HEAD = """tt.py head|tail [-n N] FILENAME...                        	         	  
    Output the first or last part of files                          	         	  
    -n  Number of lines to print (default is N=10)"""               	         	  


SORT = """tt.py sort FILENAME...                                    	         	  
    Output lines of text file in sorted order"""                    	         	  


WC = """tt.py wc FILENAME...                                        	         	  
    Print newline, word, and byte counts for each file"""           	         	  


def usage(error=None, tool=None):                                   	         	  
    """Provide a unified error reporting interface"""               	         	  
    # Print a specific error message, if requested                  	         	  
    if error is not None:                                           	         	  
        print(f"Error: {error}\n")                                  	         	  

    # Print a tool-specific message where possible; otherwise, display        	  
    # instructions for all tools                                    	         	  
    if tool == 'cat' or tool == 'tac':                              	         	  
        print(f"\t{CAT}")                                           	         	  
    elif tool == 'cut':                                             	         	  
        print(f"\t{CUT}")                                           	         	  
    elif tool == 'paste':                                           	         	  
        print(f"\t{PASTE}")                                         	         	  
    elif tool == 'grep':                                            	         	  
        print(f"\t{GREP}")                                          	         	  
    elif tool == 'head' or tool == 'tail':                          	         	  
        print(f"\t{HEAD}")                                          	         	  
    elif tool == 'sort':                                            	         	  
        print(f"\t{SORT}")                                          	         	  
    elif tool == 'wc':                                              	         	  
        print(f"\t{WC}")                                            	         	  
    else:                                                           	         	  
        print(f"""Python Text Tools Usage:                          	         	  
========================                                            	         	  

{CAT}                                                               	         	  

{CUT}                                                               	         	  

{PASTE}                                                             	         	  

{GREP}                                                              	         	  

{HEAD}                                                              	         	  

{SORT}                                                              	         	  

{WC}""")                                                            	         	  

    # Quit the program                                              	         	  
    exit(1)                                                         	         	  