#!/usr/bin/python3  	         	  

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

import requests  	         	  
from bs4 import BeautifulSoup  	         	  
from urllib.parse import urlparse, urljoin
import sys  	         	  
import time  	         	  


def crawl(url, maxDepth, depth, visited):
    """  	         	  
    Given an absolute URL, print each hyperlink found within the document.  	         	  

    Your task is to make this into a recursive function that follows hyperlinks  	         	  
    until one of two base cases are reached:  	         	  

    0) No new, unvisited links are found  	         	  
    1) The maximum depth of recursion is reached  	         	  
    """
    # check if ok to continue
    if depth > int(maxDepth):
        return
    if url in visited:
        return
    parsed = urlparse(url)
    if not parsed.scheme.startswith('http'):
        return

    # print formatting for links
    indent = ''
    for i in range(depth):
        indent += "    "
    print(indent, end='')
    print(url)
    visited.add(url)

    # visit the link
    try:
        response = requests.get(url)
        if not response.ok:
            print(f"crawl({url}): {response.status_code} {response.reason}")
            return
    # print stats if ended early
    except KeyboardInterrupt:
        print("except KeyboardInterrupt")
        after = time.time()
        num = len(visited) - 1
        plural = 's' if num > 1 else ''
        timeSpent = after - before

        print(f"Visited {num} unique page{plural} in {timeSpent} seconds")
        exit(0)
    # print what went wrong
    except Exception as e:
        print(f"Failed to get {url} because {e}")
        return

    # look for more links
    html = BeautifulSoup(response.text, 'html.parser')
    links = html.find_all('a')
    for a in links:
        link = a.get('href')
        if link:
            # Create an absolute address from a (possibly) relative URL
            absoluteURL = urljoin(url, link)

            # Only deal with resources accessible over HTTP or HTTPS
            if absoluteURL.startswith('http'):
                part = absoluteURL.split("#")
                NewUrl = part[0]
                crawl(NewUrl, maxDepth, depth + 1, visited)


# If the crawler.py module is loaded as the main module, allow our `crawl` function to be used as a command line tool
if __name__ == "__main__":
    # If no arguments are given...
    if len(sys.argv) < 2:
        print("Error: no URL supplied", file=sys.stderr)
        exit(0)
    else:
        url = sys.argv[1]

    # check link is absolute
    parsed = urlparse(url)
    if parsed.scheme.startswith('http'):
        if parsed.netloc:
            pass
    else:
        print("Error: Not a absolute URL", file=sys.stderr)
        exit(0)

    # check for maxDepth
    if len(sys.argv) > 2:
        maxDepth = sys.argv[2]
    else:
        maxDepth = 3

    plural = 's' if maxDepth != 1 else ''
    print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")

    # start crawl
    before = time.time()
    visited = {""}
    try:
        crawl(url, maxDepth, 0, visited)
    except KeyboardInterrupt:
        print("Exception KeyboardInterrupt")

    # print stats when done
    after = time.time()
    num = len(visited) - 1
    plural = 's' if num > 1 else ''
    timeSpent = after - before

    print(f"Visited {num} unique page{plural} in {timeSpent} seconds")
