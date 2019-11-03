# StarboundDungeonConverter
Old starbound dungeons are quite tedious to look through if you are trying to make a json version of it, so i made this tool to make things a bit easier.

You put the png's of the dungeon into the input folder and run the python file, it will ask you for the path to your 
starbound/tiled/packed directory. Once you have entered this just wait for the results.

What the program will do is look at the rgb value of each pixel in the dungeon file then check this against the values stored
in each of the four dictionaries tiles, tilesbackground, objects and flippedObjects.

If it has found a match then it will copy the image and paste it in a new image in the same place. The output folder contains the new images with tiles instead of pixels.

There is support for objects but something to keep in mind about this is that objects will be misaligned because images are pasted from the top left. For whatever reason chucklefish didn't choose a single spot for objects to be spawned from.
