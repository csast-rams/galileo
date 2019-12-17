import re
def Translation():
    Aminos=\
        {'Ala':['GCT','GCC','GCA','GCG'],\
         'Arg':['CGT','CGC','CGA','CGG','AGA','AGG'],\
         'Asn':['AAT','AAC'],\
         'Asp':['GAT','GAC'],\
         'Cys':['TGT','TGC'],\
         'Glu':['GAA','GAG'],\
         'Gln':['CAA','CAG'],\
         'Gly':['GGT','GGC','GGA','GGG'],\
         'His':['CAT','CAC'],\
         'Ile':['ATT','ATC','ATA'],\
         'Leu':['TTA','TTG','CTT','CTC','CTA','CTG'],\
         'Lys':['AAA','AAG'],\
         'Met(start)':['ATG'],\
         'Phe':['TTT','TTC'],\
         'Pro':['CCT','CCC','CCA','CCG'],\
         'Ser':['TCT','TCC','TCA','TCG','AGT','AGC'],\
         'Thr':['ACT','ACC','ACA','ACG'],\
         'Tyr':['TAT','TAC'],\
         'Trp':['TGG'],\
         'Val':['GTT','GTC','GTA','GTG'],\
         'STOP':['TAA','TAG','TGA']}
    Abv_Abv=\
        {'Ala':'A',\
        'Arg':'R',\
        'Asn':'N',\
        'Asp':'D',\
        'Cys':'C',\
        'Glu':'E',\
        'Gln':'Q',\
        'Gly':'G',\
        'His':'H',\
        'Ile':'I',\
        'Leu':'L',\
        'Lys':'K',\
        'Phe':'F',\
        'Pro':'P',\
        'Ser':'S',\
        'Thr':'T',\
        'Tyr':'Y',\
        'Trp':'W',\
        'Val':'V',\
        'Met(start)':'M',\
        'STOP':'*'}
    #–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    #
    
    IN = input("Input DNA Sequence for amino acid sequence\n>")
    
    DNA = IN.upper()
    
    bp=['A','G','C','T']
    
    seg=[]         # These rows clean up user input, raises Error if N != a,t,g,c
    
    aa_seq=[]
    
    aa_seq_single=[]
    
    for nt in DNA:
        if nt not in bp:
           print("ERROR, INPUT SEQUENCE CONTAINED UNIDENTIFIED BASE")
    seg = re.split("([A-Z]{3})", DNA)
    for obj in seg:
        if obj == '':
            seg.remove(obj)
        elif len(obj) < 3:
            seg.remove(obj)
        
    def aa(seg, list):              # <– Matches codon to AA {AA=key,codon=value}   
        for codon in seg:           #   Make Sure the Input(DNA->seg)Loops First{e.g. if "for k, v … " came first, then the final append order would be wrong
            for k, v in Aminos.items():
                if codon in v:
                    list.append(k)  #<– directs the AA abrv. to a new list
    aa(seg, aa_seq)                 
    
    AA = '-'.join(aa_seq)       #<–Links the AA chain with "–"
    
    def smol_boi(aa_seq, list):
        for Amino in aa_seq:
            for k, v in Abv_Abv.items():
                if Amino == k:
                    list.append(v)
    
    smol_boi(aa_seq, aa_seq_single)
    
    AA_s = ''.join(aa_seq_single)
    
    prompt = input("Output options:\n[1]: single letter abreviation\n[2]: 3-letter abreviation\n[0]: exit\nOPTION -> ")
    if prompt == '1':
    	print(AA_s)
    elif prompt == '2':
    	print(AA)
    elif prompt == '3':
    	print(AA)
    elif prompt == '':
    	print(AA_s)
    elif prompt == '0':
    	print("Exiting Amino Acid Translator...")
    	EXIT()