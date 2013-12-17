
import ascii
import graphics
import text
import re
import sys
import console


class Build(object):

	def __init__(self, textFilenames):
		self.textFilenames = textFilenames
		self.text = []
		self.createdText = []
		open('actualText', 'w').close()
		self.build()


	def build(self):

		(width, height) = console.getTerminalSize()

		h = open('actualText', 'a')

		for k in range(height - 18):
			h.write(' '.ljust(50) + '\n')

		with open(self.textFilenames) as f:
			self.text = f.readlines()

		for i in range(len(self.text)):

			try:
				numberOfLines = ascii.allAsciiArt[i].numberOfLines
				for j in range(numberOfLines - 1):
					h.write(' '.ljust(50) + '\n')
				text = re.sub(';', '\n', self.text[i])
				h = open('actualText', 'a')
				h.write(text)

			except:
				h.close()

		h.close()


# ----------------------------------------------------------------------------

graphics.init()
Build('staff')