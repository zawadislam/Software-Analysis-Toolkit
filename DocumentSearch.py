import docx


doc = docx.Document("C:\\Users\\zislam\\Downloads\\SDP V1 ALL K0000064476 redlines accepted")
paras = [p.text for p in doc.paragraphs if p.text]

print(f'=== Output type is a {type(paras)} of {type(paras[1])} \ntotal length is {len(paras)} ===') 
'''
=== Output type is a <class 'list'> of <class 'str'> 
total length is 25 ===
'''