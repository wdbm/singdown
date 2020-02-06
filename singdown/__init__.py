#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# singdown                                                                     #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is utilities associated with the Singdown singing syntax.       #
#                                                                              #
# copyright (C) 2020 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

usage:
    program [options]

options:
    -h, --help         display help message
    --version          display version and exit
    --filein=STRING    input file       [default: Daisy.fmd]
    --fileout=STRING   output XML file  [default: Daisy.xml]
    --bpm=FLOAT        beats per minute [default: 100]
"""

import docopt
import textwrap

name        = 'singdown'
__version__ = '2020-02-06T0150Z'

def singdown_to_xml(options=docopt.docopt(__doc__)):
    if options['--version']:
        print(__version__)
        sys.exit(0)
    filein      = options['--filein']
    fileout_XML = options['--fileout']
    fileout_WAV = options['--fileout']
    bpm         = options['--bpm']
    with open(filein) as f: data=f.read().strip().split('---')
    song = [datum.split('\n') for datum in data]
    header = textwrap.dedent(f'''<?xml version="1.0"?>\n<!DOCTYPE SINGING PUBLIC "-//SINGING//DTD SINGING mark up//EN" "Singing.v0_1.dtd" []>\n<SINGING BPM="{bpm}">\n''')
    footer = textwrap.dedent(f'''</SINGING>''')
    body = ''
    for sentence in song:
        sentence = [token for token in sentence if token is not '']
        words = [word for word in sentence[0].split() if word is not '']
        notes = [note for note in sentence[1].split() if note is not '']
        beats = [beat for beat in sentence[2].split() if beat is not '']
        for word, note, beat in zip(words, notes, beats):
            if word == 'REST' and note == 'REST':
                body = body+f'<REST BEATS="{beat}"></REST>\n'
            else:
                body = body+f'<DURATION BEATS="{beat}"><PITCH NOTE="{note}">{word}</PITCH></DURATION>\n'
    out = header+body+footer
    with open(fileout_XML, 'w') as f: f.write(out); f.close()

if __name__ == '__main__':
    main()
