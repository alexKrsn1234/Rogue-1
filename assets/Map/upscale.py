import os
from PIL import Image
     
# assign directory
directory = './'
a=0
# iterate over files in
# that directory
for filename in os.listdir(directory):
    if(not(filename == "upscale.py")):
        im = Image.open(filename)
        rgb_im = im.convert('RGB')
        img = Image.new('RGB', (48,48), color = 'red')
        pixels = img.load()
        for i in range(16):
            for j in range(16):
                r, g, b = rgb_im.getpixel((i, j))
                for k in range(3):
                    for l in range(3):
                        pixels[i*3+k,j*3+l]=(r,g,b)
        img.save('ground'+str(a)+'.png')
        a+=1
