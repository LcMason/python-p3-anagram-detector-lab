# your code goes here!
class Anagram:
    pass

    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)

    def get_word(self):
        return self._word

    def set_word(self, word):
        # conditional
        self._word = word

    # match instance method. Should take a list of possible anagrams
    # the list() function in Python separates each character of a string into individual elements in a list.
    # may need to use anther variable other than `word`
    # should return all matches in the list (if...)
    # if no matches, return an empty list. (else: ...)
    def match(self, words):
        pass
        anagram_list = []
        for candidate in words:
            if sorted(candidate) == self.sorted_word:
                anagram_list.append(candidate)
        return anagram_list
        


