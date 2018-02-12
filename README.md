# CrystalBot
[Crystallography Open Database](http://www.crystallography.net/cod/) meets Axidraw (https://shop.evilmadscientist.com/productsmenu/846), 
drawing the structure of the latest addition to the COD on a sheet of paper.

Crystallography Open Database is an open access collection of crystal structures of organic, inorganic, metal-organic compounds and minerals, created and maintained by scientists who wanted to make this data accessible for all. 
As of 2018-02-12, there were 391176 entries at the COD. It is an example of vast scientific databases whose entries are rarely, if ever, seen by human eyes. I wanted to demonstrate the expansion of human knowledge in an immediate, physical way, rendering the quiet and hidden labour of science visible. 

Huge thanks to Saulius Gražulis, @KaMykolas and ffwd for their help with crystallographic software, Axidraw and sed respectively.

An example of a random structure:
![alt text](https://github.com/Technariumas/CrystalBot/blob/master/example.png)

Same picture, inverted and converted to black and white using ImageMagick:

![alt text](https://github.com/Technariumas/CrystalBot/blob/master/output.png)

Vectorised output (using potrace):
![alt text](https://github.com/Technariumas/CrystalBot/blob/master/vector.png)

The structure, drawn on paper:
![alt text](https://github.com/Technariumas/CrystalBot/blob/master/plot.jpg)


The script is pretty self-explanatory. You will need [Jmol](https://en.wikipedia.org/wiki/Jmol), ImageMagick, [axibot](https://github.com/storborg/axibot) and [potrace](http://potrace.sourceforge.net/) to run it.

