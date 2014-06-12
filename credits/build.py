
# build.py
#
# Copyright (C) 2013 Kano Computing Ltd.
# Licence:  http://www.gnu.org/licences/gpl-2.0.txt GNU General Public License v2
#

import ascii
import graphics
import re
import console

TMP_FILE = '/tmp/actualText'
STAFF_NAMES = 'text/staff'


class Build(object):

    def __init__(self, textFilenames):
        self.textFilenames = textFilenames
        self.text = []
        self.createdText = []
        open(TMP_FILE, 'w').close()
        self.build()

    def build(self):

        (width, height) = console.getTerminalSize()

        h = open(TMP_FILE, 'a')
        # This decides how high up the text should start
        for k in range(height - 8):  # -18 initially
            h.write(' '.ljust(30) + '\n')

        with open(self.textFilenames) as f:
            self.text = f.readlines()

        for i in range(len(self.text)):
            # for each line in the text file, add the appropriate amoutn of whitespace for
            # the corresponding image
            try:
                numberOfLines = ascii.allAsciiArt[i].numberOfLines
                for j in range(numberOfLines - 2):
                    h.write(' '.ljust(30) + '\n')
                # Swap ; with whitepace and a new line character
                text = re.sub('\n', ' '.ljust(14) + '\n', self.text[i])
                text = re.sub(';', '\n', text)

                h = open(TMP_FILE, 'a')
                h.write(text)

            # should fail at the end of the file, so just close the file.
            except:
                h.close()

        h.close()

# ----------------------------------------------------------------------------

graphics.init()
Build(STAFF_NAMES)
