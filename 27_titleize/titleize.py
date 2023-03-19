def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    result = phrase.split(' ')
   
    capitalized_phrase = [word.capitalize() for word in result]
    titlized_phrase = (' ').join(capitalized_phrase)
    print(titlized_phrase)