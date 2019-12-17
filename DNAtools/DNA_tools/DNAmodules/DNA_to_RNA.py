import re

    
def TRANSCRIPTION():
    prompt = input("[1] = DNA to RNA \n[2] = RNA to DNA \n Option:  ")
    option = int(prompt)
    Seq = input("Enter sequence:  " )
    seq = Seq.upper()
    NTS = ''
    if option == 1:
        for nt in seq:
            if nt == 'T':
                NTS = NTS + 'U'
            else:
                NTS = NTS + nt
        print(f"\n > {NTS}")
    elif option == 2:
        for nt in seq:
            if nt == 'U':
                NTS = NTS + 'T'
            else:
                NTS = NTS + nt
        print(f"\n > {NTS}")
