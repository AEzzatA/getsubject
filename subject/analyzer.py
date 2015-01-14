import os
import sys
import nltk
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.tag.stanford import NERTagger

nltk.data.path.append('./nltk_data/')

class POSTagger(object):
	'''Class that holds POS tagger methods:
	it should be used like this
	obj = POSTagger(sentence)
	obj.processText()
	obj.printPOS()
	'''
	def __init__(self, text):
		self.text = nltk.word_tokenize(text)
		self.tagged_text = []
		self.result = []

	def processText(self):
		self.tagged_text = nltk.pos_tag(self.text)
		return self.tagged_text

	def getSubject(self):
		for (word, tag) in self.tagged_text:
			if tag == 'NNP':
				self.result.append(word)
		if len(self.result) == 0:
			for (word, tag) in self.tagged_text:
				if tag == 'NN':
					self.result.append(word)

		return self.result

	def printPOS(self):
		print("result is: " , self.result)



class NERTag(object):
	'''Class that holds NER tagger methods:
	it should be used like this
	obj = NERagger(sentence)
	obj.processNER()
	obj.printPOS()
	'''

	def __init__(self, text):
		self.text = nltk.word_tokenize(text)
		self.tagged_text = []
		self.result = []
		self.CLASSIFIERJAR = os.path.join(os.getcwd(), 'stanford-ner-2014-08-27/classifiers/english.all.3class.distsim.crf.ser.gz')
		self.NERJAR = os.path.join(os.getcwd(), 'stanford-ner-2014-08-27/classifiers/english.all.3class.distsim.crf.ser.gz')

	def processNER(self):
		'''Get NER output'''
		#path = self._connectToNER() #Get NER working path
		st = NERTagger(self.CLASSIFIERJAR, self.NERJAR) #Starting connection to NER
		return st.tag(self.text)

	def getSubject(self):
		for (word, tag) in self.tagged_text:
			if tag == 'LOCATION' or tag == 'PERSON':
				self.result.append(str(word))
		return self.result

	def printNER(self):
		print("result is" ,self.result)




def getInput():
	'''Return the input string passed to the program'''
	return sys.argv[1]


def printTests():
	a = TestStrings()
	for x in a.testList():
		pos = POSTagger(x)
		pos.processText()
		pos.getSubject()
		pos.printPOS()
		#print("Sentence:", x, "result is" ,getSubject(tag_list))

'''
if __name__ == '__main__':
	a = getInput()
	print a
	pos = POSTagger(a)
	pos.processText()
	pos.getSubject()
	pos.printPOS()
'''
