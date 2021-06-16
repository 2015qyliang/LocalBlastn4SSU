# conding: utf-8
# email: qfsfdxlqy@163.com
# GitHub: https://github.com/2015qyliang

import requests
from time import sleep
import re

startNum = 0
acList = [line.split('\t')[0] for line in open('AccessionTaxonomyDict.txt').readlines()]
for accession in acList[startNum:]:
	header = '>' + accession + '\n'
	EZhtml = requests.get('https://www.ezbiocloud.net/16SrRNA?ac=' + accession)
	if EZhtml.status_code == 200:
		if 'data-clipboard-text=">' in EZhtml.text and 'i>Sequence<' in EZhtml.text:
			tmpseq = re.findall('(data-clipboard-text=">)(.{200,5000})(i>Sequence<)', EZhtml.text)[0][1]
			seq = tmpseq.split('&#10;')[1].split('"><')[0] + '\n'
			open('EzBio16S.fasta', 'a').write(header + seq)
			print('- Accession -', accession)
			print('--  Order  --', acList.index(accession) + 1)
			sleep(0.2)
