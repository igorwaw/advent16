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