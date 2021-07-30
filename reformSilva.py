# coding: utf-8

from Bio import SeqIO

###########################################################################
seqlist = [ ln for ln in open('SILVA_138_RefNR99.fasta').readlines() ]
for i in range(0, len(seqlist)):
	ln = seqlist[i]
	if '>' in ln:
		seqlist[i] = ln.replace(' ', '_')
	else:
		seqlist[i] = ln.replace('U', 'T')
open('Silva_138RefNr99_V1.fasta', 'w').writelines(seqlist)

###########################################################################

silva = SeqIO.parse(open('Silva_138RefNr99_V1.fasta'), 'fasta')
new = []
tax = []
for seq in silva:
	if '_Bacteria;' in str(seq.id) or '_Archaea;' in str(seq.id):
		access = str(seq.id).split('_')[0]
		taxon = ' '.join(str(seq.id).split('_')[1:])
		unitLen = len(taxon.split(';'))
		if unitLen == 7:
			genus = taxon.split(';')[5]
			geSp = taxon.split(';')[6]
			if genus == geSp.split(' ')[0] and len(geSp.split(' ')) == 2 and genus != 'uncultured':
				header = '>' + access + '\n'
				sequence = str(seq.seq) + '\n'
				new.append(header + sequence)
				tax.append(access + '\t' +  taxon + '\n')
open('Silva_138RefNr99_V2.fasta', 'w').writelines(new)
open('AccessionTaxonomyDict.txt', 'w').writelines(tax)
