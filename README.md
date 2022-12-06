# WorkflowBin

This is a repository that conatins various scripts I have made for productive workflows

# gdoc2md_zotero.py

Problem: You recently learned about time-saving document writing workflows but currently are using google docs with zotero.
You would like start writing in markdown but don't want to redo the placement of in-text citations.

Solution: This script enables conversion of a google doc with zotero citations to a markdown doc with zotero citations

1. in the google doc, you must use the "Switch word Processors" function in the Zotero tab

2. copy and paste the generated text into a plain text file (let's say: "googledoc.txt"

3. run the command gdoc2md_zotero.py googledoc.txt

The result is a textfile: gdoc2md_googledoc.md that contains the reformatted citations in markdown format for use with the same zotero library

Note: This conversion does not preserve any sort of formating from the original google doc and is mainly to preserve citations. 
