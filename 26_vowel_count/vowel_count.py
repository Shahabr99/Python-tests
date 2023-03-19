def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    result = {}
    
    new_phrase = phrase.lower()
    for letter in new_phrase:
        if vowels.find(letter) != -1:
            
            if letter in result: 
                v = result.get(letter) + 1
                result[letter] = v
            else:
                result[letter] = 1
    print(result)
        
