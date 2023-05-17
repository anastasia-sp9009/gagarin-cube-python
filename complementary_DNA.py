#https://www.codewars.com/kata/554e4a2f232cdd87d9000038
def DNA_strand(dna):
    list_dna = list(dna)
    dna_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    result = []
    for i in list_dna:
        result.append(dna_map[i])
    return ''.join(result)

print(DNA_strand("ATTGC"))