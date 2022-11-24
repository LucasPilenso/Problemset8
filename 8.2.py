from Bio import SeqIO
import sys

filename = sys.argv[1]
for info in  SeqIO.parse(filename , 'fasta'):
	sequence = info.seq
	print('\n', info.id , ':')
	for i in range(0 , len(sequence), 3):
		print(sequence[i:i+3] , end = ' ')
