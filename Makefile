.DEFAULT_GOAL := all
CFLAGS=-Wall -g

all: game

game: object.o

.PHONY: clean test

clean: 
	rm -f game object.o

# The test suite is a Python script
# that must exist in this directory.
test:
	./game_test.py
