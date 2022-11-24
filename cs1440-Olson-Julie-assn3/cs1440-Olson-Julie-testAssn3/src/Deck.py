from Card import Card  	         	  
from RandNumberSet import RandNumberSet  	         	  


class Deck():  	         	  
    def __init__(self, card_size, num_cards, max_num):  	         	  
        """
        deck constructor
        save arguments to use elsewhere
        for each card in the deck
            create a non-repeating list of random numbers (less than max_num)
            shuffle numbers within their segments
            pass deck position (ID) and sorted number set to Card
            save the formatted card string to the deck
        """
        self.num_cards = int(num_cards)
        self.card_size = int(card_size)
        self.max_num = int(max_num)
        self.deck = []

        for i in range(1, self.num_cards + 1):
            numbers = RandNumberSet(card_size, max_num)
            numbers.shuffle()
            intCard = str(Card(i - 1, numbers))
            self.deck.append(str(intCard))
        self.__str__()

    def __len__(self):  	         	  
        """  	         	  
        Return an integer: the number of cards in this deck  	         	  
        """  	         	  
        return self.num_cards

    def card(self, n):  	         	  
        """  	         	  
        Retrieve Card N from the deck  	         	  
        """
        if int(n) <= 0:
            return None
        if int(n) > self.num_cards:
            return None
        else:
            return self.deck[int(n) - 1]

    def __str__(self):  	         	  
        """  	         	  
        Return String: Display the entire Deck as a string  	         	  
        """
        deckString = ''
        for i in range(1, self.num_cards + 1):
            deckString += (self.deck[i - 1])
        deckString += '\n'
        return deckString

