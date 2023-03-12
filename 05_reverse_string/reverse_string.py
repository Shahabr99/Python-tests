def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    letter_list = list(phrase)
    print(letter_list)
    reversed_phrase = letter_list[::-1]
    print(reversed_phrase)
    return ('').join(reversed_phrase)





