class Genoma:
    def __init__(self,adn):
        self.size = len(adn) - 1
        self.adn = adn
        self.arn = ""
        self.proteins = []

    def toArn(self):
        self.arn = self.adn.replace('T', 'U')
    
    def toProtein(self):
        self.toArn()
        for i in range(0, self.size, 3):
            codon = self.arn[i:i+3]
            self.proteins.append(codon)

