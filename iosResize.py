#Resize iTunes Artwork using the PIL image library
#free from : http://www.pythonware.com/products/pil/index.htm
#Tested on python version 2.7.1
#Author Lar Judge 
#Email lar@larjudge.com
#GitHub https://github.com/larjudge

import Image

#define all the different sizes for the various icons. They are all square.
sizesAndNames = { 57 : "Icon", 
                  114 : "Icon@2x", 
                  72 : "Icon-72", 
                  29 : "Icon-Small", 
                  58 : "Icon-Small@2x", 
                  50 : "Icon-Small-50"}

#open the iTunes Artwork File as the base Icon to resize (512 x 512)
imageFile = "iTunesArtwork.png"
im0 = Image.open(imageFile)
ext = ".png"

#Copy the image to the neccessary size
#save the newly created image
def resizeAndWrite(sizeAndName) :
    im = im0.resize((sizeAndName[0], sizeAndName[0]), Image.ANTIALIAS)
    im.save(sizeAndName[1] + ext)

#Call the resizeAndWrite func on all image sizes and names
map(resizeAndWrite, sizesAndNames.items());