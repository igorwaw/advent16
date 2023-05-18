## Day 10: Balance Bots

The instruction wasn't very clear, but here's the situation. We have 2 types of bot commands:

- take microchip: this can always be executed
- give microchip to another bot or place it in the output: this can only be executed if the bot has 2 microchips

So here's my take: I process the input file, execute the first type of instructions immediately and put other in the queue.
Then I iterate over the instruction queue until it's empty: if the bot is ready, command is executed and removed from the queue.

Two Python features were particularly useful to make the code both shorter and more readable: data class and default dict.

## Day 11: Radioisotope Thermoelectric Generators