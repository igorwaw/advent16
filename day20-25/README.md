## Day 20: Firewall Rules

Once again exercise in optimization. We have some blocklists and need to find IPs
outside of them. There are some nice, easy to code ways to do it that would work
for smaller spaces. Eg. I could create ranges for blocklists, unpack them into
one list and just check `if ip not combined_blocklist`. But such ways would
take too much time or memory to check 2^32 addresses. Solution? Code like it's
1980 and only operations you have are +, - and <.

## Day 21: Scrambled Letters and Hash

Part 1: we need to scramble a password according to a list of instructions. Easy.
Part 2: we need to unscramble a password. A bit complicated. Most instructions can
be easily reversed or even work the same both ways. Except one, for rotating string
based on a position of a letter. I wasn't able to figure out how to reverse the
formula, so I ended up trying all possibilities, getting the numbers and putting
them in a lookup table.

## Day 22: Grid Computing

We need to move data around the grid cluster. Part 1, calculate pairs of
nodes that can be used for moving data - very easy, just a regexp to parse
input plus some elementary maths.

Part 2: it's very annoying that I can't code a universal solution. A usual
BFS brute force wouldn't work as the problem space is too big. Instead I
combined the strong points of the computer: looking up data and doing simple
maths - and strong points of human: pattern recognition. First, I printed the grid.

There is only one empty node. Which means we need to move the "hole" next to the
node we're interested in. In my case, it happens to be last but one node on
the last row. So I would simply move it up (1 step for each row), except there
are also a few nodes much larger then the rest, that can't be copied. They form
a "wall" which we need to pass to the left and then go back to the right.

Finally, we need to move the data using the empty node, then move the empty node
(by going down, to the side and up again). So, moving the data by one column
takes 5 steps. Complete formula is `(emptyx+1-wallbegin)+emptyy+wallsize+(width-1)*5`
which at least makes the solution viable for other setups where the wall is in one
row, extends to the right edge and the hole is down and to the right relative to the
first node of the wall. 