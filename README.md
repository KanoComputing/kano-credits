
Kano-Credits

Uses python curses.

To build program so the text and art are in line, run:

python build.py

Then to run the program:

python main.py

To add ascii art, save in a text file - for credits for staff, preferably put in 18-20 line intervals including the ascii art and one line of white space directly below.  Will need to repeat the art at least once (see examples in staff-images folder).

Create an ascii object in ascii.py, and list the art in an array e.g. in staffAsciiArt.

Similarly add the file containing the text (list of names) in the text.py file.
Currently the list of names is in the format:

Name1;Information about person1
Name2;Information about person2

The build progarm creates a file to format the text like:

Name
Information about person1






Name2
Information about person2

with an appropriate amount of whitespace to match the art and text together.

Currently formatted for a 1024 by 768 window.