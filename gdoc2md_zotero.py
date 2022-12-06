#!/usr/bin/env python3

#created by Tyler Laird on 12-05-2022

import sys
import re

filename = sys.argv[1]

with open(filename,'r') as infile:
    filetext = infile.read()

#regex to identify all citations in the text
citations = re.findall("ITEM CSL_CITATION.+?}}]}", filetext)

#parsing the individual citations to extract the citation-key
#the citation key is linked to the zotero library on your local computer
#for my usage the citation key is in the BetterBibTex format
#the citation key is then modified to be a markdown style in-text citation that can be swapped with the original citation

master_output_list=[]
for c in citations:
    entries = re.findall('"citation-key":".+?"', c)
    output_citation_list=[]
    for e in entries:
        e1=re.sub('"citation-key":"','@',e)
        e1=e1[0:-1]
        output_citation_list.append(e1)
    output= "["+"; ".join(output_citation_list)+"]"
    print(output)
    master_output_list.append(output)

swap_dict= dict(zip(citations,master_output_list))

output_text = re.sub("ITEM CSL_CITATION.+?}}]}", lambda x: swap_dict[x.group()], filetext)
with open("gdoc2md_"+filename, "w") as outfile:
    outfile.write(output_text)
