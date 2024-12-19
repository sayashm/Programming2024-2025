# https://dodona.be/nl/courses/4157/series/46299/activities/973922705

class GeneticCode:
    '''
    >>> code = GeneticCode('standard_code.txt')

    >>> code.amino_acid('AGT')
    'S'
    >>> code.amino_acid('cga')
    'R'
    >>> code.amino_acid('UCU')
    'S'
    >>> code.amino_acid('ABC')
    Traceback (most recent call last):
    AssertionError: invalid codon
    >>> code.amino_acid('aagc')
    Traceback (most recent call last):
    AssertionError: invalid codon


    >>> code.protein('AAGTCGTAGCTACGXXXXGAGAAGGAT')
    Traceback (most recent call last):
    AssertionError: invalid sequence
    '''
    def __init__(self, location:str):
        with open(location, 'r', encoding='utf-8') as reader:
            lines = reader.readlines()

        self.codon_table = {}
        for line in lines:
            codon, amino_acid = line.strip().split()
            self.codon_table[codon.upper()] = amino_acid.upper()


    def amino_acid(self, codon):
        codon = codon.upper()

        codon_dna = codon.replace('U', 'T')
        codon_rna = codon.replace('T', 'U')

        if codon_dna in self.codon_table:
            return self.codon_table[codon_dna]
        if codon_rna in self.codon_table:
            return self.codon_table[codon_rna]

        raise AssertionError("invalid codon")

    def protein(self, sequence:str):
        sequence = sequence.upper().replace('U', 'T')

        assert (
             all(c in "ATCGUatcgu" for c in sequence)
        ), 'invalid sequence'

        def divider(seq:str):
            return [seq[3* i : 3*(i+1)] for i in range(len(seq)//3)]


        return ''.join([self.amino_acid(codon) for  codon in divider(sequence)])


