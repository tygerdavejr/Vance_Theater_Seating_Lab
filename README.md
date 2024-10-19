# Vance_Theater_Seating_Lab
This program displays a welcome banner and the constant values in a meaningful format.  It then prompts the
user for input per section and validates that input, calculates tickets sold, and displays a cumulative total
of total sales.  Finally, it displays a summary of the sales per section and total ticket sales.

To build this program I first wrote out the pseudocode to get myself aligned.  I then used
iPython to test snippets to make sure my logic was good, then I went in and wrote the actual code.

In some instances I needed to refer back to older projects to remember formatting, for example how
to do decimal point for money.  I knew how to do it, but I didn't remember the exact format.

For entry validation, I forced the input as a string, and then processed that way.  It was cleaner than
doing int(input()) commands as a non-integer will actually break the program.  It also prevents the user from
entering negatives, floats, exponentials, etc.  Entries like -1, 25.5, ebwehaip, etc are all ignored, an error
message is displayed, and the user is prompted to input a new value.

The next method of validation was to ensure the seats sold fit into the expected range of no more than seats
available.  If this did occur, the user would be given an error message, and then prompted to enter a
new value.

The main approach I took was to build the constants into tuples and then use a loop to call functions.
I felt it was significantly cleaner than writing a bunch of lines to call functions one constant at a time.
It also means any future programmer only needs to add new constants and then ensure that constant is included
into the tuple.

This was another fun exercise.  I enjoyed the challenge.  I don't want to get ahead into classes and objects
even though I see other students are already working on that format.  I figure that will come soon enough.

UPDATE:  
I read and then reread this week's reading and decided I needed to incorporate a SENTINEL to the software.
This added minor complexity.  Because I am processing ticket sales as a loop, I can't use a BREAK; it only
exit's the current loop.  I wanted to print a Thank You message and then exit the program entirely.

I could have done the initial input, included an IF statement to check for SENTINEL, and then continue, but I 
would have also needed to repeat the lines inside the loop.  What I chose to do instead was prime an error 
message with a null value, prime the input variable with a wrong value, and then enter the loop.  Basically,
the loop ALWAYS fails the first iteration.  The loop will then print the error message (a null string on the first
loop), input a value, check the value for SENTINEL and end program if true, else return to the top of the loop.

Again, I tested my code in iPython to ensure my logic was correct before implementing the change in my
assignment.
