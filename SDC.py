from PIL import Image, ImageOps
from pathlib import Path
import os
import json


inputFolder = os.path.dirname(os.path.realpath(__file__)) + "/input/"
outputFolder = os.path.dirname(os.path.realpath(__file__)) + "/output/"
tileData = os.path.dirname(os.path.realpath(__file__)) + "/tileData/"
overlayImage = Image.open(Path(os.path.dirname(os.path.realpath(__file__)) + "/overlay.png"))


if os.path.isfile("tilePath.json"):
    with open("tilePath.json", "r") as read_file:
        tilePath = json.load(read_file)
else:
    tilePath = Path(input('Please input the path to your Starbound/tiled/packed directory: '))
    with open("tilePath.json", "w") as write_file:
        json.dump(str(tilePath), write_file)


if os.path.isfile("objectPath.json"):
    with open("objectPath.json", "r") as read_file:
        objectPath = json.load(read_file)
else:
    objectPath = Path(input('Please input the path to your Starbound/assets/_unpacked/objects directory: '))
    with open("objectPath.json", "w") as write_file:
        json.dump(str(objectPath), write_file)


tiles = {
    (32, 32, 32, 255) : Path(str(tilePath) + "/miscellaneous/11.png"),#Air
    (255, 0, 220, 255) : Path(str(tilePath) + "/miscellaneous/01.png"),#Magic Pink Brush
    #(0, 0, 0, 255) : Path(str(tilePath) + "/miscellaneous/02.png"),#Invisible Wall (boundary)
    (85, 255, 0, 255) : Path(str(tilePath) + "/miscellaneous/03.png"),#Player start
    (120, 120, 120, 255) : Path(str(tilePath) + "/miscellaneous/04.png"),#World gen must contain air
    #(0, 0, 0, 255) : Path(str(tilePath) + "/miscellaneous/05.png"),#World gen must contain solid
    (34, 102, 0, 255) : Path(str(tilePath) + "/miscellaneous/06.png"),#Biome item
    (26, 77, 0, 255) : Path(str(tilePath) + "/miscellaneous/07.png"),#Biome tree
    (128, 128, 128, 255) : Path(str(tilePath) + "/miscellaneous/08.png"),#Surface1
    (100, 100, 100, 255) : Path(str(tilePath) + "/miscellaneous/08.png"),#Surface1
    (204, 186, 143, 255) : Path(str(tilePath) + "/miscellaneous/08.png"),#Surface1
    (204, 176, 143, 255) : Path(str(tilePath) + "/miscellaneous/08.png"),#Surface1
    (143, 186, 204, 255) : Path(str(tilePath) + "/miscellaneous/09.png"),#Surface2
    (143, 176, 204, 255) : Path(str(tilePath) + "/miscellaneous/09.png"),#Surface2
    (177, 204, 143, 255) : Path(str(tilePath) + "/miscellaneous/10.png"),#Surface3
    (177, 194, 143, 255) : Path(str(tilePath) + "/miscellaneous/10.png"),#Surface3
    (48, 48, 48, 255) : Path(str(tilePath) + "/miscellaneous/11.png"),#Air overwriteable
    (255, 168, 0, 255) : Path(str(tilePath) + "/miscellaneous/12.png"),#Red connector
    (0, 255, 186, 255) : Path(str(tilePath) + "/miscellaneous/13.png"),#Yellow connector
    (168, 255, 0, 255) : Path(str(tilePath) + "/miscellaneous/14.png"),#Green connector
    (0, 38, 255, 255) : Path(str(tilePath) + "/miscellaneous/15.png"),#Blue connector
    (0, 0, 0, 255) : Path(str(tilePath) + "/miscellaneous/16.png"),#World gen must contain air background
    (255, 255, 255, 255) : Path(str(tilePath) + "/miscellaneous/17.png")#World gen must contain solid background
    #(0, 0, 0, 255) : Path(str(tilePath) + "/miscellaneous/18.png"),#Invisible Wall (structure)
    #(0, 0, 0, 255) : Path(str(tilePath) + "/miscellaneous/19.png"),#Underwater boundary
    #(0, 0, 0, 255) : Path(str(tilePath) + "/miscellaneous/20.png"),#Zero g
    #(0, 0, 0, 255) : Path(str(tilePath) + "/miscellaneous/21.png"),#Zero g protected
    #(0, 0, 0, 255) : Path(str(tilePath) + "/miscellaneous/22.png"),#World gen must contain liquid
    #(0, 0, 0, 255) : Path(str(tilePath) + "/miscellaneous/23.png"),#World gen must not contain liquid
}
            
tilesBackground = {
    (200, 200, 200, 255) : Path(str(tilePath) + "/miscellaneous/08.png"),#Surface1
    (255, 232, 178, 255) : Path(str(tilePath) + "/miscellaneous/08.png"),#Surface1
    (255, 222, 178, 255) : Path(str(tilePath) + "/miscellaneous/08.png"),#Surface1
    (178, 232, 255, 255) : Path(str(tilePath) + "/miscellaneous/09.png"),#Surface2
    (178, 222, 255, 255) : Path(str(tilePath) + "/miscellaneous/09.png"),#Surface2
    (222, 255, 178, 255) : Path(str(tilePath) + "/miscellaneous/10.png"),#Surface3
    (222, 245, 178, 255) : Path(str(tilePath) + "/miscellaneous/10.png"),#Surface3
}

platforms = {}
objects = {}


class StarObject:
    def __init__(self, name, image, x_offset, y_offset, flipped):
        self.name = name
        self.image = image
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.flipped = flipped


def convert():
    for tileFile in os.listdir(tileData):
        with open(tileData + tileFile, "r") as read_file:
            data = json.load(read_file)

        for tileList in data["tiles"]:
            if "comment" in tileList:
                eachValue = tileList["value"]
                value = (eachValue[0], eachValue[1], eachValue[2], eachValue[3])
                brush = tileList["brush"]

                if "foreground" in tileList["comment"]:
                    tiles[value] = Path(str(tilePath) + "/materials/" + brush[1][1] + ".png")
                elif "background" in tileList["comment"]:
                    tilesBackground[value] = Path(str(tilePath) + "/materials/" + brush[1][1] + ".png")

                elif "platform" in tileList["comment"]:
                    platforms[value] = Path(str(tilePath) + "/materials/" + brush[1][1] + ".png")

                elif "left" in tileList["comment"]:
                    for root, dirs, files in os.walk(objectPath):  
                        if brush[1][1] + ".object" in files:
                            with open(root + "/" + brush[1][1] + ".object", "r") as object_file:
                                try:
                                    object_data = json.load(object_file)
                                except json.JSONDecodeError:
                                    print("JSONDecodeError: " + str(object_file))
                            
                            orientations = object_data["orientations"]

                            objects[value] = StarObject(brush[1][1], Path(str(tilePath) + "/objects/" + brush[1][1] + ".png"), orientations[0]["imagePosition"][0], orientations[0]["imagePosition"][1], True)  

                else:
                    for root, dirs, files in os.walk(objectPath):  
                        if brush[1][1] + ".object" in files:
                            with open(root + "/" + brush[1][1] + ".object", "r") as object_file:
                                try:
                                    object_data = json.load(object_file)
                                except json.JSONDecodeError:
                                    print("JSONDecodeError: " + str(object_file))
                            
                            orientations = object_data["orientations"]

                            objects[value] = StarObject(brush[1][1], Path(str(tilePath) + "/objects/" + brush[1][1] + ".png"), orientations[0]["imagePosition"][0], orientations[0]["imagePosition"][1], False)



    for image in os.listdir(inputFolder):
        currentFile = Image.open(inputFolder + image)
        newImage = Image.new('RGB', (currentFile.width*8, currentFile.height*8))

        for x in range(0, currentFile.width):
            for y in range(0, currentFile.height):
                pixel = currentFile.getpixel((x,y))

                if "objects" in image:
                    if pixel in objects:
                        if objects[pixel].flipped == False:
                            img = Image.open(objects[pixel].image)
                            newImage.paste(img, ((x*8) + objects[pixel].x_offset, (y*8) - objects[pixel].y_offset - img.size[1] + 8))

                        elif objects[pixel].flipped == True:
                            img = Image.open(objects[pixel].image)
                            newImage.paste(ImageOps.mirror(img), ((x*8) + objects[pixel].x_offset, (y*8) - objects[pixel].y_offset - img.size[1] + 8))

                    elif pixel in tiles and not pixel == (255, 0, 220, 255):
                        newImage.paste(Image.open(tiles[pixel]), (x*8,y*8))

                    elif pixel in tilesBackground:
                        backgroundImage = Image.open(tilesBackground[pixel])
                        overlayedImage = backgroundImage.copy()
                        overlayedImage.paste(overlayImage, (0,0), overlayImage)
                        newImage.paste(overlayedImage, (x*8,y*8))

                    elif pixel in platforms:
                        newImage.paste(Image.open(platforms[pixel]), (x*8,y*8))

                else:
                    if pixel in tiles:
                        newImage.paste(Image.open(tiles[pixel]), (x*8,y*8))

                    elif pixel in tilesBackground:
                        backgroundImage = Image.open(tilesBackground[pixel])
                        overlayedImage = backgroundImage.copy()
                        overlayedImage.paste(overlayImage, (0,0), overlayImage)
                        newImage.paste(overlayedImage, (x*8,y*8))

                    elif pixel in platforms:
                        newImage.paste(Image.open(platforms[pixel]), (x*8,y*8))

        newImage.save(outputFolder + image)


if __name__ == '__main__':
    convert()