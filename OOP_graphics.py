
import curses
import console
import math
import loop
import graphics

visibleAsciiArt = []
staffAsciiArt = []
premiumAsciiArt = []
#allAsciiArt = []
height = 0
width = 0
printMessageToScreen = ''

class AsciiArt(object):

    # art will store the asciiArt
    # name will store the name of the file
    # numberOfLines will store how long each piece of ascii art is
    # startingHeight gives us how high on the screen the image is drawn.
    # When this value is < 2 - numberOfLines, it gets removed from the visibleAsciiArt array
    
	def __init__(self, name, numberOfLines, color):
		global height
		global width

		(width, height) = console.getTerminalSize()

		self.name = name
		self.numberOfLines = numberOfLines
		self.startingHeight = height
		self.currentHeight = height
		self.color = color

		with open(self.name) as f:
			self.art = f.readlines()
		for j in range(len(self.art)):
			self.art[j] = self.art[j].rstrip('\n')

	#def shuffleElements(self, i):
	#	if i == 20 - self.numberOfLines:
	#		moveObjectToBottom()


	def drawArt(self):
		global width

		x = width/6
		y = self.currentHeight
		tempy = self.currentHeight
		idx = 0
		idx2 = self.numberOfLines

		# if element is a set distance above starting point, and staffAsciiArt is not empty
		if (y == (self.startingHeight - self.numberOfLines)) and staffAsciiArt:
			makeStaffElementVisible()
		# if element from premiumAsciiArt is a set distance from where it started and is in the premiumA
		elif (y == (self.startingHeight - self.numberOfLines)) and self in premiumAsciiArt:
			switchToPremiumImages()

		# if image would otherwise be drawn outside (above) the terminal
		if y <= 0:
			tempy = 0
			idx = -y

        # if image would otherwise be drawn outside (below) the terminal
		if y >= height - self.numberOfLines - 1:
			idx2 = height - y

		for idx in range(idx, idx2):
			if y == -self.numberOfLines:
				# so the element is back at the bottom of the page at the end of this function
				self.currentHeight = self.startingHeight
				f = open('consolelog', 'a')
				f.write('self.currentHeight = self.startingHeight has been carried out\n\n')
 				f.close()
				return
			graphics.drawTile(x, tempy, self.art[idx], self.color)
			tempy = tempy + 1

		self.currentHeight = self.currentHeight - 1


#####################################################################################


def init():
	global visibleAsciiArt
	global premiumAsciiArt
	global staffAsciiArt

	wizard = AsciiArt("staff-images/wizard", 15, curses.color_pair(2))

	backflip = AsciiArt("backflip", 4, curses.color_pair(3))
	backflip1 = AsciiArt("backflip", 4, curses.color_pair(3))
	backflip2 = AsciiArt("backflip", 4, curses.color_pair(3))
	backflip3 = AsciiArt("backflip", 4, curses.color_pair(3))

	handstand = AsciiArt("handstand", 4, curses.color_pair(7))
	handstand1 = AsciiArt("handstand", 4, curses.color_pair(7))
	handstand2 = AsciiArt("handstand", 4, curses.color_pair(7))
	handstand3 = AsciiArt("handstand", 4, curses.color_pair(7))

	somersault = AsciiArt("somersault", 4, curses.color_pair(8))
	somersault1 = AsciiArt("somersault", 4, curses.color_pair(8))
	somersault2 = AsciiArt("somersault", 4, curses.color_pair(8))
	somersault3 = AsciiArt("somersault", 4, curses.color_pair(8))

	coffee = AsciiArt("staff-images/coffee", 15, curses.color_pair(5))
	coffee.currentHeight = coffee.currentHeight - coffee.numberOfLines

	hand = AsciiArt("staff-images/hand", 15, curses.color_pair(6))

	boom = AsciiArt("staff-images/boom", 15, curses.color_pair(4))

	peter = AsciiArt("staff-images/peter-pan", 26, curses.color_pair(2))

	shoes = AsciiArt("staff-images/shoes", 10, curses.color_pair(8))

	monkey = AsciiArt("staff-images/monkey", 21, curses.color_pair(6))

	staffAsciiArt = [hand, wizard, boom, peter, shoes, monkey]
	premiumAsciiArt = [handstand, somersault, backflip, handstand1, somersault1, backflip1, handstand2, somersault2, backflip2, handstand3, somersault3, backflip3]
	visibleAsciiArt = [coffee]


def makeStaffElementVisible():
	global visibleAsciiArt
	global staffAsciiArt

	visibleAsciiArt.append(staffAsciiArt[0])
	staffAsciiArt.pop(0)

	f = open('consolelog', 'a')
	f.write('staffAsciiArt.pop(0) has been carried out\n')
	f.write('staffAsciiArt: ' + str(staffAsciiArt) + '\n\n')
 	f.close()


def switchToPremiumImages():  # TODO: need to turn this off if filled with icons already 
	global visibleAsciiArt
	global premiumAsciiArt
	global printMessageToScreen

	f = open('consolelog', 'a')

	premiumAsciiArt[0].currentHeight = premiumAsciiArt[0].startingHeight
	visibleAsciiArt.append(premiumAsciiArt[0])
	premiumAsciiArt.append(premiumAsciiArt[0])
	premiumAsciiArt.pop(0)

	f.write('Item added to visibleAsciiArt\n')
	f.write('visibleAsciiArt: ' + str(visibleAsciiArt) + '\n\n')

 	f.close()

# Sticks the object at the top of the array onto the bottom
def moveObjectToBottom():
	global visibleAsciiArt

	f = open('consolelog', 'a')

	visibleAsciiArt[0].currentHeight = visibleAsciiArt[0].startingHeight
	visibleAsciiArt.append(visibleAsciiArt[0])
	visibleAsciiArt.remove(visibleAsciiArt[0])

	f.write('In moveObjectToBottom\n')
	f.write('visibleAsciiArt ' + str(visibleAsciiArt) + '\n\n')
	f.close()

def removeTopElement():
	global visibleAsciiArt
	visibleAsciiArt.pop(0)