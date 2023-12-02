import re
import data

class Genoma:
    def __init__(self,adn):
        self.size = len(adn)
        self.adn = adn
        self.arn = ""
        self.codons = []
        self.proteins = ""

    def to_arn(self):
        self.arn = self.adn.replace('T', 'U')
        valid = self.validate(self.arn)
        if(valid):
            for i in range(0, self.size, 3):
                codon = self.arn[i:i+3]
                self.codons.append(codon)
            return True
        else:
            print("El genoma no es valido")
            return False
    
    def get_proteins(self):
        for codon in self.codons:
            protein = data.find_set(codon)
            if protein:
                self.proteins = self.proteins + protein
            else:
                print("El codon {} no es valido".format(codon))
                return False
        return True

    def validate(self, adn):
        valid = re.compile(r"^(.{3})*$")
        if valid.match(adn):
            return True
        else:
            return False
        

def main():

    genoma = Genoma("ATGGATCCAAGTATGGGTGTGAATTCTGTTACCATTTCTGTTGAGGGTATGACTTGCAATTCCTGTGTTTGGACCATTGAGCAGCAGATTGGAAAAGTGAATGGTGTGCATCACATTAAGGTATCACTGGAAGAAAAA")


    if genoma.to_arn():
        print("La conversion a ARN fue exitosa.")
    else:
        print("La conversion a ARN fallo.")


    if genoma.get_proteins():
        print("La obtencion de proteinas fue exitosa.")
    else:
        print("La obtencion de proteinas fallo.")


    print("Codones:", genoma.codons)
    print("Proteinas:", genoma.proteins)



if __name__ == "__main__":
    main()
