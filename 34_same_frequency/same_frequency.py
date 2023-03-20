def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    num1_s = str(num1)
    num2_s = str(num2)
    if len(num1_s) > len(num2_s):
        return False
    elif len(num1_s) < len(num2_s):
        return False
    else:
        return True
    
   
