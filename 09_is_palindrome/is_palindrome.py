def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    modified_phrase = phrase.lower().replace(' ', '')
    print(modified_phrase)
    list_form = list(modified_phrase)
    print(list_form)
    reversed_array = list_form[::-1]
    print(reversed_array)
    new_word = ("").join(reversed_array)
    print(new_word)
    if new_word == modified_phrase:
        return True
    else:
        return False