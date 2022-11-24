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

import time                                                         	         	  
import sys                                                          	         	  
from Report import Report                                           	         	  


rpt = Report(year=2020)

if __name__ == '__main__':
    if len(sys.argv) < 2:           # error message if no directory given
        print("Error: must provide directory")
        exit(1)

    print("Reading the databases...", file=sys.stderr)
    rpt.all.num_areas = 0
    before = time.time()                                            	         	  

    file = open(f'{sys.argv[1]}/area_titles.csv')
    file.readline()     # skip first line
    area_list = {}
    for line in file:
        line = line.replace('"', '')    # get rid of quotes
        onecheck = line.strip().split(',', 1)   # pls get rid of newlines and split on first comma

        if onecheck[0].isnumeric():     # no letters
            if not (onecheck[0].endswith("000")):      # can't end in 000
                area_list[onecheck[0]] = onecheck[1].strip()  # make dictionary
    file.close()

    singlefile = open(f'{sys.argv[1]}/2020.annual.singlefile.csv')
    for line in singlefile:
        check = line.rstrip().replace('"', '').split(',')    # strip line and split on comma
        if check[0] in area_list:
            if not check[0].endswith("000"):
                # all industry section
                if check[1] == "0":        # own_code
                    if check[2] == "10":   # industry_code
                        rpt.all.num_areas += 1              # track all valid areas
                        rpt.all.total_annual_wages += int(check[10])   # add to total wages

                        if int(check[10]) > rpt.all.max_annual_wage[1]:     # if line's wage is larger than max
                            rpt.all.max_annual_wage[0] = area_list[check[0]].strip()   # track place
                            rpt.all.max_annual_wage[1] = int(check[10])     # and wage

                        rpt.all.total_estab += int(check[8])    # add to total estab
                        if int(check[8]) > rpt.all.max_estab[1]:    # if line's num is larger than max
                            rpt.all.max_estab[0] = area_list[check[0]].strip()     # track place
                            rpt.all.max_estab[1] = int(check[8])        # and num

                        rpt.all.total_empl += int(check[9])     # add to total empl
                        if int(check[9]) > rpt.all.max_empl[1]:     # if line's empl is larger than max
                            rpt.all.max_empl[0] = area_list[check[0]].strip()      # track place
                            rpt.all.max_empl[1] = int(check[9])     # and num
                # for software
                if check[1] == "5":  # own_code
                    if check[2] == "5112":  # industry_code
                        rpt.soft.num_areas += 1     # add to total areas
                        rpt.soft.total_annual_wages += int(check[10])  # add to total wages

                        if int(check[10]) > rpt.soft.max_annual_wage[1]:    # if line's wage is larger than max
                            rpt.soft.max_annual_wage[0] = area_list[check[0]].strip()  # track place
                            rpt.soft.max_annual_wage[1] = int(check[10])        # and amount

                        rpt.soft.total_estab += int(check[8])       # add to total estab
                        if int(check[8]) > rpt.soft.max_estab[1]:   # if line's estab is larger than max
                            rpt.soft.max_estab[0] = area_list[check[0]].strip()    # track place
                            rpt.soft.max_estab[1] = int(check[8])       # and num

                        rpt.soft.total_empl += int(check[9])        # add to total empl
                        if int(check[9]) > rpt.soft.max_empl[1]:    # if line's empl is larger than max
                            rpt.soft.max_empl[0] = area_list[check[0]].strip()     # track place
                            rpt.soft.max_empl[1] = int(check[9])        # and num
    singlefile.close()

    after = time.time()                                             	         	  
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

    # Print the completed report                                    	         	  
    print(rpt)
