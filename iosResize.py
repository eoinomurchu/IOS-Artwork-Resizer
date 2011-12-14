#Resize iTunes Artwork using the PIL image library
#free from : http://www.pythonware.com/products/pil/index.htm
#Tested on python version 2.7.1
#Author Lar Judge 
#Email lar@larjudge.com
#GitHub https://github.com/larjudge

import Image

#open the iTunes Artwork File as the base Icon to resize (512 x 512)
imageFile = "iTunesArtwork.png"
im0 = Image.open(imageFile)

#define all the different sizes for the various icons. They are all square.
size1 = 57
size2 = 114
size3 = 72
size4 = 29
size5 = 58
size6 = 50

#Copy the image to the six neccessary sizes
im1 = im0.resize((size1, size1), Image.ANTIALIAS)
im2 = im0.resize((size2, size2), Image.ANTIALIAS)
im3 = im0.resize((size3, size3), Image.ANTIALIAS)
im4 = im0.resize((size4, size4), Image.ANTIALIAS)
im5 = im0.resize((size5, size5), Image.ANTIALIAS)
im6 = im0.resize((size6, size6), Image.ANTIALIAS)

#save the newly created images
ext = ".png"
im1.save("Icon" + ext)
im2.save("Icon@2x" +ext)
im3.save("Icon-72" +ext)
im4.save("Icon-Small" +ext)
im5.save("Icon-Small@2x" +ext)
im6.save("Icon-Small-50" +ext)
