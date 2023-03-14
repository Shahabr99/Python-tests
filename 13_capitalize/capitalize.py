def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    first_letter = phrase[0]
    
    capitalized = first_letter.upper()
   
    new_phrase = phrase.replace(first_letter, capitalized, 1)
    return new_phrase
