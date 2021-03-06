# hw8pr1.py
# Lab 8
#
# Name:
#

# keep this import line...
from cs5png3 import *
from math import log, log2
import colorsys



def inMSet(c,n):
	"""Takes a complex number, c, and a number if iterations, n, and checks to see if c
	is in the Mandelbrot Set"""
	z = 0 + 0j

	for i in range(n):
		z = z**2+c

		if abs(z) > 2: 
			return False	
	return True


def jSet(z, c, max):
	max = 100
	n = 0
	while abs(c) <= 2 and n < max:
		c = c*c + z
		n += 1
	if n == max:
		return max
	return n + 1 - log(log2(abs(c)))

def hsv2rgb(h,s,v):
	return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def zoom(xMinMax, yMinMax, factor):
	xMin, xMax = xMinMax
	yMin, yMax = yMinMax
	x, y = ((xMin + xMax)/2 ,(yMin + yMax) / 2)

	print("Center: " + str((x,y)))
	x = x - (0.1 * x)
	y = y - (0.1 * y)


	return xMin - (0.1 * x), xMax + (0.1 * x), yMin - (0.1 * y) ,yMax + (0.1 * y)

				

def weWantThisPixel(col, row):
	""" a function that returns True if we want
		 the pixel at col, row and False otherwise
	"""

	#Instead of only placing a mark when both are true, it will do it when either
	#are true. This means it will draw not only the nodes (dots) but also the horizontal
	#and vertical lines
	if col%10 == 0  or  row%10 == 0:
		return True
	else:
		return False


def scale(pix, pixMax, floatMin, floatMax):
	""" scale accepts
			pix, the CURRENT pixel column (or row)
			pixMax, the total # of pixel columns
			floatMin, the min floating-point value
			floatMax, the max floating-point value
		scale returns the floating-point value that
			corresponds to pix
	"""

	if pix == pixMax: return floatMax
	elif pix == 0: return floatMin
	else:
		pixFraction = float(pix)/float(pixMax)
		total = abs(floatMin) + abs(floatMax)
		floatFraction = (total*pixFraction)+(floatMin)
		return floatFraction


def mset():
	""" creates an image or set of images of the Julia set
		specified by "a"
	"""
	width = 1200
	height = 800
	image = PNGImage(width, height)
	FRAMES = 1
	NUMITER = 200  # of updates, from above
	XMIN = -0.5   # the smallest real coordinate value
	XMAX =  0.5  # the largest real coordinate value
	YMIN = -0.5  # the smallest imag coordinate value
	YMAX =  0.5   # the largest imag coordinate value
	a = -1.476 + 0.0j 	  #Z value for use in Julia set -> x & y should be between -2 and 2


	
	for aCount in range(FRAMES):
		#a = a + aCount/100000
		
		#XMIN, XMAX, YMIN, YMAX = zoom((XMIN, XMAX), (YMIN, YMAX), 0.1)

		print("Y: " + str((YMIN, YMAX)))
		print ("X: " + str((XMIN, XMAX)))

		# create a loop in order to draw some pixels
		for col in range(width):
			for row in range(height):
				
				#   scale to create the real part of c (x)
				x = scale(col, width, XMIN, XMAX)
				
				#   scale to create the imag. part of c (y)
				y = scale(row, height, YMIN, YMAX)

				c = x + (y * 1j)
				# THEN, test if it's in the M. Set:

				#get count before excape velocity > 2
				color = jSet(a, c, NUMITER)
				
				#convert to HSV color value
				hue = int(255 * color / NUMITER)
				saturation = 100
				value = 100 if color < NUMITER else 0
				
				#convert HSV to RGB
				val = hsv2rgb(hue/100, saturation/100, value/100)

				#Use info from above to draw pixel
				image.plotPoint(col, row, val)
				

		# we looped through every image pixel; now write the file
		image.saveFile(str(aCount) + ".png")



#This runs the main function -> you may want to remove this:
mset()