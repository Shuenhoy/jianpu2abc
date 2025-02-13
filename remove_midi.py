# remove "\midi { \context { \Score tempoWholesPerMinute = #(ly:make-moment 84 4)}}"

import sys
infile = sys.argv[1]
outfile = sys.argv[2]


with open(infile, 'r') as f:
    alltext = f.read()

alltext = alltext.replace(r"\midi { \context { \Score tempoWholesPerMinute = #(ly:make-moment 84 4)}}", "")

with open(outfile, 'w') as f:
    f.write(alltext)