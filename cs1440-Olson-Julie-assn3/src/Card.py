from RandNumberSet import RandNumberSet


class Card():
    COLUMN_NAMES = list("BINGODARLYZEMPUX")  	         	  

    def __init__(self, idnum, ns):
        """  	         	  
        Initialize a Bingo! card  	         	  
        """
        self.idnum = int(idnum)
        self.ns = ns
        self.size = len(ns)

    def id(self):
        """
        Return an integer: the ID number of the card
        """
        return self.idnum

    def number_at(self, row, col):  	         	  
        """  	         	  
        Return an integer or a string: the value in the Bingo square at (row, col)  	         	  
        """
        if self.size % 2 != 0:
            middle = (self.size // 2)
            if row == middle and col == middle:
                return "FREE!"
        row = self.ns[row]
        return row[col]

    def __len__(self):
        """  	         	  
        Return an integer: the length of one dimension of the card.  	         	  
        For a 3x3 card return 3, for a 5x5 return 5, etc.  	         	  
        """  	         	  
        return self.size

    def __str__(self):  	         	  
        """  	         	  
        Return a string: a neatly formatted, square bingo card  	         	  
        """
        # first chunk does the column letters and the first border
        cardString = ''
        cardString += "Card #" + str(self.idnum + 1) + '\n'
        for letter in range(self.size):
            cardString += "   "
            cardString += (Card.COLUMN_NAMES[letter])
            cardString += "  "
        cardString += "\n+"
        for chunk in range(self.size):  # dividing lines
            cardString += "-----+"

        # for each chunk, print one line of numbers and one divider line
        # if middle, print free space
        if self.size % 2 != 0:
            middle = (self.size // 2)
        else:
            middle = 10000000000000000
        for row in range(self.size):            # for each row <-->
            nums = self.ns.next_row()
            cardString += "\n|"
            for chunk in range(self.size):      # for each cell
                if row == middle and chunk == middle:
                    cardString += "FREE!|"
                else:
                    if nums[chunk] > 9:             # if number is two digits
                        cardString += " "
                    else:
                        cardString += "  "
                    cardString += str(nums[chunk])
                    if nums[chunk] > 99:            # if number is 3 digits
                        cardString += " |"
                    else:
                        cardString += "  |"
            cardString += '\n+'
            for chunk in range(self.size):
                cardString += "-----+"
        cardString += '\n\n'
        return cardString
