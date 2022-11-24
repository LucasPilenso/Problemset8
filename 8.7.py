import re

outfh = open("Python_08.translatedx.aa", "w")
outfh2 = open("Python_08.translated-longesttx.aa", "w")
outfh3 = open("Python_08.orf-longest.nt", "w")

	for k in fw_rev_codons:
		outfh.write(k+"\n")
		sequence = fw_rev_codons[k]
		prot_seq = translate_dna_to_aa(sequence)
		outfh.write(prot_seq)
		outfh.write("\n")

		longest_match = ""
		outfh2.write(k+"\n")
	for match in re.finditer(r"M.*?_", prot_seq):
		stop = int(match.end())
		start = int(match.start())
		if (stop - start) > len(longest_match):
			longest_match = match.group()
			stop = int(match.end()) #get the NEW end
			start = int(match.start()) #get updated start
            
			joined = "".join(sequence) #gets codons in a string, not list
            
		outfh3.write(k + "\n") #write key
		outfh3.write(joined[start*3:(stop*3)]) #write orf
		outfh3.write("\n")

        outfh2.write(longest_match+"\n")
 

outfh.close()
outfh2.close()
outfh3.close()
