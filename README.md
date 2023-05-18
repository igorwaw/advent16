# Advent of Code 2016

Advent of Code is a serious of programming puzzles: <https://adventofcode.com/2016/about>
Here is my take on the 2016 edition, done well later.

Feel free to use for inspiration. For some tasks I implemented more than was
required because I felt like it, for others I went straight to the point.

## Technology used

![Python](https://img.shields.io/badge/python-%3E%3D3.8-blue) 

I solved all puzzles with Python. Tested with 3.10 and with 3.6 where possible, most should work with any Python 3. I use the following
features of modern Python:

* dataclasses (introduced in 3.7) - day 1, 10, 11
* walrus operator (introduced in 3.8) - day 4, 7, 11

Extra Python libraries: Numpy for day 8


## AI powered

For this edition I experimented using Github Copilot to assist. From my experience, it worked great for the standard stuff such as opening files, iterating etc. - eg. I wrote "with" and automatically got "open INPUTFILE as f:". Then, when writing the main algorithm, I often disabled it because I kept getting wrong but distracting suggestions. After a few puzzles I disabled it completely as it was too distracting.

## Tasks

See directories
