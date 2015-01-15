# This file contains tools which may be useful throughout the project

class Counter(dict):
    """The Counter class is a dictionary that will
    give zero for keys that are not in the dictionary,
    rather than raising an error.
    """    
    def __getitem__(self, key):
        if key in self:
            return dict.__getitem__(self, key)
        return 0
        
        
def list_to_counter(lst):
    """Converts a list to a counter object"""
    c = Counter()
    for entry in lst:
        c[entry] += 1
    return c
        
# def cost(card):
    # """Abstraction for finding the cost of a card
    # Currently, card should be a Card object.
    # """
    # return card.cost