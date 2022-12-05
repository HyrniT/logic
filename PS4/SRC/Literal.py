class Literal:
    # Init literal
    def __init__(self, symbol = "", negation = False) -> None:
        self.symbol = symbol
        self.negation = negation

    # Represent literal
    def __repr__(self):
        return '-{}'.format(self.symbol) if self.negation == True else self.symbol

    # Override == (object of class become unhashable)
    def __eq__(self, literal) -> bool:
        return self.symbol == literal.symbol and self.negation == literal.negation
    
    # Hash type literal (make object of class become hashable)
    def __hash__(self):
        result = '-' + self.symbol if self.negation else self.symbol
        return hash(result)

    # Override < (to sort literals)
    def __lt__(self, literal) -> bool:
        if self.symbol != literal.symbol:
            return self.symbol < literal.symbol
        return self.negation < literal.negation # negation = False (0) < negation = True (1) 
                                                # A < -A
                                                # A OR -A

    # Negate symbol
    def negate(self):
        self.negation = 1 - self.negation # if a = True (1) -> a = 1 - True (1) = 0 (False)
                                          # if a = False (0) -> a = 1 - False (0) = 1 (True)
        
    # Check if opposite literals
    def isOpposite(self, literal):
        return self.negation != literal.negation and self.symbol == literal.symbol
    
    # Parse literal
    def parseLiteral(stringLiteral):
        stringLiteral = stringLiteral.strip() # remove spaces at the beginning and at the end of the character

        if stringLiteral[0] == '-':
            newLiteral = Literal(symbol = stringLiteral[1], negation = True) # negative literal
        else:
            newLiteral = Literal(symbol = stringLiteral[0], negation = False) # positive literal

        return newLiteral   

# TEST LITERAL
"""
a = Literal.parseLiteral('-A') # a = -A
b = Literal.parseLiteral('-A') # b = -A
a.negate() # a = A
print(a)
print(b)
print(a < b) # True
print(a.isOpposite(b)) # True
"""