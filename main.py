import re
import data

class Genoma:
    def __init__(self, adn):
        self.size = len(adn)
        self.adn = adn
        self.arn = ""
        self.codons = []
        self.proteins = ""

    def to_arn(self):
        self.arn = self.adn.replace('T', 'U')
        valid = self.validate(self.arn)
        if valid:
            for i in range(0, self.size, 3):
                codon = self.arn[i:i+3]
                self.codons.append(codon)
            return True
        else:
            print("El genoma no es válido")
            return False

    def get_proteins(self):
        for codon in self.codons:
            protein = data.find_set(codon)
            if protein:
                self.proteins += protein
            else:
                print(f"El codon {codon} no es válido")
                return False
        return True

    def validate(self, adn):
        valid = re.compile(r"^(.{3})*$")
        return bool(valid.match(adn))

    def find_orfs(self):
        start_codon = "ATG"
        stop_codons = ["TAA", "TAG", "TGA"]
        pattern = re.compile(start_codon + "([ATGC]{3})*?(" + "|".join(stop_codons) + ")")
        matches = pattern.finditer(self.adn)
        for match in matches:
            print(match.start(), match.end())

def identify_protein_structure(seq):
    pattern = re.compile(r"([WG]{1}\w{1,2}[ED]{1}\w{1,2}[WG]{1})")
    matches = pattern.findall(seq)
    print(matches)

def identify_rna_structure(seq):
    pattern = re.compile(r"((?:G|C){3,}|(?:A|U){3,})")
    matches = pattern.findall(seq)
    print(matches)

def main():
    genoma = Genoma("ATGGATCCAAGTATGGGTGTGAATTCTGTTACCATTTCTGTTGAGGGTATGACTTGCAATTCCTGTGTTTGGACCATTGAGCAGCAGATTGGAAAAGTGAATGGTGTGCATCACATTAAGGTATCACTGGAAGAAAAA")

    if genoma.to_arn():
        print("La conversión a ARN fue exitosa.")
    else:
        print("La conversión a ARN falló.")

    if genoma.get_proteins():
        print("La obtención de proteínas fue exitosa.")
    else:
        print("La obtención de proteínas falló.")

    print("Codones:", genoma.codons)
    print("Proteínas:", genoma.proteins)

    print("Longitud:", genoma.size)
    genoma.find_orfs()

    # Ejemplo de identificación de estructura de proteínas
    protein_seq = genoma.proteins
    print("Proteínas:", protein_seq)
    print("Longitud:", len(protein_seq))
    identify_protein_structure(protein_seq)

    # Ejemplo de identificación de estructura de ARN
    rna_seq = genoma.arn
    print("ARN:", rna_seq)
    identify_rna_structure(rna_seq)

if __name__ == "__main__":
    main()
