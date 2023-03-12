def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    capitalized = phrase[0].upper()
    
    new_phrase = phrase.replace(phrase[0], capitalized)
    return new_phrase