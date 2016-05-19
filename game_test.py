#!/usr/bin/python

import os
import sys
import pexpect

# Start the game program.
game = pexpect.spawn(os.path.join(os.getcwd(), 'game'))

# Log all output to stdout.
game.logfile = sys.stdout

# Start playing the game.
game.expect('You enter the The great Hall.')
game.sendline('n')
game.expect('You go north, into:\r\nThe throne room.')
game.sendline('e')
game.expect('You go east, into:\r\nKitchen, you have the knife now.')
game.sendline('w')
game.expect('You go west, into:\r\nThe throne room.')
game.sendline('w')
game.expect('You go west, into:\r\nThe arena, with the minotaur.')

# Attack the minotaur.
monster_is_alive = True
while monster_is_alive:
    game.sendline('a')
    game.expect('You attack The evil minotaur!\r\nIt is \D*')
    # Stop attacking once the minotaur is dead.
    if len(game.after) == 48:
        monster_is_alive = False

# Go back to the great hall and do a happy dance, then leave the game.
game.sendline('e')
game.expect('You go east, into:\r\nThe throne room.')
game.sendline('s')
game.expect('You go south, into:\r\nThe great Hall.')
for i in range(5):
    game.sendline('a')
    game.expect('You flail in the air at nothing. Idiot.')
game.sendcontrol('c')
