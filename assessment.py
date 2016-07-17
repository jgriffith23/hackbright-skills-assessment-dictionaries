"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    # Split string into words, along spaces.
    phrase = phrase.split(" ")

    # Initialize empty dictionary to contain word counts.
    word_counts = {}

    # Iterate over words in provided string.
    for word in phrase:

        # Try to get the value for the current word in word_counts. If a key
        # exists for the current word, increment its count. Otherwise, add it
        # to word_counts with a value of 1.
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

# Rather than define what could easily become a rather large data structure
# here, import it from a separate file.
from melon_data import melons

def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon
    
    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25 
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    # If Ubermelon does stock the melon, return the actual price from our 
    # dictionary. Otherwise, tell the user there is no price for that melon.
    if melon_name in melons:
        return melons[melon_name]
    else: 
        return "No price found"


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    # Initialize an empty dictionary to contain word lengths.
    word_lengths = {}

    # Iterate over the list of words.
    for word in words:

        # Get the current word's length.
        length = len(word)

        # If the length exists as a key in our dictionary, append the current
        # word to the key's value, which is a list. Else, create the key and
        # add the current word as its value.
        word_lengths[length] = word_lengths.get(length, [])
        word_lengths[length].append(word)

    # Use list comprehension to create a list of tuples of the form
    # (length, sorted(words of that length)).
    word_lengths_as_tuples = [(length, sorted(word_lengths[length])) for length
                              in word_lengths]

    # We just made the list of tuples from a dictionary, so there's no
    # gurantee it's sorted by word length. Sort just in case, and return.
    return sorted(word_lengths_as_tuples)

# Import official English-to-Pirate Dictionary, so we can look up words
# for our automatic translation program.
from english_to_pirate_dictionary import english_to_pirate

def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """


    # Split the passed phrase along spaces so we can operate on individual
    # words as needed.
    phrase = phrase.split(" ")

    # Initialize an empty list to contain our pirate-ized phrase.
    pirate_phrase = []

    # Iterate over the words in the passed phrase
    for word in phrase:

        # Look the word up in the dictionary. If it's there, swap the English
        # word we're looking at for the pirate version. Otherwise, do nothing.
        if word in english_to_pirate:
            word = english_to_pirate[word]

        # Append the word to the pirate-ized list of words.
        pirate_phrase.append(word)

    # Join the translated list of words to create one phrase.
    return " ".join(pirate_phrase)

def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # Initialize an empty dictionary to contain our words grouped by first
    # letter. That should allow us to look up all words that start with a
    # particular letter.
    names_by_first_letter = {}

    # Iterate over names in passed list.
    for name in names:

        # Get the first letter of the name.
        first_letter = name[0]

        # If that letter is not in the dictionary, add it with a value of []. Either way,
        # append the name we're currently looking at. Creating the list this way
        # ensures that the words will appear in the order given by the passed list.
        names_by_first_letter[first_letter] = names_by_first_letter.get(first_letter, [])
        names_by_first_letter[first_letter].append(name)

    # Initialize an empty list for our final game list.
    silly_list = []

    # Set the current word to the first word the user passed.
    current_word = names[0]

    # Set state variable to True. It should remain True until we're done
    # creating the silly list of words.
    creating_list = True

    # As long as we're still creating the list...
    while creating_list:

        # Append the word we're currently looking at to that list.
        silly_list.append(current_word)

        # Remove the current word from the list associated with the word's
        # first letter in our dictionary, since we don't want to us the same
        # word twice.

        # In the given example, names_by_first_letter has the following key/value pair:
        #     'b': ['bagon', 'baltoy', 'booger']

        # When current_word is 'bagon', current_word[0] is 'b'. So this line would
        # remove 'bagon' from the 'b' key's associated list of words.
        names_by_first_letter[current_word[0]].remove(current_word)

        # Get the last letter of the current word, so we can pick the next word.
        last_letter = current_word[-1]

        # If the list associated with the last_letter in our dictionary
        # is not empty (that is, if we haven't removed all words from
        # it), then update the current word to be the first remaining word in
        # that list.
        if names_by_first_letter[last_letter] != []:
            current_word = names_by_first_letter[last_letter][0]

        # Otherwise, we must be done. Update state variable to False to end
        # the loop.
        else:
            creating_list = False

    return silly_list

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
