# Simple reverse_compliment generator
def REVERSE_COMP():
#STOP = ("Press 0 to END:")
    seq = input("Enter DNA sequence:" '\n')
    rev = (f'{seq}')[::-1]
    revcomp = ''
    for nt in rev:
        if nt == 'A':
            revcomp = revcomp + 'T'
        elif nt == 'T':
            revcomp = revcomp + 'A'
        elif nt == 'G':
            revcomp = revcomp + 'C'
        elif nt == 'C':
            revcomp = revcomp + 'G'
        elif nt == 'N':
            revcomp = revcomp + nt
        else:
            print('Unrecognized dNT...')
            exit()
    print('\n''Reverse compliment:' '\n' f'{revcomp}'"\n")
