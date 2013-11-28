
import curses
import console
import math
import loop
import graphics
import OOP_graphics

currentText= []
allText = []
height = 0
width = 0

class Text(object):

	# name will store the name of the file
	
	def __init__(self, name):
		global height, width

		(width, height) = console.getTerminalSize()

		self.name = name
		self.startingHeight = height - 1

		with open(self.name) as f:
			self.text = f.readlines()
		for i in range(len(self.text)):
			self.text[i] = self.text[i].rstrip('\n')


	def drawText(self):
		global height, width

		color = curses.color_pair(8)

		x = (2*width)/3
		# y = self.startingHeight # Where the box is placed vertically
		y = 0
		idx = 0
		numLines = height
		for idx in range(numLines):
			if len(self.text)-1 <= idx:
				break
			graphics.drawTile(x, y, self.text[idx], color)
			y = y + 1


###########################################################


def init():
	global currentText
	global allText
	global height

	staff = Text("staff", )
	premiumDonators = Text("premiumDonators")
	scum = Text("scum")

	allText= [premiumDonators, scum]
	currentText = [staff]


def changeVisibleText():
	global allText
	global currentText

	currentText.append(allText[0])
	currentText.pop(0)
	allText.append(allText[0])
	allText.pop(0)