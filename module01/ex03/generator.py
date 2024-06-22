import random


def generator(text, sep=" ", option=None):
    '''Splits the text according to sep value and yield the substrings.
        option precise if a action is performed to the substrings before it is yielded
    '''
    if not isinstance(text, str):
        print("ERROR")
        return
    
    words = text.split(sep)
    if option == "shuffle":
        random.shuffle(words)
        for word in words:
            yield word
    
    if option == "ordered":
        for word in sorted(words):
            yield word
            
    if option == "unique":
        for word in set(words):
            yield word
    
    if option is None:
        for word in words:
            yield word
