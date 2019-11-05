import Graphics.Tiff 
im = Graphics.Tiff.load("my_image.tiff")

import Graphics.Bmp
image = Graphics.Bmp.load("bashful.bmp")

import Graphics.Jpeg as Jpeg
image = Jpeg.load("doc.jpeg")

from Graphics import Png
image = Png.load("dopey.png")

from Graphics import Tiff as picture
image = picture.load("grumpy.tiff")

from Graphics.Convert.jpeg2png import convert as jpeg2png
jpeg2png('my_image.jpeg')

from Graphics import *

Bmp.load('foo')
Jpeg.load('oop')
Tiff.load('007')
