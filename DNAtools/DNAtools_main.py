from DNA_tools.DNAmodules import DNA_to_RNA as A, DNA_cds_trim as C, rev_comp as B
from pathlib import Path

#def fastainput():
#    p = Path.cwd()
#    q = p / 'FastaFiles'
#    opt = input("Enter 'tool#': \n")
#    input_file = input("Enter 'in_file.fasta':  ")
#    output_file = input("Enter 'output_file.fasta': ")
##    e = filein_out.split()
#    if input_file in q.name:
#        Info = q.read_text()
#        in_seq = Info.readlines()[1:]
#    o = q.open("output_file", 'x')
#    outid = o.write(f"{Fasta_id}")
#    if opt == '1':
#        A.TRANSCRIPTION(in_seq)
#
 
#    if opt == '1':
#        A.TRANSCRIPTION_f(in_seq)
#        from DNA_to_RNA import NTS
#        fin = open("output_file", 'a')
#        fin.write(NTS)
#        o.close
#        print("Transcription output .fasta file within the file: '/FastaFiles'")
#
#
#
    
    
    
def prompt():
#    print(Path.cwd())
    Prompt = input("Select the DNA tool you would like to use by typing option then ENTER: \n [1] = DNA Transcription \n [2] = Sequence to Reverse Compliment \n [3] = DNA trimmer to obtain only start - stop cds \n \n [0] = Exit \n OPTION:  ")
    while True:
        if Prompt == '1':
            print("\n ## Transcription tool ## \n")
            A.TRANSCRIPTION()
        elif Prompt == '2':
            print("\n ## Reverse Compliment tool ## \n")
            B.REVERSE_COMP()
        elif Prompt == '3':
            print("\n ## CDS Trimmer tool [NOTE: already trimmed DNA i.e. (start = ATG, END = TAA or TAG or TGA) will return an error ## \n")
            C.TRIMMER()
        elif Prompt == '0':
            print("\n Exiting DNA Tools \n")
            exit()
#        elif Prompt == 'fasta':
#            fastainput()
        else:
            print("\n Unrecognized option, please use options [#] \n")
            prompt()
        

prompt()


