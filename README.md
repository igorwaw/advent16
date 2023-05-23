# Advent of Code 2016

Advent of Code is a serious of programming puzzles: <https://adventofcode.com/2016/about>
Here is my take on the 2016 edition, done well later.

Feel free to use for inspiration. For some tasks I implemented more than was
required because I felt like it, for others I went straight to the point.

## Technology used

![Python](https://img.shields.io/badge/python-%3E%3D3.10-blue)

I solved all puzzles with Python. Tested with 3.10, most should work with older Python 3. I used the following
features of modern Python:

* dataclasses (introduced in 3.7) - day 1, 10, 11, 13, 17
* walrus operator (introduced in 3.8) - day 4, 7, 11
* match/case (introduced in 3.10) - day 12
* bit_count function (introduced in 3.10) - day 13

Extra Python libraries: Numpy for day 8


## AI powered

For the first few puzzles I experimented using Github Copilot to assist. From my experience, it
worked great for the standard stuff such as opening files, iterating etc. - eg. I wrote "with"
and automatically got "open INPUTFILE as f:". Then, when writing the main algorithm, I often
disabled it because I kept getting wrong but distracting suggestions. After a few days I
disabled it completely as it was too distracting.

## Tasks

See directories
