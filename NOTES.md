## Learning process:
Here is how I built up the tool, starting with a sample string, then list, then moving to fasta files. 
Only interesting if you want to see the learning process. 

Problem from rosalind.info. The goal is pretty simple: given a DNA string t, 'transcribe' to an 
RNA string u by replacing all occurrences of 'T' in t with 'U' in u.
I build upon this as we go, and end up creating a user interface to read in DNA sequences as a fasta
and output RNA sequences as a new fasta.

## import necessary packages
```python
#using biopython to get the SeqIO.parse() method for reading fasta files

from Bio import SeqIO

#using sys for sys.exit('error message') if user input is invalid

import sys

#using os for os.path.exists(path) to make sure user input file exists

import os
```

## Start with the sample string:

```python
t = "GATGGAACTTGACTACGTAAATT"

#lets use the replace() method, which takes arguments (find, replace)

u = t.replace("T", "U")

print(u)
```

## Now try a sample list:

Now let's see if we can do it with a list of sequences. 
Note, we can't just use replace() on a list, so instead we'll iterate through the list and apply replace() to each element in the list.

```python
tlist = ["GATGGAACTTGACTACGTAAATT", "GTTGATGGAACTTGACTACGTAAATT", "GATGGAACTTGACTACGTAAATTGTTC"]
ulist = []

#we'll need to append to ulist in this loop rather than overwrite (ie ulist.append() rather than ulist =).

for seq in tlist:
    ulist.append(seq.replace("T", "U"))

print(ulist)
```

## Now lets use a fasta file input
still pretty easy, maybe we can now do a fasta file

```python
fastafile = "rosalind.fasta"

fasta_u = []

#we'll use the SeqIO.parse() function, which takes a file name and a file type and returns an iterable from that file.

for seq_record in SeqIO.parse(fastafile,"fasta"):
    print(seq_record.id)
    fasta_u.append(seq_record.seq.replace("T", "U"))

print(fasta_u)
```

## Now let's see if we can instead write this to another fasta file.

```python
with open("output.fasta", "w") as fastaout:
    for seq_record in SeqIO.parse(fastafile, "fasta"):
        rna_seq = str((seq_record.seq.replace("T", "U")))
        fastaout.write(">" + seq_record.id + "U" + "\n" + rna_seq + "\n")
```

## Awesome! Now lets make the whole thing interactive: (see transcribe.py)
