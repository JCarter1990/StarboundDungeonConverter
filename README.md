# StarboundDungeonConverter
Old starbound dungeons are quite tedious to look through if you are trying to make a json version of it, 
so i made this tool to make things a bit easier.

Make sure to create an input folder and output folder within the Starbound Dungeon Converter folder, for whatever reason github decided to remove them when i uploaded this.

You put the png's of the dungeon into the input folder and run the python file, it will ask you for the path to your 
starbound/tiled/packed directory. Once you have entered this just wait for the results.

What the program will do is look at the rgb value of each pixel in the dungeon file then check this against the values stored
in each of the four dictionaries tiles, tilesbackground, objects and flippedObjects.

If it has found a match then it will open the resulting image and paste it in a new image in the same place.
The output folder contains the new images with tiles instead of pixels.

At the moment the program only contains tile information for glitch buildings so if you want to convert other race buildings
you will need to add the tile information to one of the four dictionaries.

Tile information follows the format (0, 0, 0, 255) : Path(starboundPath + "/materials/castlewalls1.png") where the four digits
are RGB and Alpha values. The only other bit you need to change is the "/materials/X.png" where X is the name of the tile file.

There is support for objects but i haven't added the tile info for them, something to keep in mind about this though is that objects
will be misaligned because images are pasted from the top left.
