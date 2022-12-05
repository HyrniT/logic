from Literal import Literal

class Clause:
    # Init clause
    def __init__(self) -> None:
        self.literals = [] # clause is a list of literals
    
    # Represent clause
    def __repr__(self):
        if len(self.literals) != 0:
            return ' OR '.join(str(literal) for literal in self.literals)
        else:
            return '{}'
    
    # Override == (object of class become unhashable)
    def __eq__(self, clause) -> bool:
        if len(self.literals) != len(clause.literals):
            return False
        return set(self.literals) == set(clause.literals)
    
    # Hash type clause (make object of class become hashable)
    def __hash__(self) -> int:
        result = tuple(self.literals) # conver to tuple to hash because unhashable type: 'list'
        return hash(result)
    
    # Override < (to sort clauses)
    def __lt__(self, clause) -> bool:
        if len(self.literals) != len(clause.literals):
            return len(self.literals) < len(clause.literals)

        for index in range(len(self.literals)):
            if self.literals[index] != clause.literals[index]:
                return self.literals[index] < clause.literals[index]
        
        return False
    
    # Check if clause is empty
    def isEmpty(self):
        return len(self.literals) == 0
    
    # Check if clause is meaningless (example: A OR -B OR B)
    def isMeaningless(self):
        for index in range(len(self.literals) - 1):   
            if self.literals[index].isOpposite(self.literals[index + 1]): # it's ok because your list literals 
                return True                                               # sorted and removed duplicate
        return False

    # Add literal into clause
    def addLiteral(self, literal):
        self.literals.append(literal)
    
    # Remove duplicate and sort literals
    def cleanClause(self):
        self.literals = sorted(set(self.literals))

    # Clone clause with exception
    def cloneClauseNot(self, _literal):
        newClause = Clause() 

        for literal in self.literals:
            if literal != _literal:
                newClause.addLiteral(literal)
        
        return newClause
    
    # Parse clause
    def parseClause(stringClause):
        newClause = Clause()
        stringClause = stringClause.strip() # remove spaces at the beginning and at the end of the string
        stringLiterals = stringClause.split('OR') # split string into list with seperator OR
        
        for stringLiteral in stringLiterals:
            literal = Literal.parseLiteral(stringLiteral)
            newClause.addLiteral(literal)
        
        newClause.cleanClause()
        return newClause

    # Merge clauses
    def mergeClauses(clause1, clause2):
        newClause = Clause() 

        newClause.literals = clause1.literals + clause2.literals 
        newClause.cleanClause()

        return newClause

    # Negate clause
    def negate(self):
        for literal in self.literals:
            literal.negate()

    # Resolve clauses
    def PL_Resolve(clause1, clause2):
        isEmpty = False
        resolvents = set()

        for literal1 in clause1.literals:
            for literal2 in clause2.literals:
                if literal1.isOpposite(literal2):
                    newClause = Clause.mergeClauses(clause1.cloneClauseNot(literal1), 
                        clause2.cloneClauseNot(literal2))
                    if newClause.isMeaningless(): # xử lý dấu chấm đỏ thứ 3 trong đề bài
                        continue
                    if newClause.isEmpty():
                        isEmpty = True
                    resolvents.add(newClause)

        return resolvents, isEmpty
    
# TEST CLAUSE
"""
A = Clause.parseClause('-B OR A OR A OR B')
B = Clause.parseClause('B OR A OR -B OR -B')
C = Clause.parseClause('C OR -A')
D = Clause.mergeClauses(A, C)
print(A)
print(B)
print(A.isMeaningless())
print(A == B)
print(D)
"""