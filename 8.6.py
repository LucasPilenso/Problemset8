from Bio import SeqIO
import sys

filename=sys.argv[1]

with open ('Python_08.codons-6frames.nt', 'w') as file:
	for info in  SeqIO.parse(filename , 'fasta'):
		sequence = info.seq
		sequence_rc = info.seq.reverse_complement()
		file.write('{}{} {}\n'.format('\n', info.id , 'reading frame 1:'))
		for i in range(0 , len(sequence), 3):
			file.write('{}{}'.format(sequence[i:i+3] , ' '))
		file.write('{}{} {}\n'.format('\n', info.id , 'reading frame 2:'))
		for i in range(0 , len(sequence), 3):
			file.write('{}{}'.format(sequence[i+1:i+4] , ' '))
		file.write('{}{} {}\n'.format('\n', info.id , 'reading frame 3:'))
		for i in range(0 , len(sequence), 3):
			file.write('{}{}'.format(sequence[i+2:i+5] , ' '))
		sequence_rc = info.seq.reverse_complement()
		file.write('{}{} {}\n'.format('\n', info.id , 'reverse complement reading frame 1:'))
		for i in range(0 , len(sequence_rc), 3):
			file.write('{}{}'.format(sequence[i:i+3] , ' '))
		file.write('{}{} {}\n'.format('\n', info.id , 'reverse complement reading frame 2:'))
		for i in range(0 , len(sequence_rc), 3):
			file.write('{}{}'.format(sequence[i+1:i+4] , ' '))
		file.write('{}{} {}\n'.format('\n', info.id , 'reverse complement reading frame 3:'))
		for i in range(0 , len(sequence_rc), 3):
			file.write('{}{}'.format(sequence[i+2:i+5] , ' '))

with open('Python_08.translated_aa.fasta','w') as arquivo: 
	for info in  SeqIO.parse(filename , 'fasta'):
		sequence = info.seq
		sequence_rc = info.seq.reverse_complement()
		protein1 = sequence.translate(to_stop = True)
		protein2 = sequence[1:-1].translate(to_stop = True)
		rc_protein1 = sequence_rc.translate(to_stop = True)
		protein3 = sequence[2:-1].translate(to_stop = True)
		rc_protein2 = sequence_rc[1:-1].translate(to_stop = True)
		rc_protein3 = sequence_rc[2:-1].translate(to_stop = True)
		arquivo.write('>{} {}\n{}\n'.format(info.id , 'reading frame 1 translates into:', protein1))
		arquivo.write('>{} {}\n{}\n'.format(info.id , 'reading frame 2 translates into:', protein2))
		arquivo.write('>{} {}\n{}\n'.format(info.id , 'reading frame 3 translates into:', protein3))
		arquivo.write('>{} {}\n{}\n'.format(info.id , 'reverse complement reading frame 1 translates into:', rc_protein1))
		arquivo.write('>{} {}\n{}\n'.format(info.id , 'reverse complement reading frame 2 translates into:', rc_protein2))
		arquivo.write('>{} {}\n{}\n'.format(info.id , 'reverse complement reading frame 3 translates into:', rc_protein3))

from collections import OrderedDict

frames = []
max_frames= []
lista = []
def remove_reps(lista):
	return list(OrderedDict.fromkeys(lista))

with open('Python_08.translated-longest.aa', 'w') as arq:
	with open('Python_08.translated_aa.fasta', 'r') as peptideos:
		for info in SeqIO.parse(peptideos, 'fasta'):
			id =info.id
			s = info.seq
			lista.append(id)
			frames.append(s)
		n=6
		output=[frames[i:i + n] for i in range(0, len(frames), n)]
		for x in output:
			max_frames.append(max(x))
		p = 0
		while p < len(max_frames):
			arq.write('{}:\n'.format(remove_reps(lista)[p]))
			arq.write('{}\n'.format(max_frames[p]))
			p +=1

