"""
-------------------------------------------------------
Morse Code Definitions and Functions
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2024-03-07"
-------------------------------------------------------
"""
# In order by letters.
DATA1 = (('A', '.-'), ('B', '-...'), ('C', '-.-.'),
         ('D', '-..'), ('E', '.'), ('F', '..-.'),
         ('G', '--.'), ('H', '....'), ('I', '..'),
         ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
         ('M', '--'), ('N', '-.'), ('O', '---'),
         ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
         ('S', '...'), ('T', '-'), ('U', '..-'),
         ('V', '...-'), ('W', '.--'), ('X', '-..-'),
         ('Y', '-.--'), ('Z', '--..'))

# In order by splitting.
DATA2 = (('M', '--'), ('F', '..-.'), ('T', '-'),
         ('C', '-.-.'), ('J', '.---'), ('P', '.--.'),
         ('W', '.--'), ('A', '.-'), ('D', '-..'),
         ('H', '....'), ('K', '-.-'), ('N', '-.'),
         ('R', '.-.'), ('U', '..-'), ('Y', '-.--'),
         ('B', '-...'), ('E', '.'), ('I', '..'),
         ('G', '--.'), ('L', '.-..'), ('O', '---'),
         ('Q', '--.-'), ('S', '...'), ('V', '...-'),
         ('X', '-..-'), ('Z', '--..'))

# In order by popularity.
DATA3 = (('E', '.'), ('T', '-'), ('A', '.-'),
         ('O', '---'), ('I', '..'), ('N', '-.'),
         ('S', '...'), ('H', '....'), ('R', '.-.'),
         ('D', '-..'), ('L', '.-..'), ('U', '..-'),
         ('C', '-.-.'), ('M', '--'), ('P', '.--.'),
         ('F', '..-.'), ('Y', '-.--'), ('W', '.--'),
         ('G', '--.'), ('B', '-...'), ('V', '...-'),
         ('K', '-.-'), ('J', '.---'), ('X', '-..-'),
         ('Z', '--..'), ('Q', '--.-'))


class ByLetter:
    """
    -------------------------------------------------------
    Stores letters and matching Morse codes. Compares
    elements by letter attribute.
    -------------------------------------------------------
    """

    def __init__(self, letter, code):
        """
        -------------------------------------------------------
        Initialize a ByLetter object.
        Use: var = ByLetter(letter, code)
        -------------------------------------------------------
        Parameters:
            letter - a letter of the alphabet (str)
            code - the Morse code matching letter (str)
        Returns:
            A ByLetter object.
        -------------------------------------------------------
        """
        self.letter = letter
        self.code = code

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Compares source against target for equality.
        Object are equal if their letters match.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - ByLetter to compare source to (ByLetter)
        Returns:
            result - True if letters match, False otherwise (boolean)
        -------------------------------------------------------
        """

        result = self.letter == target.letter

        return result

    def __lt__(self, target):
        """
        -------------------------------------------------------
        Determines if source comes before target.
        Use: source < target
        -------------------------------------------------------
        Parameters:
            target - ByLetter to compare source to (ByLetter)
        Returns:
            result - True if source precedes target,
              False otherwise (boolean)
        -------------------------------------------------------
        """

        result = self.letter < target.letter
        return result

    def __le__(self, target):
        """
        -------------------------------------------------------
        Determines if source precedes or is or equal to target.
        Use: source <= target
        -------------------------------------------------------
        Parameters:
            target - ByLetter to compare source to (ByLetter)
        Returns:
            result - True if source precedes or is equal to target,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        result = self.letter <= target.letter
        return result

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of ByLetter data.
        Use: print(source)
        Use: string = str(source)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of ByLetter (str)
        -------------------------------------------------------
        """
        return "({}, {})".format(self.letter, self.code)


class ByCode:
    """
    -------------------------------------------------------
    Stores letters and matching Morse codes. Compares
    elements by code attribute.
    -------------------------------------------------------
    """

    def __init__(self, letter, code):
        """
        -------------------------------------------------------
        Initialize a ByCode object.
        Use: var = ByCode(letter, code)
        -------------------------------------------------------
        Parameters:
            letter - a letter of the alphabet (str)
            code - the Morse code matching letter (str)
        Returns:
            A ByCode object.
        -------------------------------------------------------
        """
        self.letter = letter
        self.code = code
        return

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Compares source against target for equality.
        Object are equal if their codes match.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - ByCode to compare source to (ByCode)
        Returns:
            result - True if codes match, False otherwise (boolean)
        -------------------------------------------------------
        """

        result = self.code == target.code
        return result

    def __lt__(self, target):
        """
        -------------------------------------------------------
        Determines if source comes before target.
        Use: source < target
        -------------------------------------------------------
        Parameters:
            target - ByCode to compare source to (ByCode)
        Returns:
            result - True if source precedes target,
              False otherwise (boolean)
        -------------------------------------------------------
        """

        result = self.code < target.code
        return result

    def __le__(self, target):
        """
        -------------------------------------------------------
        Determines if source precedes or is or equal to target.
        Use: source <= target
        -------------------------------------------------------
        Parameters:
            target - ByCode to compare source to (ByCode)
        Returns:
            result - True if source precedes or is equal to target,
              False otherwise (boolean)
        -------------------------------------------------------
        """

        result = self.code <= target.code
        return result

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of ByCode data.
        Use: print(source)
        Use: string = str(source)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of ByCode (str)
        -------------------------------------------------------
        """
        return "({}, {})".format(self.code, self.letter)

def fill_letter_bst(bst, values):
    """
    -------------------------------------------------------
    Fills a BST with ByLetter Morse code letter/code pairs
    (Function must convert contents of values to ByLetter objects)
    Use: fill_letter(bst, values)
    -------------------------------------------------------
    Parameters:
        bst - a bst (BST)
        values - set of Morse code letter/code pairs (list of tuples)
    Returns:
        None
    -------------------------------------------------------
    """

    for item in values:
        value = ByLetter(item[0], item[1])
        bst.insert(value)
    return
    
def fill_code_bst(bst, values):
    """
    -------------------------------------------------------
    Fills a BST with ByCode Morse code letter/code pairs.
    (Function must convert contents of values to ByCode objects)
    Use: fill_letter(bst, values)
    -------------------------------------------------------
    Parameters:
        bst - a bst (BST)
        values - set of Morse code letter/code pairs (list of tuples)
    Returns:
        None
    -------------------------------------------------------
    """

    for value in values:
        item = ByCode(value[0], value[1])
        bst.insert(item)
    return
    
def encode_morse(bst, text):
    """
    -------------------------------------------------------
    Converts English text to Morse code
    Use: code = encode_morse(bst, text)
    -------------------------------------------------------
    Parameters:
        bst - Morse code bst sorted by letter (BST)
        text - English text to convert (str)
    Returns:
        result - Morse code version of text (str)
    -------------------------------------------------------
    """

    result = ""
    for char in text.upper():
        if char.isalpha():
            item = ByLetter(char, None)
            item = bst.retrieve(item)
            result += item.code + " "
        elif char == " ":
            result += "\n"
    result = result.strip()
    return result
    
def decode_morse(bst, code):
    """
    -------------------------------------------------------
    Converts Morse code to English text
    Use: text = decode_morse(bst, code)
    -------------------------------------------------------
    Parameters:
        bst - Morse code bst sorted by code (BST)
        code - Morse code to convert (str)
    Returns:
        result - English version of code (str)
    -------------------------------------------------------
    """

    result = ""
    lst = code.split()
    for char in lst:
        item = ByCode(None, char)
        character = bst.retrieve(item)
        result+=character.letter
    return result
