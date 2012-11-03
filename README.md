pywsd.py
--------

This is a utility script to create UML sequence diagrams using a plain-text
notation. That is, this program converts

	alice->bob: authentication request
	bob-->alice: response

to 

![example.png](https://raw.github.com/btbytes/pywsd/master/example.png)


## Typical Usage

Simplest:

	$ ./pywsd.py example.txt
	$ ls
	example.png


Something fancy:

	$ ./pywsd.py example.txt -s napkin
	$ ls
	example.png

The sequnce diagram should look like something you drew on a napkin.

Note: `./pywsd.py -h` for a list of available styles.


If you want to get rid of the water marking at the bottom, use `convert`:

	$ convert example.png -gravity South -chop 0x14 example.png


With a `Makefile` (because makefiles rock):

	SOURCES = $(wildcard *.txt)
	INTER = $(patsubst %.txt, %.png1, $(SOURCES))
	PNGS = $(patsubst %.txt, %.png, $(SOURCES))

	all: $(PNGS)

	%.png1: %.txt
		./pywsd.py $< -o $@

	%.png: %.png1
		convert $< -gravity South -chop 0x14 $@

	clean:
		rm -f $(INTER)

	clean-all:
		rm -f $(PNGS)


Thanks to [WebSequnceDiagrams.com](http://www.websequencediagrams.com/) for making such a handy and intuitive tool available for free on the web. 
