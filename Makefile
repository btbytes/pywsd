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

.PHONY: clean-all