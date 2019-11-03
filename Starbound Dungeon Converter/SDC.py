from PIL import Image, ImageOps
from pathlib import Path
import os
import json

def convert():
    inputFolder = os.path.dirname(os.path.realpath(__file__)) + "/input/"
    outputFolder = os.path.dirname(os.path.realpath(__file__)) + "/output/"
    tileData = os.path.dirname(os.path.realpath(__file__)) + "/tileData/"
    foregroundImage = Image.open(Path(os.path.dirname(os.path.realpath(__file__)) + "/overlay.png"))
    
    if os.path.isfile("starPath.json"):
        with open("starPath.json", "r") as read_file:
            starboundPath = json.load(read_file)
    else:
        starboundPath = Path(input('Please input the path to your Starbound/tiled/packed directory: '))
        with open("starPath.json", "w") as write_file:
            json.dump(str(starboundPath), write_file)
        
    tiles = {
        (32, 32, 32, 255) : Path(str(starboundPath) + "/miscellaneous/11.png"),#Air
        (255, 0, 220, 255) : Path(str(starboundPath) + "/miscellaneous/01.png"),#Magic Pink Brush
        #(0, 0, 0, 255) : Path(str(starboundPath) + "/miscellaneous/02.png"),#Invisible Wall (boundary)
        (85, 255, 0, 255) : Path(str(starboundPath) + "/miscellaneous/03.png"),#Player start
        (120, 120, 120, 255) : Path(str(starboundPath) + "/miscellaneous/04.png"),#World gen must contain air
        #(0, 0, 0, 255) : Path(str(starboundPath) + "/miscellaneous/05.png"),#World gen must contain solid
        (34, 102, 0, 255) : Path(str(starboundPath) + "/miscellaneous/06.png"),#Biome item
        (26, 77, 0, 255) : Path(str(starboundPath) + "/miscellaneous/07.png"),#Biome tree
        (128, 128, 128, 255) : Path(str(starboundPath) + "/miscellaneous/08.png"),#Surface1
        (100, 100, 100, 255) : Path(str(starboundPath) + "/miscellaneous/08.png"),#Surface1
        (204, 186, 143, 255) : Path(str(starboundPath) + "/miscellaneous/08.png"),#Surface1
        (204, 176, 143, 255) : Path(str(starboundPath) + "/miscellaneous/08.png"),#Surface1
        (143, 186, 204, 255) : Path(str(starboundPath) + "/miscellaneous/09.png"),#Surface2
        (143, 176, 204, 255) : Path(str(starboundPath) + "/miscellaneous/09.png"),#Surface2
        (177, 204, 143, 255) : Path(str(starboundPath) + "/miscellaneous/10.png"),#Surface3
        (177, 194, 143, 255) : Path(str(starboundPath) + "/miscellaneous/10.png"),#Surface3
        (48, 48, 48, 255) : Path(str(starboundPath) + "/miscellaneous/11.png"),#Air overwriteable
        (255, 168, 0, 255) : Path(str(starboundPath) + "/miscellaneous/12.png"),#Red connector
        (0, 255, 186, 255) : Path(str(starboundPath) + "/miscellaneous/13.png"),#Yellow connector
        (168, 255, 0, 255) : Path(str(starboundPath) + "/miscellaneous/14.png"),#Green connector
        (0, 38, 255, 255) : Path(str(starboundPath) + "/miscellaneous/15.png"),#Blue connector
        (0, 0, 0, 255) : Path(str(starboundPath) + "/miscellaneous/16.png"),#World gen must contain air background
        (255, 255, 255, 255) : Path(str(starboundPath) + "/miscellaneous/17.png")#World gen must contain solid background
        #(0, 0, 0, 255) : Path(str(starboundPath) + "/miscellaneous/18.png"),#Invisible Wall (structure)
        #(0, 0, 0, 255) : Path(str(starboundPath) + "/miscellaneous/19.png"),#Underwater boundary
        #(0, 0, 0, 255) : Path(str(starboundPath) + "/miscellaneous/20.png"),#Zero g
        #(0, 0, 0, 255) : Path(str(starboundPath) + "/miscellaneous/21.png"),#Zero g protected
        #(0, 0, 0, 255) : Path(str(starboundPath) + "/miscellaneous/22.png"),#World gen must contain liquid
        #(0, 0, 0, 255) : Path(str(starboundPath) + "/miscellaneous/23.png"),#World gen must not contain liquid
    }
             
    tilesBackground = {
        (200, 200, 200, 255) : Path(str(starboundPath) + "/miscellaneous/08.png"),#Surface1
        (255, 232, 178, 255) : Path(str(starboundPath) + "/miscellaneous/08.png"),#Surface1
        (255, 222, 178, 255) : Path(str(starboundPath) + "/miscellaneous/08.png"),#Surface1
        (178, 232, 255, 255) : Path(str(starboundPath) + "/miscellaneous/09.png"),#Surface2
        (178, 222, 255, 255) : Path(str(starboundPath) + "/miscellaneous/09.png"),#Surface2
        (222, 255, 178, 255) : Path(str(starboundPath) + "/miscellaneous/10.png"),#Surface3
        (222, 245, 178, 255) : Path(str(starboundPath) + "/miscellaneous/10.png"),#Surface3
    }
    
    objects = {
    }
    
    flippedObjects = {
    }

    for tileFile in os.listdir(tileData):
        with open(tileData + tileFile, "r") as read_file:
            data = json.load(read_file)
        for tileList in data["tiles"]:
            if "comment" in tileList:
                eachValue = tileList["value"]
                value = (eachValue[0], eachValue[1], eachValue[2], eachValue[3])
                brush = tileList["brush"]
                if "foreground" in tileList["comment"]:
                    tiles[value] = Path(str(starboundPath) + "/materials/" + brush[1][1] + ".png")
                elif "background" in tileList["comment"]:
                    tilesBackground[value] = Path(str(starboundPath) + "/materials/" + brush[1][1] + ".png")
                elif "platform" in tileList["comment"]:
                    objects[value] = Path(str(starboundPath) + "/materials/" + brush[1][1] + ".png")
                elif "left" in tileList["comment"]:
                    flippedObjects[value] = Path(str(starboundPath) + "/objects/" + brush[1][1] + ".png")
                else:
                    objects[value] = Path(str(starboundPath) + "/objects/" + brush[1][1] + ".png")

    for image in os.listdir(inputFolder):
        currentFile = Image.open(inputFolder + image)
        convertedImage = Image.new('RGB', (currentFile.width*8, currentFile.height*8))
        for x in range(0, currentFile.width):
            for y in range(0, currentFile.height):
                pixel = currentFile.getpixel((x,y))
                if "objects" in image:
                    if pixel in objects:
                        convertedImage.paste(Image.open(objects[pixel]), (x*8,y*8))
                    elif pixel in flippedObjects:
                        convertedImage.paste(ImageOps.mirror(Image.open(flippedObjects[pixel])), (x*8,y*8))
                else:
                    if pixel in tiles:
                        convertedImage.paste(Image.open(tiles[pixel]), (x*8,y*8))
                    elif pixel in tilesBackground:
                        backgroundImage = Image.open(tilesBackground[pixel])
                        overlayedImage = backgroundImage.copy()
                        overlayedImage.paste(foregroundImage, (0,0), foregroundImage)
                        convertedImage.paste(overlayedImage, (x*8,y*8))
        convertedImage.save(outputFolder + image)

if __name__ == '__main__':
    convert()