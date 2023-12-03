import re

import data


class Genome:
    def __init__(self, adn):
        self.adn = adn
        self.size = len(adn)
        self.codons = []
        self.arn = ""
        self.proteins = []

        if self.to_arn():
            print("La obtención de ARN fue exitosa.")
            if self.get_proteins():
                print("La obtención de proteínas fue exitosa.")
        else:
            raise ValueError("Invalid ADN sequence")

    def to_arn(self):
        self.arn = self.adn.replace('T', 'U')
        if self.validate(self.arn):
            for i in range(0, self.size, 3):
                codon = self.arn[i:i + 3]
                self.codons.append(codon)
            return True
        else:
            print("La secuencia de ADN no es válida")
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

    @staticmethod
    def validate(x):
        valid = re.compile(r"^(.{3})*$")
        return bool(valid.match(x))


def find_motif(genome, motif):
    pattern = re.compile(motif)
    matches = pattern.findall(genome.arn)

    print(matches)


def identify_protein_structure(genome):
    proteinstr = ""
    for protein in genome.proteins:
        proteinstr += protein

    print(proteinstr)
    pattern = re.compile(r"([WG]\w{1,2}[ED]\w{1,2}[WG])")
    matches = pattern.findall(proteinstr)
    print(matches)


def identify_rna_structure(genome):
    pattern = re.compile(r"([GC]{3,}|[AU]{3,})")
    matches = pattern.findall(genome.arn)
    print(matches)
