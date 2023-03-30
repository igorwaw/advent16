# Day 1: No Time for a Taxicab

Day 1 and we're already moving on a grid! I used a dataclass for coordinates - I've got a feeling I'll use it a lot.

Got some good results with Github Copilot. Clearly someone's solution for this exact task was in the training data, because I got a working solution for part 1 almost automatically. But the solution for part 2 needed some fixes.

# Day 2: Bathroom Security

Another Copilot experiment. Got the code almost right for part 1 and very wrong for part 2. I rewrote it using too many elifs, the code could be made shorter by using hexadecimal numbers.

# Day 3: Squares With Three Sides

Again correct results from Copilot for part 1 only. For part 2, I ended up disabling it because it tried to write it in a completely different way. Shorter, arguably more elegant, but wrong. The code is still simple, but already too much for the AI.

# Day 4: Security Through Obscurity

Disabled Copilot, not much use here. Good old copy-paste worked better.

Two tasks. Part 1 was about calculating a checksum using an unusual algorithm. Counter object greatly simplified the code.
Part 2 was a simple cypher - addition, subtraction and modulo is all that's needed.

# Day 5: How About a Nice Game of Chess?

We're generating password by making a lot of md5 hashes and extracting specific characters. Nothing special, there's a handy md5 function
in hashlib module from the standard library. And for the text manipulation, as long as you remember the difference between int 0 and character "0"
and between string and array of characters, you're gonna be fine.

# Day 6: Signals and Noise

Two simple tasks. First, read input file and get columns instead of rows. Just the for loop over each line, nothing fancy.
Second, for each column, get the most/least common letter. Counter from collections module is once again useful.

# Day 7: Internet Protocol Version 7

Regular expressions with backreferences for part 1. I hate them, though I seem to be getting better at them.

But I couldn't write the right regexp for part 2. Instead, I found it easier to do some C-style coding in Python:
process string as a character array and use a very simple state machine (with just 2 states: inside and
outside the square brackets). I'm looking for all ABA blocks, store them in two sets (actually I just store AB),
separately for inside and outside square brackets. Then it's just checking if the two sets have any elements in common.
The important thing is to reverse characters for one of the sets.

# Day 8: Two-Factor Authentication

Now that's more like it! First taste of unusal hardware: we have a list of instructions for the screen and need to find out what
it would display. I used Numpy since it makes operations on 2D arrays both easier and faster. Granted, not by much in a simple
example like this. I also packed the whole logic around display into a class and even used type hints - overkill for such a simple
program.

