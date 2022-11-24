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


def cut(args):
    """
    NOTE: this is no longer at all what the code looks like sorry
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
                        print(newline)
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
                    print(newline)
                else:
                    print(first field)
            close file
            """

    if len(args) < 1:  # makes sure at least 1 file is given
        usage('Too few arguments')
    masterList = []
    count = 0
    if args[0] == "-f":
        if len(args) < 2:  # makes sure at least 1 file is given
            usage('Too few arguments')
        field = args[1].split(",")  # now a list
        field = sorted(field)

        i = 0
        x = 2
        while i < len(args[2:]):    #for each file
            listCount = 0
            file = open(args[x], 'r')
            for line in file.readlines():  # split into lines, repeat for each line

                masterList.append(line.split(","))
                listCount += 1
            if count < listCount:  # will keep track of the longest file length
                count = listCount
            file.close()
            i += 1
            x += 1

        for i in range(len(masterList)):  # for each element of the list
            diff = count - len(masterList[i])  # find how much longer the longest is
            for j in range(diff):  # add empty elements to match length of longest
                masterList[i].extend('\n')
        j = 0
        c = 0
        while j < len(masterList[c]) + 1:  # these will loop through each filelist at the same
            for i in range(len(masterList)):  # position to create the individual output lines
                if j < len(masterList[i]):
                    if str(j+1) in field:      # if one of the fields, print nothing [+1 because fields dont start at 0]
                        print(masterList[i][j].strip(), end="")
                        print("")  # newline at the end of each output line
                c = i
            j += 1

    else:
        i = 0
        while i < len(args):  # for each file
            listCount = 0
            file = open(args[i], 'r')

            for line in file.readlines():  # split into lines, repeat for each line
                masterList.append(line.split(","))
                listCount += 1
            if count < listCount:  # will keep track of the longest file length
                count = listCount
            file.close()
            i += 1

        for i in range(len(masterList)):  # for each element of the list
            diff = count - len(masterList[i])  # find how much longer the longest is
            for j in range(diff):  # add empty elements to match length of longest
                masterList[i].extend('\n')

        j = 0
        while j < 1:  # these will loop through each filelist at the same
            for i in range(len(masterList) - 1):  # position to create the individual output lines
                print(masterList[i][j].strip(','), end="")
                if not i == len(masterList) - 2:
                    print("")  # newline at the end of each output line
            j += 1




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
    if len(args) < 1:                                           # makes sure at least 1 file is given
        usage('Too few arguments')
    oneListToRuleThemAll = []
    count = 0
    i = 0
    while i < len(args):
        listCount = 0                                           # will keep track of how many lines are in each file
        file = open(args[i], 'r')                               # open file
        babyList = []
        for line in file.readlines():                           # split into lines, repeat for each line
            babyList.append(line)                               # adds lines to a list
            listCount += 1
        oneListToRuleThemAll.append(babyList)                   # creates a 2D array of the file lists
        if count < listCount:                                   # will keep track of the longest file length
            count = listCount
        file.close()
        i += 1

    for i in range(len(oneListToRuleThemAll)):                  # for each element of the list
        diff = count - len(oneListToRuleThemAll[i])             # find how much longer the longest is
        for j in range(diff):                                   # add empty elements to match length of longest
            oneListToRuleThemAll[i].extend('\n')

    j = 0
    c = 0
    while j < len(oneListToRuleThemAll[c]) + 1:                 # these will loop through each filelist at the same
        for i in range(len(oneListToRuleThemAll)):              # position to create the individual output lines
            if j < len(oneListToRuleThemAll[i]):
                if oneListToRuleThemAll[i][j] == '\n':          # if a field is 'empty'/ a filler it prints a comma
                    if i == len(args) - 1:                      # if this field is at the end of the output file
                        print("", end="")                       # don't print a comma
                    else:
                        print(",", end="")                      # else print placeholder comma
                else:
                    if i == len(args) - 1:                      # if the field is at the end of the output line no comma
                        print(oneListToRuleThemAll[i][j].strip(), end="")
                    else:                                       # else print comma to separate
                        print(oneListToRuleThemAll[i][j].strip(), end=",")
            c = i
        print("")                                               # newline at the end of each output line
        j += 1
