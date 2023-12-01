
starts_with_A = {
            "AUU":"I",
            "AUC":"I",
            "AUA":"I",
            "AUG":"M",
            "ACU":"T",
            "ACC":"T",
            "ACA":"T",
            "ACG":"T",
            "AAU":"N",
            "AAC":"N",
            "AAA":"K",
            "AAG":"K",
            "AGU":"S",
            "AGC":"S",
            "AGA":"R",
            "AGG":"R",
        }

starts_with_C = {
            "CUU":"L",
            "CUC":"L",
            "CUA":"L",
            "CUG":"L",
            "CCU":"P",
            "CCC":"P",
            "CCA":"P",
            "CCG":"P",
            "CAU":"H",
            "CAC":"H",
            "CAA":"Q",
            "CAG":"Q",
            "CGU":"R",
            "CGC":"R",
            "CGA":"R",
            "CGG":"R",
        }

starts_with_G = {
            "GUU":"V",
            "GUC":"V",
            "GUA":"V",
            "GUG":"V",
            "GCU":"A",
            "GCC":"A",
            "GCA":"A",
            "GCG":"A",
            "GAU":"D",
            "GAC":"D",
            "GAA":"E",
            "GAG":"E",
            "GGU":"G",
            "GGC":"G",
            "GGA":"G",
            "GGG":"G",
        }

starts_with_U = {
            "UUU":"F",
            "UUC":"F",
            "UUA":"L",
            "UUG":"L",
            "UCU":"S",
            "UCC":"S",
            "UCA":"S",
            "UCG":"S",
            "UAU":"Y",
            "UAC":"Y",
            "UAA":"*",
            "UAG":"*",
            "UGU":"C",
            "UGC":"C",
            "UGA":"*",
            "UGG":"W",
        }

def is_in_A( codon):
    if codon in starts_with_A:
        return starts_with_A[codon]
    else:
        return False

def is_in_C( codon):
    if codon in starts_with_C:
        return starts_with_C[codon]
    else:
        return False

def is_in_G( codon):
    if codon in starts_with_G:
        return starts_with_G[codon]
    else:
        return False

def is_in_U( codon):
    if codon in starts_with_U:
        return starts_with_U[codon]
    else:
        return False
    
def find_set( codon):
    if is_in_A(codon):
        return is_in_A(codon)
    elif is_in_C(codon):
        return is_in_C(codon)
    elif is_in_G(codon):
        return is_in_G(codon)
    elif is_in_U(codon):
        return is_in_U(codon)
    else:
        return False