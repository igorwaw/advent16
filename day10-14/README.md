## Day 10: Balance Bots

The instruction wasn't very clear, but here's the situation. We have 2 types of bot commands:

- take microchip: this can always be executed
- give microchip to another bot or place it in the output: this can only be executed if the bot has 2 microchips

So here's my take: I process the input file, execute the first type of instructions immediately and put other in the queue.
Then I iterate over the instruction queue until it's empty: if the bot is ready, command is executed and removed from the queue.

Two Python features were particularly useful to make the code both shorter and more readable: data class and default dict.

## Day 11: Radioisotope Thermoelectric Generators

Hardest problem so far this year. We need to move all devices to the 4th floor. RTGs emit radiation that would damage
a chip on the same floor, unless the chip is connected to its own RTG. Elevator can only take 1 or 2 devices (not 0).

The problem takes a few steps to solve:

- read input and model the data,
- check for the end condition at each iteration of the main loop,
- get the next possible move, check if it leads to a valid condition,
- repeat until the solution is found, in the right order (BFS) and avoiding the states that were already checked.

I used dataclasses, itertools, sets, regular expressions... Can't imagine doing that in anything other then Python.

## Day 12: Leonardo's Monorail

We need to simulate a computer with a very simple CPU architecture: 4 registers, 4 instructions. Easy. Very similar
to day 23 from 2015, in fact I copied some code. 