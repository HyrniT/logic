from Clause import Clause
from itertools import combinations

class KnowledgeBase:
    # Init KB
    def __init__(self) -> None:
        self.clauses = [] # KB is a list of CNF clause

    # Add clause into KB
    def addClause(self, clause):
        self.clauses.append(clause)

    # Remove duplicate and sort clauses
    def buildKnowledgeBase(self, stringAlpha, stringClauses):
        stringAlpha = stringAlpha.strip()
        stringLiterals = stringAlpha.split('OR')
        for stringLiteral in stringLiterals:
            clause = Clause.parseClause(stringLiteral)
            clause.negate()
            self.addClause(clause)
        for stringClause in stringClauses:
            clause = Clause.parseClause(stringClause)
            clause.cleanClause()
            self.addClause(clause)
    
    # Resolution algorithm
    def PL_Resolution(self):
        inputClauses = set(self.clauses) # contain input clauses
        outputClauses = [] # contain output clauses
        isUnsatisfiable = False
        #print(inputClauses)

        # Artificial Intelligence: A Modern Approach, Third Edition, Chapter 7, Figure 7.12, PL-RESOLUTION funtion
        while True:
            new = set() # to remove duplicate after update

            # https://www.geeksforgeeks.org/python-program-to-get-all-unique-combinations-of-two-lists/
            for (clause1, clause2) in combinations(inputClauses, 2): # create a combination with 2 clauses
                resolvents, isEmpty = Clause.PL_Resolve(clause1, clause2)
                new.update(resolvents)
                isUnsatisfiable |= isEmpty # if contain the empty clause -> True

            # https://www.geeksforgeeks.org/python-set-difference/
            diffenceClauses = new.difference(inputClauses) # diffenceClauses =  new \ inputClauses
            outputClauses.append(diffenceClauses)
            inputClauses.update(new)
            
            if isUnsatisfiable == True:    # if entail
                return True, outputClauses
            if len(diffenceClauses) == 0:  # if new is a subset of inputClauses
                return False, outputClauses 
            