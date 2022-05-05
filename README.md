# Reference Extractor

Use this tool to extract text references from a PDF of an academic paper.

`pip install pdfminer`
`python3 extract_references.py -f <filename>`

Assumes:
- the file is in the same directory as extract_references.py
- the references are contained in a section called References, which is 
followed by a section called Appendix (or by nothing)
