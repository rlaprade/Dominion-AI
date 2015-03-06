
class Error(Exception):
    """Base class for errors"""
    pass
    
class CardError(Error):
    """Base class for errors involving a card"""
    def __init__(self, card):
        self.card = card
        
    def __str__(self):
        return "{} not available".format(card)
        
#####################################################################
    
class NoAvailableCardError(CardError):
    pass
    
class HandError(NoAvailableCardError):
    """Exception raised when a card is attempted to be
    accessed in a player's hand, but there is no
    such card in the hand
    """
    def __str__(self):
        return "No {} in hand.".format(self.card)
        
class SupplyError(NoAvailableCardError):
    """Exception indicating that no copies of the
    requested card remain in the supply
    """
    def __str__(self):
        return "No {} cards remaining in supply.".format(self.card)
        
#####################################################################        
        
class InsufficientFundsError(CardError):
    def __str__(self):
        if str(self.card)[0] in set(['a','e','i','o','u']):
            return "Insufficient resources to buy an {}.".format(self.card)
        else:
            return "Insufficient resources to buy a {}.".format(self.card)
        
class ZeroActionsError(CardError):
    def __str__(self):
        return "You cannot play {} because you have no remaining actions.".format(self.card)
