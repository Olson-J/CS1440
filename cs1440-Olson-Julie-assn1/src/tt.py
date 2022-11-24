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
import os
import sys

from Concatenate import cat, tac                                    	         	  
from CutPaste import cut, paste                                     	         	  
from Grep import grep                                               	         	  
from Partial import head, tail                                      	         	  
from Sorting import sort                                            	         	  
from WordCount import wc                                            	         	  
from Usage import usage                                             	         	  

"""
    check that at least 2 arguments have been given
    if less than 2 exit and call usage() for error message
    else check which tool was called and forward remaining arguments
    if not a valid tool name, call usage
"""
if len(sys.argv) < 2:
    usage()
else:
    args = sys.argv[2:]
    if sys.argv[1] == "cat":
        cat(args)
    elif sys.argv[1] == "tac":
        tac(args)
    elif sys.argv[1] == "cut":
        cut(args)
    elif sys.argv[1] == "paste":
        paste(args)
    elif sys.argv[1] == "grep":
        grep(args)
    elif sys.argv[1] == "head":
        head(args)
    elif sys.argv[1] == "tail":
        tail(args)
    elif sys.argv[1] == "sort":
        sort(args)
    elif sys.argv[1] == "wc":
        wc(args)
    else:
        usage('Invalid tool name')
