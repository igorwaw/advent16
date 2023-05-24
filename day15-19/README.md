## Day 15: Timing is Everything

We got a machine with spinning disks and need to calculate when they reach
a specific position. Solved the puzzle in two ways: brute force - iterating
through the steps, and fancy, using Chinese Remainder Theorem. Actually the
brute force version was good enough, it only took about 2 seconds.
Python is notorious for low performance, yet it iterated through 3 million
steps in a moment. Computers are really fast!

## Day 16: Dragon Checksum

Generating checksums. Nothing fancy here.

## Day 17: Two Steps Forward

Finding path in the vault - obvious application of BFS.

## Day 18: Like a Rogue

A simple cellular automata. For part 2 the problem gets huge,
so we just need to make sure the program isn't terribly inefficient.

## Day 19: An Elephant Named Joseph

Elves passing presents in a (large) circle. I tried brute force first -
worked for part 1, but was too slow for part 2.

I didn't know the problem described here, but I thought the name must
mean something and googled for "Joseph algorithm". Google was smart
enough to find "Josephus algorithm" for me. That also worked for part 1.

Part 2 was different. There are generalized Josephus solutions for
finding survivor with a group of size n with a step of k. So, if 
we modify k at each step to be number_of_remaining _elves//2, that
should do it, right? Wrong.

Instead, I checked the answer for some low numbers and found the
pattern. 