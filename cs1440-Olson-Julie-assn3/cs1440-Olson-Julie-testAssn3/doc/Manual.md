# Bingo! User Manual  	         	  
To run this program, open a command line and navigate to the correct directory. Then type 'python ./src/bingo.py' and hit enter.

When the program is first launched, you will see a prompt on your screen asking you if you want to create a new deck or exit the program. To exit the program, type 'x' or 'X' and hit enter to quit the program. If you want to create a new deck, type "c" or "C" and hit enter. If you happen to enter anything other than X or C, the program will give you a prompt saying the input was not a valid option before reprinting the menu. Simply enter X or C and hit enter to continue.

Note: menu is not case sensitive, so it does not matter if your input is upper or lower case

If you chose to create a new deck, you will see a prompt asking you to choose a card size. To pick what size card you would like, type a number from the range given (3 - 16) in numerical form (example: '7', not 'seven'). 

Note: If invalid input is given at any time the program will remind you of what type of input is expected, and reprompt you as many times as needed

Next you will be asked to choose a maximum number from the provided range. Just like the last prompt, enter your choice in numeric form. 

Next you will be asked to choose how many cards you want to be in your deck. You will be given a range of numbers to choose from, simply enter your choice in numeric form.

You will now see a menu of options that will allow you to choose what to do with the deck you have created. You will have the option to enter (P) to print one card, (D) to display the entire deck, (S) to save the deck to a text file, or (X) to return to the main menu.

PRINTING ONE CARD: if you entered (P) you will now be asked to choose which card you want to print by entering an ID number. This ID number corresponds to the card's position in the deck, and should be given in numeric form. The program will then print the ID number to the screen along with the corresponding bingo card. You will then be presented with the menu of four options again and can repeat the process from the previous step.

DISPLAY ENTIRE DECK: if you entered (D) the program will display the entire deck, with an ID number in front of each card. You will then be presented with the menu of four options again and can repeat the process from the previous step.

SAVE DECK TO TEXT FILE: if you entered (S) you will be asked to enter the name of the output file you want the deck to be saved to. For example: '5x5.txt' or 'myBingoDeck.txt'. You will then be presented with the menu of four choices and can repeat the process from the previous step.

RETURN TO MAIN MENU: if you entered (X) the program will bring you back to the original menu with the options to create a new deck or exit the program. Further detail on how you can proceed can be found at the beginning of this document if needed. 
