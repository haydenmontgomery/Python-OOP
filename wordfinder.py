"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    """
    A class that for reading from a file and getting words from it
    
    >>> wf = WordFinder("words.txt")

    >>> wf.words[9] == 'Aaron'
    True

    >>> wf.words[8009] == 'anchylose'
    True

    >>> wf.words[103609] == 'laemodipodan'
    True
    """
    def __init__(self, filename):
        """
        Initializer for the Word Finder.
        """
        self.filename = filename
        self.words = []
        self.read_file()
        
    def __repr__(self):
        """
        Representation of the class in string form
        """
        return f"WordFinder({self.filename})"

    def read_file(self):
        """
        Reads the text file and puts the words into a list.
        """
        with open(self.filename, 'r') as file:
            for line in file:
                self.words.append(line.strip())

    def random(self):
        """
        Returns a random word from the read file
        """
        return self.words[randint(0,len(self.words) - 1)]
    
