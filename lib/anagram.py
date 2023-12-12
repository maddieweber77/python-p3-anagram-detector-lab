list = ['enlists', 'google', 'inlets', 'banana']
class Anagram:
    def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])
        
    def match(self, word_list):
        match_word_list = []

        for word in word_list:
            if sorted([letter for letter in word]) == self.word_letters:
                match_word_list.append(word)
        
        return match_word_list
                
        
    # for length of chars of word
    # check each character to see if it's in the first word
        ## if it is, return the anagram
        # if it isn't, move on to the next word
    
    # two loops -- looping through the characters of the words and looping through the words