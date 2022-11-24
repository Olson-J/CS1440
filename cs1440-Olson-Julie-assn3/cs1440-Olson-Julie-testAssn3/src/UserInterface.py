from Deck import Deck
from Menu import Menu  	         	  
from MenuOption import MenuOption
from math import floor


class UserInterface():  	         	  
    """  	         	  
    Provide the UserInterface for the program, which consists of the Main menu and the Deck menu  	         	  

    Also provides methods for accepting and validating user input  	         	  
    """  	         	  

    def __init__(self):  	         	  
        self.__m_currentDeck = None  	         	  
        self.__m_menu = Menu("Main")  	         	  
        self.__m_menu += MenuOption("C", "Create a new deck")  	         	  
        self.__m_menu += MenuOption("X", "Exit the program")  	         	  

    def run(self):  	         	  
        """  	         	  
        Return None: present the main menu to the user  	         	  

        Repeatedly prompt for a valid command until good input is given, or the program is exited  	         	  
        """  	         	  
        print("Welcome to the Bingo Deck Generator\n")  	         	  

        while True:  	         	  
            command = self.__m_menu.prompt()
            if command.upper() == "C":  	         	  
                self.__create_deck()  	         	  
            elif command.upper() == "X":  	         	  
                break  	         	  

    def __deck_menu(self):  	         	  
        """  	         	  
        Return None  	         	  

        Present the deck menu to user until a valid selection is chosen  	         	  
        """  	         	  
        menu = Menu("Deck")  	         	  
        menu += MenuOption("P", "Print a card to the screen")  	         	  
        menu += MenuOption("D", "Display the whole deck to the screen")  	         	  
        menu += MenuOption("S", "Save the whole deck to a file")  	         	  
        menu += MenuOption("X", "Return to the Main menu")  	         	  

        while True:
            command = menu.prompt()  	         	  
            if command.upper() == "P":  	         	  
                self.__print_card()
            elif command.upper() == "D":
                print(self.__m_currentDeck)
            elif command.upper() == "S":  	         	  
                self.__save_deck()  	         	  
            elif command.upper() == "X":  	         	  
                break  	         	  

    def __get_str(self, prompt):
        """  	         	  
        return a string given by the user in response to a prompt
        repeat prompt until non empty string is given
        """
        while True:
            string = input(prompt)
            if string != "":
                return string
            else:
                print("Please enter a file name such as 'myDeck.txt'")

    def __get_int(self, prompt, lo, hi):  	         	  
        """  	         	  
        return an int given by the user in response to a prompt
        check that input is within the range of lo and high
        re-prompt if not         	  
        """
        while True:
            string = input(prompt)
            if string.isnumeric():
                if (int(string) >= lo) and (int(string) <= hi):
                    return string
                else:
                    print("Please input a number in the range [" + str(lo) + " - " + str(hi) + "]\n")
            else:
                print("Please input a number in the range [" + str(lo) + " - " + str(hi) + "]\n")

    def __create_deck(self):
        """
        returns none
        asks user for info regarding the deck and cards
        creates a new deck and stores it in self.__m_currentDeck
        """
        card_size = self.__get_int("\nEnter a card size [3-16]:\n", 3, 16)
        min = int(card_size) * int(card_size) * 2
        max = floor(3.9 * int(card_size) * int(card_size))
        max_num = self.__get_int("\nEnter max number [" + str(min) + " - " + str(max) + "]:\n", min, max)
        num_cards = self.__get_int("\nEnter a number of cards [2 - 8192]:\n", 2, 8192)
        self.__m_currentDeck = Deck(card_size, num_cards, max_num)
        self.__deck_menu()

    def __print_card(self):  	         	  
        """  	         	  
        returns none
        prompt user for card id, re=prompt if input is invalid
        print card id
        print specified card from the deck
        """
        cardID = self.__get_int("\nID of card to print [1 - "
                + str(len(self.__m_currentDeck)) + "]:\n", 1,
                len(self.__m_currentDeck))
        print(self.__m_currentDeck.card(int(cardID)))

    def __save_deck(self):  	         	  
        """
        return none
        get name of file from user
        open file
        save deck to file
        close file
        """
        filename = self.__get_str("\nEnter output file name:\n")
        f = open(filename, "w")
        f.write(str(self.__m_currentDeck))
        f.close()
        print("Deck saved to '" + filename + "'!\n")
