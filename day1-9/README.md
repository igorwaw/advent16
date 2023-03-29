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