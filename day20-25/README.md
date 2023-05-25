## Day 20: Firewall Rules

Once again exercise in optimization. We have some blocklists and need to find IPs
outside of them. There are some nice, easy to code ways to do it that would work
for smaller spaces. Eg. I could create ranges for blocklists, unpack them into
one list and just check `if ip not combined_blocklist`. But such ways would
take too much time or memory to check 2^32 addresses. Solution? Code like it's
1980 and only operations you have are +, - and <.


