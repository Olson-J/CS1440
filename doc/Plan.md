# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

This program should summarize the contents of a large text file in a concise report. The program takes one argument (the name of a directory)and should be able to work from whatever working directory is provided. The names of the files to be summarized will be hardcoded into the program. A good solution will match the example summary provided and take under a minute to run. The program should handle the file one line at a time, checking the FIPS code to determine if the line should be included in the summary (only if FIPS code is from all 50 states, the District of Columbia, or territories of the US). The report must exclude areas on a given list ('statewide' areas, 'total', etc). The program will only store one line of the file in memory at any given time. If a line has an acceptable FIPS code, industry_code = 10 or 5112, and own_code = 0 or 5 then the line's data will be added to "all industries" or "software publishing industry" sections of the report, respectively.

I know how to:
- process files one line at a time
- look for certain character sequences in a line
- softcode directory handleing 

I don't know how to:
- use/make a dictionary

## Phase 1: System Analysis *(10%)*

Data used:
- gets one argument from the command line that specifies which directory the input files are in

output:
- in the form of the report, which was premade in report.py. the program will basically just fill out the report

algorithms needed:
- convert file into dictionary
- process file one line at a time (NOT read() or readlines())
- identify FIPS codes, determine whether or not to keep line for final report
- create and keep track of kept FIPS in a dictionary 
- determine if line should go in the 'all industries' portion or the software publishing industry portion

## Phase 2: Design *(30%)*

```python
def areaTitles(sys.argv[1]):
    """
    go to the repository's top directory
    open [given directory]/area.titles.csv
    bad input: open will call an error
    good input:
    discard first line
    split line into 2 fields(splits into code and area, even if the area has a comma in it)
    if ok, collect into a dictionary mapping codes to area titles
    return dictionary
    """
    file = open(f'{sys.argv[1]}/area_titles.csv')
    file.readline()
    area_list = {}
    for line in file:
        check = line.rstrip().split(',', 1)         # i think this will only split it once? on the first comma?
        if (check[0].isnumeric()) && not(check[0].endswith("000")):
            area_list[ check[0] ] = check[1]        # puts code and area into dictionary
    return area_list
```

```python
def industries(file, area_list):
    """
    go to the repository's top directory
    open [given directory]/area.titles.csv
    bad input: open will call an error
    good input:
    process line by line
    find lines with ok FIPS (strings not ints)
    check if ok industry
    check if ok ownership code
    if all ok add info to the correct field
    also add 1 to num_areas
    repeat last 3 lines for software industry
    """
    file = open(f'{sys.argv[1]}/2020.annual.singlefile.csv')
    for line in file:
        check = line.rstrip().split(',')
        if (check[0] in area_list) && (check[0].isnumeric()) && not(check[0].endswith("000")):
            add 1 to rpt.all.num_areas
            # all industry section
            if check[1] = "0": #own_code
                if check[2] = "10": # industry_code
                    add int(check[15]) to rpt.all.total_annual_wages
                    if int(check[15]) > rpt.all.max_annual_wage[1]:
                        rpt.all.max_annual_wage[0] = area_list[check[0]]    # marks where the wage is from as well as what it was
                        rpt.all.max_annual_wage[1] = int(check[15])
                    add int(check[13]) to rpt.all.total_estab
                    if int(check[13]) > rpt.all.max_estab[1]:
                        rpt.all.max_estab[0] = area_list[check[0]]
                        rpt.all.max_estab[1] = int(check[13])
                    add int(check[14]) to rpt.all.total_empl
                    if int(check[14)] > rpt.all.max_empl[1]:
                        rpt.all.max_empl[0] = area_list[check[0]]
                        rpt.all.max_empl[1] = int(check[14])
            # for software
            if check[1] = "5": #own_code
                if check[2] = "5112":   #industry_code
                    add int(check[15]) to rpt.soft.total_annual_wages
                    if int(check[15]) > rpt.soft.max_annual_wage[1]:
                        rpt.soft.max_annual_wage[0] = area_list[check[0]]
                        rpt.soft.max_annual_wage[1] = int(check[15])
                    add int(check[13]) to rpt.soft.total_estab
                    if int(check[13]) > rpt.soft.max_estab[1]:
                        rpt.soft.max_estab[0] = area_list[check[0]]
                        rpt.soft.max_estab[1] = int(check[13])
                    add int(check[14]) to rpt.soft.total_empl
                    if int(check[14]) > rpt.soft.max_empl:
                        rpt.soft.max_empl[0] = area_list[check[0]]
                        rpt.soft.max_empl[1] = int(check[14])
```

## Phase 3: Implementation *(15%)*

- moved contents of areaTitles and industries to main, having it in a seperate function didn't really turn out to be beneficial or make sense
- did some minor edits for formatting and translating
- added a close file statement I somehow forgot
- commented out filler data in report section; I used rpt to store info instead of using extra variables, so I don't need to reassign the rpt field values

## Phase 4: Testing & Debugging *(30%)*

**test: python src/bigData.py data/CT_combined**
- printed the report with all sections being 0; used print statements to figure out that my conditional loop wasn't actually being entered, more print statements showed that my dictionary of FIPS codes and areas was not actually being written to and was completely empty.
- my dictionary creating code was saying that none of the FIPS code strings were numeric ; I think it was creating strings of strings? ('"48640"' instead of '48640'). The " were included in the string itself, so I removed them before splitting the file line. Area_list was no longer empty
- 2020 file was still not recognizing the file contents in the area_list and was not filling out the report properly ; same problem with ", removed
- report now has the correct number of areas, but no other fields are filled out ; each field of the file has the " problem. removed
- error when trying to add field to total_wages, was trying to add an empty string; I forgot to account for fields 9-13 being removed from the singlefiles, I was trying to access the wrong field
- was printing a newline after the place name ; not sure why. I added .strip() everywhere I thought it could help, somehow I managed to get rid of one newline in the max_wages section of the report but not any of the others. I don't know how that happened, each section's code is almost identical so idk what's going on
- was not printing anything for the software fields ; I had messed up the files, and CT_combined was a copy of CT_all_industries so there was no data for the software fields. Remade the file correctly
- was miscounting the number of FIPS areas ; moved the counting statements farther into the loops for all_industries, realized I forgot to add a count statement for the software industry so I added one

**test: python src/bigData.py data/CT_reversed**
- wasn't giving any output for software sections again ; messed up the file again, recreated it and it works now

**test: python src/bigData.py data/DC_all_industries**
- somehow undid the one section of report that I had fixed the extra newline in, all sections have the extra newline again ; idk man I can't figure out where the newline is coming from

all other files got the correct numbers in the report, but all had an issue with the extra newlines. UPDATE: the change to report.py fixed it and the report is formatted correctly now

## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance

    *   What parts of your program are sloppily written and hard to understand?
    the part of my code that processes the 2020 file is pretty dense looking and repetitive, but I'm not entirely sure how to thin it out and honestly I'm pretty happy that it works, so I don't really want to mess with it
        *   Are there parts of your program which you aren't quite sure how/why they work?
        no, once I figured out how to make the dictionary and use rpt it was pretty straightforward
        *   If a bug is reported in a few months, how long would it take you to find the cause?
        maybe half an hour max? with the report formatted the way it is it's pretty easy to tell where things go wrong, and then theres only a few lines of code per section
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        yes? I hope so 
        *   ...yourself in six month's time?
        yes
    *   How easy will it be to add a new feature to this program in a year?
    pretty easy, again the formatting breaks up the program into nice chunks
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        I think so
        *   ...the operating system?
        It should?
        *   ...to the next version of Python?
        It should unless the formatting for dictionaries or .rstrip() changes
*   Fill out the Assignment Reflection on Canvas.
