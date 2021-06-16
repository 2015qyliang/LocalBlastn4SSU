# conding: utf-8
# email: qfsfdxlqy@163.com
# GitHub: https://github.com/2015qyliang

from bs4 import BeautifulSoup
import chardet
import os

def getInforLine(EzHtml):
	summaryLPSN = []
	html = open(EzHtml, 'rb').read()
	soup = BeautifulSoup(html, 'html.parser')
	partAs = soup.find_all('td', {'class':'dt-center'})
	partBs = soup.find_all('td', {'class':'dt-head-center'})
	linesNum = len(partBs)
	for ln in range(linesNum):
		accessIndex = 1 + 4*ln
		taxonIndex = 2 + 4*ln
		strainIndex = 3 + 4*ln
		Accession = partAs[accessIndex].text
		Taxon = partAs[taxonIndex].text
		if len(partAs[strainIndex].text) > 2:
			Strain = partAs[strainIndex].text.replace(' ', '_')
		else:
			Strain = 'NA'
		Taxonomy = partBs[ln].text
		taxLine = '\t'.join([Accession, Taxon, (Strain.encode('ascii', 'ignore')).decode('ascii', 'ignore'), Taxonomy]) + '\n'
		summaryLPSN.append(taxLine)
	return summaryLPSN

startNum = 0
files = [fn for fn in os.listdir('C:/Users/lqy/Downloads/') if '.html' in fn]
open('AccessionTaxonomyDict.txt', 'w')
for fn in files[startNum:]:
	print('-- Ongoing', fn, '--', files.index(fn) + 1, '--')
	EzHtml = 'C:/Users/lqy/Downloads//' + fn
	taxInfor = getInforLine(EzHtml)
	open('AccessionTaxonomyDict.txt', 'a').writelines(taxInfor)
	print('-- Done', fn, '--', files.index(fn) + 1, '--')

print('-----------------------------DONE-----------------------------')

