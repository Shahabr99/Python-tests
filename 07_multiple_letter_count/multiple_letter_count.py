def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    count = 1
    dict = {}
    for letter in phrase:
        if letter in dict:
            val = dict.get(letter)
            dict[letter] = val + 1
        elif letter not in dict:
            dict[letter] = count
    return dict   
        