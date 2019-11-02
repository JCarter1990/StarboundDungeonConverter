from PIL import Image, ImageOps
from pathlib import Path
import os

def convert():
    inputFolder = os.path.dirname(os.path.realpath(__file__)) + "/input/"
    outputFolder = os.path.dirname(os.path.realpath(__file__)) + "/output/"
    foregroundImage = Image.open(Path(os.path.dirname(os.path.realpath(__file__)) + "/overlay.png"))
    
    starboundPath = input('Please input the path to your Starbound/tiled/packed directory: ')
    tiles = {
        #(32, 32, 32, 255) : Path(starboundPath + "/miscellaneous/00.png"),#Air
        (255, 0, 220, 255) : Path(starboundPath + "/miscellaneous/01.png"),#Magic Pink Brush
        #(0, 0, 0, 255) : Path(starboundPath + "/miscellaneous/02.png"),#Invisible Wall (boundary)
        (85, 255, 0, 255) : Path(starboundPath + "/miscellaneous/03.png"),#Player start
        (120, 120, 120, 255) : Path(starboundPath + "/miscellaneous/04.png"),#World gen must contain air
        #(0, 0, 0, 255) : Path(starboundPath + "/miscellaneous/05.png"),#World gen must contain solid
        (34, 102, 0, 255) : Path(starboundPath + "/miscellaneous/06.png"),#Biome item
        (26, 77, 0, 255) : Path(starboundPath + "/miscellaneous/07.png"),#Biome tree
        (128, 128, 128, 255) : Path(starboundPath + "/miscellaneous/08.png"),#Surface1
        #(0, 0, 0, 255) : Path(starboundPath + "/miscellaneous/09.png"),#Surface2
        #(0, 0, 0, 255) : Path(starboundPath + "/miscellaneous/10.png"),#Surface3
        #(48, 48, 48, 255) : Path(starboundPath + "/miscellaneous/11.png"),#Air overwriteable
        (255, 168, 0, 255) : Path(starboundPath + "/miscellaneous/12.png"),#Red connector
        (0, 255, 186, 255) : Path(starboundPath + "/miscellaneous/13.png"),#Yellow connector
        (168, 255, 0, 255) : Path(starboundPath + "/miscellaneous/14.png"),#Green connector
        (0, 38, 255, 255) : Path(starboundPath + "/miscellaneous/15.png"),#Blue connector
        (0, 0, 0, 255) : Path(starboundPath + "/miscellaneous/16.png"),#World gen must contain air background
        (255, 255, 255, 255) : Path(starboundPath + "/miscellaneous/17.png"),#World gen must contain solid background
        #(0, 0, 0, 255) : Path(starboundPath + "/miscellaneous/18.png"),#Invisible Wall (structure)
        #(0, 0, 0, 255) : Path(starboundPath + "/miscellaneous/19.png"),#Underwater boundary
        #(0, 0, 0, 255) : Path(starboundPath + "/miscellaneous/20.png"),#Zero g
        #(0, 0, 0, 255) : Path(starboundPath + "/miscellaneous/21.png"),#Zero g protected
        #(0, 0, 0, 255) : Path(starboundPath + "/miscellaneous/22.png"),#World gen must contain liquid
        #(0, 0, 0, 255) : Path(starboundPath + "/miscellaneous/23.png"),#World gen must not contain liquid
        (85, 217, 217, 255) : Path(starboundPath + "/materials/castlewalls1.png"),
        (70, 179, 179, 255) : Path(starboundPath + "/materials/castlewalls1.png"),
        (85, 98, 217, 255) : Path(starboundPath + "/materials/castlewalls2.png"),
        (70, 81, 179, 255) : Path(starboundPath + "/materials/castlewalls2.png"),
        (217, 85, 85, 255) : Path(starboundPath + "/materials/rooftiles.png"),
        (179, 70, 70, 255) : Path(starboundPath + "/materials/rooftiles.png"),
        (217, 184, 85, 255) : Path(starboundPath + "/materials/darkwood.png"),
        (129, 217, 85, 255) : Path(starboundPath + "/materials/bookpiles.png"),
        (153, 85, 217, 255) : Path(starboundPath + "/materials/bars.png"),
        (217, 115, 85, 255) : Path(starboundPath + "/materials/crosshatch.png"),
        (193, 217, 85, 255) : Path(starboundPath + "/materials/fadedblocks.png"),
        (144, 85, 217, 255) : Path(starboundPath + "/materials/woodenwindow1.png"),
        (217, 70, 41, 255) : Path(starboundPath + "/materials/thatch.png"),
        (217, 151, 85, 255) : Path(starboundPath + "/materials/fence.png"),
        (217, 193, 128, 255) : Path(starboundPath + "/materials/dirt.png"),
        (166, 143, 70, 255) : Path(starboundPath + "/materials/fullwood1.png"),
        (217, 85, 153, 255) : Path(starboundPath + "/materials/sewage.png"),
        (179, 70, 126, 255) : Path(starboundPath + "/materials/sewage.png"),
        (204, 80, 144, 255) : Path(starboundPath + "/materials/sewage.png"),
        (201, 217, 85, 255) : Path(starboundPath + "/materials/sewerpipe.png"),
        (166, 179, 70, 255) : Path(starboundPath + "/materials/sewerpipe.png"),
        (189, 204, 80, 255) : Path(starboundPath + "/materials/sewerpipe.png"),
        (85, 217, 94, 255) : Path(starboundPath + "/materials/plantmatter.png"),
        (80, 204, 88, 255) : Path(starboundPath + "/materials/plantmatter.png")
    }
             
    tilesBackground = {
        (200, 200, 200, 255) : Path(starboundPath + "/miscellaneous/08.png"),#Surface1
        #(0, 0, 0, 255) : Path(starboundPath + "/miscellaneous/09.png"),#Surface2
        #(0, 0, 0, 255) : Path(starboundPath + "/miscellaneous/10.png"),#Surface3
        (55, 140, 140, 255) : Path(starboundPath + "/materials/castlewalls1.png"),
        (40, 102, 102, 255) : Path(starboundPath + "/materials/castlewalls1.png"),
        (55, 63, 140, 255) : Path(starboundPath + "/materials/castlewalls2.png"),
        (40, 46, 102, 255) : Path(starboundPath + "/materials/castlewalls2.png"),
        (140, 55, 55, 255) : Path(starboundPath + "/materials/rooftiles.png"),
        (102, 40, 40, 255) : Path(starboundPath + "/materials/rooftiles.png"),
        (166, 140, 65, 255) : Path(starboundPath + "/materials/darkwood.png"),
        (98, 166, 65, 255) : Path(starboundPath + "/materials/bookpiles.png"),
        (117, 65, 166, 255) : Path(starboundPath + "/materials/bars.png"),
        (166, 89, 65, 255) : Path(starboundPath + "/materials/crosshatch.png"),
        (147, 166, 65, 255) : Path(starboundPath + "/materials/fadedblocks.png"),
        (110, 65, 166, 255) : Path(starboundPath + "/materials/woodenwindow1.png"),
        (166, 54, 31, 255) : Path(starboundPath + "/materials/thatch.png"),
        (166, 115, 65, 255) : Path(starboundPath + "/materials/fence.png"),
        (166, 148, 98, 255) : Path(starboundPath + "/materials/dirt.png"),
        (115, 99, 48, 255) : Path(starboundPath + "/materials/fullwood1.png"),
        (166, 65, 117, 255) : Path(starboundPath + "/materials/sewage.png"),
        (128, 50, 50, 255) : Path(starboundPath + "/materials/sewage.png"),
        (155, 166, 65, 255) : Path(starboundPath + "/materials/sewerpipe.png"),
        (118, 128, 50, 255) : Path(starboundPath + "/materials/sewerpipe.png"),
        (65, 166, 71, 255) : Path(starboundPath + "/materials/plantmatter.png")
    }
    
    objects = {
        (179, 141, 89, 255) : Path(starboundPath + "/materials/platform.png"),
        (179, 126, 89, 255) : Path(starboundPath + "/materials/woodenplatform.png"),
        (179, 112, 89, 255) : Path(starboundPath + "/materials/copperplatform.png")
    }
    
    flippedObjects = {
    }
    
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