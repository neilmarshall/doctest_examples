import doctest

def test_func(text, multiplier):
    """A simple toy function to show the use of docstrings
    
    Function called with expected arguments:
    
    >>> test_func('abc', 2)
    'ABCABC'
    
    Function will raise an exception for arguments not of the right type
    
    >>> test_func('abc', 'abc')
    Traceback (most recent call last):
        ...
    TypeError: Expected str and int, got <class 'str'> and <class 'str'>
    
    >>> test_func(5, 5)
    Traceback (most recent call last):
        ...
    TypeError: Expected str and int, got <class 'int'> and <class 'int'>

    Args
    ----
    text : str
        text; will be converted to upper case
        
    multiplier : int
        integer; will concatenate this many copies of text
        
    Returns
    -------
    return_value : str
    
    """
    if not (isinstance(text, str) and isinstance(multiplier, int)):
        raise TypeError("Expected str and int, got {} and {}"
            .format(type(text), type(multiplier)))
    return multiplier * text.upper()

if __name__ == "__main__":
    doctest.testmod()
    print(test_func('abc', 2))
