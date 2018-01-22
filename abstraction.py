class Document:
	def __init__(self,name):
		self.name = name 

class Pdf(Document):
	def show(self):
		return "Show pdf contents"

class Word(Document):
	def show(self):
		return "Show Word Contents"

documents = [Pdf('Document1'),Pdf('Document2'),Word('Document3')]

for doc in documents:
	print doc.show() 
