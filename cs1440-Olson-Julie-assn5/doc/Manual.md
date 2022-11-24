# Recursive Web Crawler User Manual

This program requires several python libraries. If they are not already installed on your computer, use the pip install command to install the following libraries:
beautifulsoup
requests

This program also requires the user to provide an absolute URL, as opposed to a relative URL. Absolute URLs include a scheme, such as http or https, followed by :// and a hostname, such as duckduckgo.com. If the provided URL is missing either or both of these parts (known as a relative URL), it will not be accepted and an error message will appear.

To properly run the program the user must provide an absolute URL, and has the option of specifying how many 'levels' deep they wish the crawler to go. If no level is specified, or if a negative number is provided the program will default to 3.

Output will consist of a list of the visited links being printed to the screen, with indentation marking what 'level' each link was found on. If a page is unreachable an error message will be printed to inform you, but the program should not crash or stop because of them. When the crawler has run its course a statement will be printed informing you of the program's statistics such as pages visited and running time. 

If you wish to end the program before the crawler has finished running, you may hit ctrl-c to stop the crawler. On occasion it might be necessary to hit the key combination a few times before it takes effect, but once it does the program will print the statistics message and quit.

Examples of accepted input:

```https://cs.usu.edu 0```
```http://unnovative.net/level0.html```

Invalid input examples:
```cs.usu.edu```
```level10.html```
