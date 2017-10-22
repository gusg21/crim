# crim

Welcome to crim! If you've ever heard of __Befunge__, you'll have a head start with crim.

## How work?

It's best to think of a crim program as a 2d surface with characters arranged in a grid. Your program controls a little "pointer" that can move through the grid in one cell steps in any of the cardinal directions (up, right, down, left). Your pointer is always in a mode, and each mode processes commands differently. As your pointer moves, it will pass through commands and execute them.

Your pointer always starts in the top left, moving right. Here's a _Hello, World!_ program:

    "Hello World!"

It just looks like a string, __but it is not.__ The quotes (`"`) actually switch from the default mode (`normal` mode) to `print` mode. In print mode, any characters passed through are printed to the terminal. You can't change the direction of the pointer in `print` mode. The second quote switches back from `print` into `normal`.

You might notice that the program hangs after it prints. this is because the pointer, after the last quote, will keep going. To have your program close at the end, do:

    "Hello World!"@

When the pointer passes through the `@` symbol in normal mode, your program terminates.

To help illustrate directions, this prints "Hello World!" in an endless loop.

    > "Hello World!" v
    ^                <
    
When the `>` symbol is passed through, the direction changes to right. When the program starts, the pointer was already going right, but it's needed later. The `v` directs the pointer down into the `<` which turns is left, and then into the `^` which turns it upwards. Then the `>` turns it right again, and back through the print.

### Accumulator and Memory

There are two places for storing data. The __accumulator__ can hold one number at a time. When you perform operations or commands, they almost always change the value of the accumulator. Memory is for storing data. You would pull data out of memory into the accumulator to work with it, and then put it back for later. Memory by default has 100 slots (0-99), but can be resized from the command line.

## License

This is licensed under the LGPL license.

2017, gusg21
