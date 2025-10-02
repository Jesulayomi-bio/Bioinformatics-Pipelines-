# extract a fasta file into dictionary 
def parse_fasta(file_path):
    fasta = open(file_path).read()
    # print(fasta)
    split_fasta = fasta.split("\n")  #split sequence
    header = []  #empty header list
    sequence = []  #empty sequence list +
    for line in split_fasta:    
        if line.startswith(">"):  #remove header from faste
            header.append(line)  
        if not line.startswith(">"):  #remove sequence from fasta 
            sequence.append(line) 
    
    dictionary = {
           }       
    for h in header:
        for s in sequence:
            dictionary[h.replace(">","")] = s   
            
    return dictionary