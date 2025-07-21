'''Problem from rosalind.info. The goal is pretty simple: given a DNA string t, 'transcribe' to an 
RNA string u by replacing all occurrences of 'T' in t with 'U' in u.'''

from Bio import SeqIO
import sys
import os

#read in the input fasta file
fastafile = input("Enter path to your input (DNA) fasta file: ")
#check that its a valid file type
if fastafile.endswith(".fasta") == False:
    sys.exit("Please enter a valid file name, ending with .fasta")
#check that the input file exists
if os.path.exists(fastafile) == False:
    sys.exit("Please enter a valid path, if input file is in this directory, just enter the 'filename.fasta'")

#read in the output file name (will create a file if it doesn't already exist, don't need to check path)
outputfile = input("Enter name of your output file (include .fasta ending): ")
#check that its a valid file type
if outputfile.endswith(".fasta") == False:
    sys.exit("Please enter a valid file name, ending with .fasta")

with open(outputfile, "w") as fastaout:
    for seq_record in SeqIO.parse(fastafile, "fasta"):
        rna_seq = str((seq_record.seq.replace("T", "U")))
        fastaout.write(">" + seq_record.id + "U" + "\n" + rna_seq + "\n")

#Alrighty!