"""Stage 5: Puzzle 6 of 10

Can you figure out how draw this triangle and square? Hint: Do the
triangle first, then figure out how much to turn before drawing the
square.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level29')

for count in range(3):
    artist.move_forward(100)
    artist.right(120)

artist.left()

for count in range(4):
    artist.move_forward(100)
    artist.left()
    
    
artist.check()
