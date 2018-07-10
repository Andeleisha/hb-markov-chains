"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    with open(file_path) as filename:

    	string_of_file = filename.read()

    	return string_of_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here

 
    words = text_string.split()
    

    for i in range(len(words) - 1):
    	key = tuple([words[i], words[i + 1]])


    	possible_word = []
    	chains[key] =chains.get(key, possible_word)

    	if key in chains:
    		possible_word = chains[key]
    	else:
    		possible_word = []
    	try:
    		possible_word = possible_word.append(words[i+2])
    		# chains[key] =chains.get(key, possible_word)
    	except:
    		return chains

    	# chains[key] =chains.get(key, possible_word)

    # print(chains)

    # return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    #Pick a random key
    #Append key to string
    #Pick a random word from the list of possible words
    #Append word to string
    #Create a new key 
    #Find the key 
    #Repeat Pick a random word etc etc
    #if possible words is empty list, return string

    keys = list(chains.keys())
    first_key = choice(keys)

    for word in first_key:
    	words.append(word)
    	
    

    rand_word = choice(chains[first_key])
    words.append(rand_word)
    
    new_key = (first_key[1], rand_word)
    print(new_key)


    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
