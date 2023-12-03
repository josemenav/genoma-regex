import re

import data


def validate(adn):
    valid = re.compile(r"^(.{3})*$")
    return bool(valid.match(adn))


class Genoma:
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
        valid = validate(self.arn)
        if valid:
            for i in range(0, self.size, 3):
                codon = self.arn[i:i+3]
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


def find_motif(genome, motif):
    pattern = re.compile(motif)
    matches = pattern.finditer(genome.adn)
    for match in matches:
        print("Match indexes: ",match.start(), match.end())


def identify_protein_structure(genome):
    proteinstr = ""
    for protein in genome.proteins:
        proteinstr += protein

    print(proteinstr)
    pattern = re.compile(r"([WG]\w{1,2}[ED]\w{1,2}[WG])")
    matches = pattern.findall(proteinstr)
    print("coincidencias encontradas",matches)


def identify_rna_structure(genome):
    pattern = re.compile(r"([GC]{3,}|[AU]{3,})")
    matches = pattern.findall(genome.arn)
    print(matches)


def main():
    print("Secuencia de ADN:")
    genomastr = input("Escribe la secuencia de ADN a analizar o deje en blanco para usar una predeterminada: ")

    if len(genomastr) < 1:
        genoma = Genoma(
            "ATGGATCCAAGTATGGGTGTGAATTCTGTTACCATTTCTGTTGAGGGTATGACTTGCAATTCCTGTGTTTGGACCATTGAGCAGCAGATTGGAAAAGTGAATGGTGTGCATCACATTAAGGTATCACTGGAAGAAAAA")
    else:
        genoma = Genoma(genomastr)

    print("Secuencia de ADN:", genoma.adn)
    print("Tamaño:", genoma.size)
    print("ARN:", genoma.arn)
    print("Codones:", genoma.codons)
    print("Proteínas:", genoma.proteins)
    print("")

    # Ejemplo de busqueda de motif
    print("Busqueda de motif:")
    motif = "ATG"
    print("Motif:", motif)
    find_motif(genoma, motif)
    print("")

    # Ejemplo de identificación de estructura de proteínas
    print("Identificación de estructura de proteínas:")
    identify_protein_structure(genoma)
    print("")

    # Ejemplo de identificación de estructura de ARN
    print("ARN:", genoma.arn)
    identify_rna_structure(genoma)


if __name__ == "__main__":
    main()
