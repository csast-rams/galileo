#import re
import os

#def fastainput(filename):
#    
#def fastaread():
#    

def TRIMMER():
    User = input("DNA sequence:")
    preseq = ''
    for nt in User:
        if nt == "U":
            preseq = preseq + "T"
        elif nt == "u":
            preseq = preseq + "t"
        else:
            preseq = preseq + nt
    sequence = preseq.upper()
    import re
    start = re.compile("ATG")
    search_str = sequence
    seqsearch = start.search(search_str)
    seqstart = seqsearch.start()
    seq = sequence[seqstart:-1]
    def trimmed():
      stops = re.compile("TAA|TAG|TGA")
      search_str = seq
      matchedEND = stops.search(search_str)
      endex = matchedEND.start() + 3
      print(f"\n {seq[0:endex]}")
    trimmed()

#def translation(trimmed()):
#    x = ''
#    y = ''
#    z = ''
    


  
  
#AGTAAGAAGGAAGAGAGAGAGAGGGGATGCCCGAGAGAGAGAGAGAGAGAGAGAGAGAGAGAGAGACTAGGGCACAC
    


