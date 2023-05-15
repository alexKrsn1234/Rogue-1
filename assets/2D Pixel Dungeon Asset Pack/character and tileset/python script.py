from PIL import Image


image= Image.open("Dungeon_Tileset.png")


for i in range(10):
    for j in range(10):
        cropped = image.crop((i*16,j*16,16+i*16,16+j*16))
        cropped.save(str(i)+str(j)+".png")
