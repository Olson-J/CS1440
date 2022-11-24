# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

If given no arguments on the command line, the program will print a message explaining how to use the program, and quit.This program will take in a absolute http url from the user to use as a starting point. The URL will be tested to ensure it is valid, and an error message will be printed if not. The program can also be given a maximum depth, which must be a positive integer and defaults to 3. Once the starting URL and depth are processed the program will crawl and print all the links found until the maximum depth is reached. While running, the program can be quit by hitting ctrl+c, which will raise an exception and result in the program ending and printing a notice of the early termination. Whether ended early or allowed to run its course, the program will print runtime statistics before closing, which will include how long the program ran for and how many links were visited. Program must be able to handle errors and unreachable content without crashing, and will print user friendly messages explaining what happened.

I know how to:
- write recursive functions

potential challenges: 
- proper error handling
- how to make the program visit links

## Phase 1: System Analysis *(10%)*

inputs:
- maximum depth integer; must be positive. If not provided/negative will default to 3
- starting URL; must be http(s) absolute, will need to be tested before use to make sure it is valid

outputs:
- explanation message if given no inputs
- error message (and quit) if given an invalid starting URL
- a printed list of links the crawler finds/visits
- runtime statistics report

algorithms needed:
- crawl
    - will be recursive
    - allow the user to quit with ctrl+c, and print message/quit accordingly after printing statistics
    - will take a URL, depth int, maxdepth int, and visited set as parameters
    - if program has reached maxdepth, URL has already been visited, or invalid URL; return from crawl
    - print URL with proper indentation, mark URL as visited, fetch webpage/print exceptions as needed, scan for anchor tags, process URL data from tags, call crawl again with new parameters

- exception handling
    - print human friendly message about problem, then continue running unless user hit ctrl+c

- statistics
    - keep track of how long the program took to run
    - count how many links were visited
    - print to stderr

## Phase 2: Design *(30%)*

```python
def main():
    """
    check for number of arguments given
    if 0, print message and exit
    if 1 or 2, check URL and call crawl
    print report when done
    """
    visited = {}
    before = sys.time()
    if len(sys.argv) < 2:
        print("Error: no URL supplied")
        sys.exit(1)
    elif len(sys.argv) < 3 or sys.argv[2] < 0:
        if checkURL(sys.argv[1]):
            crawl(sys.argv[1], 3, 0, visited)
    elif len(sys.argv) = 3:
        if checkURL(sys.argv[1]):
            crawl(sys.argv[1], sys.argv[2], 0, visited)
    
    after = sys.time()
    time = after - before
    if len(visited) > 1:
        print("Visited " + len(visited) + " unique pages in " + time + " seconds", file=sys.stderr)
    else:
        print("Visited 1 unique page in " + time + " seconds", file=sys.sterr)

```
```python
def checkURL(url, old):
    """
    parse url
    check if absolute URL and http(s), if not print error message
    """
    parsed = urlparse(url)
    if parsed.scheme = 'http' or parsed.scheme = 'https':
        if parsed.location:
            absolute, yay
    else:
        not absolute :(



```
```python
def crawl(url, maxDepth, depth, visited):
    """
    check depth and return if needed
    determine indent and print URL
    mark URL as visited, then visit it
    handle exceptions
    """
    try:
        if (depth > maxDepth):
            return

        indent = ''
        for i in depth:
            indent.append("    ")
        print(indent + url)
        visited.add(url)
    except KeyboardInterrupt:
        print("except KeyboardInterrupt")
        return
    except Exception as e:
        print(f"Failed to get {url} because {e}")
        return
```

## Phase 3: Implementation *(15%)*

**Deliver:**

*   (More or less) working code.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.


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

**Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   Fill out the Assignment Reflection on Canvas.
