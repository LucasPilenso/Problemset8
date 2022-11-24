from Bio import SeqIO
import sys

filename = sys.argv[1]
for info in  SeqIO.parse(filename , 'fasta'):
	sequence = info.seq
	sequence_rc = info.seq.reverse_complement()
	print('\n', info.id , 'reading frame 1:')
	for i in range(0 , len(sequence), 3):
		print ( sequence[i:i+3] , end = ' ')
	print('\n', info.id , 'reading frame 2:')
	for n in range(0 , len(sequence), 3):
		print ( sequence[n+1:n+4] , end = ' ')
	print('\n', info.id , 'reading frame 3:')
	for x in range(0 , len(sequence), 3):
		print ( sequence[x+2:x+5] , end = ' ')
	print('\n', info.id , 'reverse complement reading frame 1:')
	for i in range(0 , len(sequence_rc), 3):
		print ( sequence_rc[i:i+3] , end = ' ')
	print('\n', info.id , 'reverse complement reading frame 2:')
	for n in range(0 , len(sequence_rc), 3):
		print ( sequence_rc[n+1:n+4] , end = ' ')
	print('\n', info.id , 'reverse complement reading frame 3:')
	for x in range(0 , len(sequence_rc), 3):
		print ( sequence_rc[x+2:x+5] , end = ' ')

