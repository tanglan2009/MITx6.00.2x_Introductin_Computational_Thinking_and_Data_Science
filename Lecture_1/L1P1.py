# Default Value

def isAlphabeticalWord(word, wordList = None):
    if len(word) > 0:
        curr = word [0]
    for letter in word:
        if curr > letter:
            return False
        else:
            curr = letter
    if wordList is None:
        return True
    return word in wordList

print isAlphabeticalWord('zoo', wordList= None)


def f(x, myList = None):       # don't use a mutable type(eg alist, dictionary) as a default value.
    if myList == None:
        # This WILL allocate a new list on every call to the function.
        myList = []
    myList.append(x)
    return myList

print f(6)
print f(10)