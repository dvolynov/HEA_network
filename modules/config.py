from chemformula import ChemFormula


class Config:
    
    def __init__(self, string: str):
        self.elements, self.weights = self.extract(string)

    def extract(self, string: str) -> tuple:
        formula = ChemFormula(string)

        items = formula.element.items()
        
        elements = [i[0] for i in items]
        weights = [i[1] for i in items]

        return elements, weights