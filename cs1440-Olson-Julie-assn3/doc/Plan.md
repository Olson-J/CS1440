# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

This program creates and maipulates a deck of Bingo cards. Users will choose 
how many cards they wish to create (any number from 2 to 8192, inclusive) and
how big they want the cards to be (up to 16x16). All cards will be filled with 
values that increase column-wise from left to right, and odd sized cards will 
have a FREE spot in the center. Once the deck of cards has been created, the user
will be given the option to print a specific card, print all the cards, save the 
deck to a file, or exit the program. 

Ideally the program should provide the user with an easy-to-read menu that lists 
the possible courses of action. If an invalid command is given the menu will 
repeat itself until given a valid command. Any time the user is asked to provide
a number the acceptible range should be shown, and the input should be validated.
If the input is not in a valid form, the program should print a help message 
reminding the user what kind of input is expected and reprompt the user.

potential problems:
- I am not entirely sure if I did the source code UML properly
- formatting the cards correctly might be difficult
- the way the menu gets created and filled out seems a bit odd, I'm not sure if I totally understand it yet
- I dont know how to save the deck to a text file



## Phase 1: System Analysis *(10%)*

input:
- asks the user for input such as deck and card size, and directions for what to do with the created cards
- if the deck is to be saved to a file, asks for file

output:
- print 1+ cards to the screen or save the deck to a file. Cards will be printed with the card id in the line before the card itself

algorithms needed:
- create deck based on given deck size
- create and fill cards based on the given card size, including a free space if given an odd number. Numbers on the card should increase from left to right
- generate a list of non-repeating random numbers, and sort them so they can fill the card appropriately
- print specified card with the correct formatting, including id number if the whole deck is printed
- save the deck to a text file

## Phase 2: Design *(30%)*

---------------------------- UI class ----------------------------
```python
def __get_str(prompt):
    """
    return a string given by the user in response to a prompt
    repeat prompt until non empty string is given
    """
    while True:
        string = input(prompt)
        if string != "":
            return string
```

```python
def __get_int(prompt, lo, hi):
    """
    return an int given by the user in response to a prompt
    check that input is within the range of lo and high
    reprompt if not
    """
    while True:
        string = input(prompt)
        if string.isnumeric():
            if (string > lo) and (string < hi):
                return string
        else:
            print("Please input a number in the range [" + lo + " - " + hi + "]\n")
```
```python
def __create_deck():
    """
    returns none
    asks user for info regarding the deck and cards
    creates a new deck and stores it in self.__m_currentDeck
    """
    card_size = self.__get_int("Enter a card size [3-16]:", 3, 16)
    max_num = self.__get_int("Enter max number [50 - 97]:", 50, 97)
    num_cards = self.__get_int("Enter a number of cards [2 - 8192]:", 2, 8192)
    self.__m_currentDeck = Deck(card_size, num_cards, max_num)
```
```python
def __print_card():
    """
    returns none
    prompt user for card id, reprompt if input is invalid
    print card id
    print specified card from the deck
    """
    cardID = self.__get_int("ID of card to print [1 - " 
            + len(self.__m_currentDeck) + "]:", 1,
            len(self.__m_currentDeck))
    print("Card #" + cardID)
    print(self.__m_currentDeck.card(cardID))
```
```python
def __save_deck(prompt):
    """
    return none
    get name of file from user
    open file
    save deck to file
    close file
    """
    filename = self.__get_str("Enter output file name:")
    f = open(filename, "w")
    f.write(self.__m_currentDeck)
    f.close()
```
---------------------------- Deck class ----------------------------

```python
def Deck(card_size, num_cards, max_num):
    """
    deck constructor
    save arguments to use elsewhere
    for each card in the deck
        create a non-repeating list of random numbers (less than max_num)
        shuffle numbers within their segments
        pass deck position (ID) and sorted number set to Card
        save the formatted card string to the deck
    """
    self.num_cards = num_cards
    self.card_size = card_size
    self.max_num = max_num
    for i in range(1, num_cards + 1):
        numbers = RandNumberSet(card_size, max_num)
        numbers.shuffle
        intCard = Card(i, numbers)
        deck[i] = str(intCard)
```

```python
def __len__():
    """
    return the number of cards in deck 
    """
    return self.num_cards
```
```python
def card(n):
    """
    retrieve card n from deck
    """
    return deck[n]
```
```python
def __str__():
    """
    return String of the entire deck
    """
    deckString = ''
    for i in range(1, self.num_cards + 1):
        deckString.append(Deck.card(i))
    return deckString
```
---------------------------- Card class ----------------------------
```python
def Card(idnum, ns):
    """
    initialize a bingo card
    """
    self.idnum = idnum
    self.ns = ns
```
```python
def id():
    """
    returns the id num of the card
    """
    return self.idnum
```
```python
def number_at(row, col):
    """
    returns an int, from the card at row, col
    """
    row = getitem(self.ns)
    return row[col]
```
```python
def __len__():
    """
    return an int; the length of one side of the card
    """
    return len(RandNumberSet)

```
```python
def __str__():
    """
    return a nicely formatted bingo card as a string
    first include card id, BINGO letters, and first divider line
    then add the numbers with the correct formatting, alternating with dividing lines
    """
    cardString = ''
    cardString.append("Card #" + self.idnum + "\n")
    for letter in range(len(RandNumberSet)):
        cardString.append("   ")
        cardString.append(Card.COLUMN_NAMES[letter])
        cardString.append("  ")
    cardString.append("\n+")
    for chunk in range(len(RandNumberSet)):     # dividing lines
        cardString.append("-----+")
    
    for row in range ((len(RandNumberSet) * 2)): #accounts for dividers
        cardString.append("\n|")
        nums = self.ns.next_row()
        for chunk in range(len(RandNumberSet)):
            if not nums == None:
                if (nums[chunk] % 10) >= 1:     # finds number of digits
                    cardString.append(" ")
                else:
                    cardString.append("  ")
                cardString.append(nums[chunk])
                cardString.append("  |")
        cardString.append("\n+")
        for chunk in range(len(RandNumberSet)):     # dividing lines
            cardString.append("-----+")
    
```
-------------------------- RandNumberSet class --------------------------
```python
def RandNumberSet(nSize, nMax): #mostly provided but I added in a check to prevent repeating numbers
    """  	         	  
        Create a RandNumberSet  	         	  

        'nSize': a parameter restricted to be in the range [3..16]
        'nMax': a parameter restricted to be no less than `nSize*nSize`

        Numbers are kept in separate segments so that the numbers within
        columns on the resulting Bingo! card increase from left to right.

        Within a column numbers are unordered.  	         	  
        A newly initialized RandNumberSet may present its numbers in
        order.  Use .shuffle() to mix it up.  	         	  
        """  	         	  
        # sanity check on __m_nSize  	         	  
        self.__m_nSize = nSize  	         	  
        if self.__m_nSize < RandNumberSet.MIN_SIZE:  	         	  
            self.__m_nSize = RandNumberSet.MIN_SIZE  	         	  

        if self.__m_nSize > RandNumberSet.MAX_SIZE:  	         	  
            self.__m_nSize = RandNumberSet.MAX_SIZE  	         	  

        # sanity check on __m_nMax: pick the larger of `nMax` or `nSize^2 * 2`  	         	  
        self.__m_nMax = max(nMax, self.__m_nSize * self.__m_nSize * 2)
        self.__m_nRowPos = 0  	         	  

        segments = []  	         	  
        segment_size = nMax // self.__m_nSize  # n.b. `//` operator means "integer division"  	         	  
        remainder = nMax % self.__m_nSize  	         	  
        low = 1  	         	  
        for segment in range(1, self.__m_nSize + 1):  	         	  
            high = low + segment_size  	         	  
            # When `len(RandNumberSet)` is not evenly divisible by `nSize`,  	         	  
            # there will be some numbers left over.  Distribute these extra  	         	  
            # numbers starting from segment #0, going up from there
            if segment <= remainder:  	         	  
                high += 1  	   
# -------------- I ADDED THIS NEXT BIT ------------------------------------
            for piece in list(range(low, high + 1)):
                # will go through each number in the new list to check for duplicates
                if piece not in segments:
                    segments.append(piece) 
# ---------------------------------------------------------------------- 	         	  
            low = high  	         	  
        self.segments = segments

```

## Phase 3: Implementation *(15%)*

- changed "import Deck" in UI class to "from Deck import Deck" becauseI got an error saying Deck() was not callable
- was trying to add len(self.__m_currentDeck) to a string, changed it to str(len(self.__m_currentDeck))
- was trying to call Deck.card in the Deck class, changed to self.card
- imported RandNumberSet in Card class
- changed all .append() to += when adding to strings

## Phase 4: Testing & Debugging *(30%)*

**Test: ran bingo.py to see how far it got**
- crashed after entering card size, was trying to compare a string and an int in the RandNumberSet class; converted strings to ints before comparison

- crashed after entering number of cards, was trying to concatenate int to str in the Deck class; changed string to an int (now addition, not concatenation)

- was trying to compare string and int in RandNumberSet class; converted strings to ints

- was trying to multiply by strings in RandNumberSet class, then tried to use integer division on two strings; converted strings to ints

- got 'unhashable type int' error; changed how I was adding elements to list

- got a typeError with the shuffle function, as well as with a bunch of other functions whenever it tried to access segments; segments was noneType, the array was not being filled properly after the check for duplicates. Changed how I checked for doubles, array now filled properly

- error when trying to find the lenth of one card in the Card class, added it as an argument for the class for convenience

- typeError when trying to return a Card; forgot to actually put a return statement in the __Str__ function in the Card class

- Bingo card formatting had the right border style and lettering, but did not have any numbers; number set was not being sorted and split into segments correctly, which was messing up next_row(). realized I did not actually need to change the source code as much as I did, restored it and it fixed it

- was not printing the deck menu after creating a deck; forgot to call it

- was printing two different ID numbers before printing out a card; had accidentally added an ID number to the same string twice, one of which was not even the correct number. removed second number

- could not write deck to file, said argument must be str not Deck; changed input to a string object

- max numbers needs to be calculated based off of the card size; 


**Test: runTests.py **
- failed free sapce test; completely forgot to include the free space in the cards. ended up rewriting how I put the cards together

- tests are not running properly?; I think it's because I added some arguments to Card class or something? I don't know how to fix the test

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
