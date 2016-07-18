#START TIME: 2:00 PM

"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    # Convert the given list of words to a set to remove all duplicates.
    unique_words = set(words)

    # Convert the set of unique words back to a list, so it can be returned
    # as the type the design description asked for.
    return list(unique_words)


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    # Convert the two passed lists of items into sets, so we can perform set
    # math to find the elemnets they have in common.
    items1_converted_to_set = set(items1)
    items2_converted_to_set = set(items2)

    # Find the intersection of unique items in the two passed lists.
    intersection = items1_converted_to_set & items2_converted_to_set

    # Return the intersection as a list, as requested in the design description.
    return list(intersection)


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    # Initialize an empty dictionary to contain pairs
    pairs_dict = {}

    # Iterate over the list of numbers
    for number in numbers:

        # First, check to see if the current number is in the dictionary's set of
        # values. If it is, we don't need to do anything, because this pair exists.
        if not number in pairs_dict.values():

            # To access numbers after current number, iterate over indices in list.
            for index in xrange(len(numbers)-1):

                # Fetch next number after current number
                next_num = numbers[index + 1]

                # If the sum is 0, check whether the key exists. Add the pair
                # to the dictionary if not.
                if (number + next_num == 0):
                    pairs_dict[number] = pairs_dict.get(number,next_num)

    # Initialize an empty list to contain pairs converted to lists.
    pairs_list = []

    # Iterate over the items in the dictionary.
    for pair in pairs_dict.items():

        # Convert each dictionary item into a list, and add it to the list
        # to return.
        pairs_list.append(list(pair))

    return pairs_list


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    # Call a function that returns a dictionary, where the keys are characters
    # and each value is the number of times that character appears in the string.
    char_counts = get_char_counts(phrase)

    # Initialize a variable to track the highest number of times a letter occurs
    highest_count = 0

    # Iterate over the keys in char_counts to find the highest number of times
    # a letter occurs. Set highest_count to that value.
    for character in char_counts.iterkeys():
        current_char_count = char_counts[character]
        if current_char_count > highest_count:
            highest_count = current_char_count

    # Use list comprehension to find all characters in char_counts that have
    # counts matching the highest count observed.
    most_common_chars = [character for character in char_counts.iterkeys()
                         if char_counts[character] == highest_count]

    # Sort and return the list of most common characters.
    return sorted(most_common_chars)


def get_char_counts(string):
    """Given a string, finds the number of times each character the string
    contains appears. Ignores spaces.

    Since this function counts characters, not letters, the counts are
    case-sensitive.

    Example:

    >>> get_char_counts("I like turtles.")
    {'e': 2, 'I': 1, 'k': 1, 'l': 2, '.': 1, 'i': 1, 's': 1, 'r': 1, 'u': 1, 't': 2}

    NOTE: Written to encapsulate repeatable behavior and clean up top_chars()
    function.

    """

    # Initialize an empty dictionary to contain character/count pairs.
    char_counts = {}

    # Remove all spaces (" ") from the passed string.
    string = string.replace(" ", "")

    # Iterate over all characters in string. If there's no key/value pair for
    # a given character, add it to the dictionary with a count of 1. Otherwise,
    # Increment the count.
    for character in string:

        # Note: to count letters rather than characters, this could
        # have set the character read to character.lower().
        char_counts[character] = char_counts.get(character, 0) + 1

    return char_counts

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
