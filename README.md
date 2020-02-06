# Singdown

Singdown is a simple, plaintext singing syntax inspired by [Markdown](https://en.wikipedia.org/wiki/Markdown) which is designed to be written and read easily by humans and machines. It can be converted using included commands to an XML format suitable for input to the [singing mode](http://zeehio.github.io/festival/doc/Singing-Synthesis.html) of the Festival Speech Synthesis System.

Singdown is formed from lines separated by `---`. A line features three tracks, and elements within tracks are separated by whitespace. The first track consists of the words sung. The second track consists of the notes, separated by commas when there are multiple notes corresponding to a word. The third track consists of the beats, which correspond to a global beats-per-minute specification. There is a special line that corresponds to a rest, wherein the first and second tracks both consist of the word "REST" and the third track corresponds to the beat of the rest.

# setup

```Bash
sudo apt install festival sox speech-tools

pip install singdown
```

# example: Daily Bell

The following Singdown syntax can be saved to a file `Daisy.sd`:

```
Daisy   Daisy
F4,D4   Bb3,F3
1.0,1.0 1.0,1.0
---
Give me   your answer    do
G3   A3   Bb3  G3,Bb3    F3
0.33 0.33 0.34 0.67,0.33 1.5
---
REST
REST 
0.5
---
I'm half crazy 
C4  F4   D4,Bb3
1.0 1.0  1.0,1.0
---
all  for  the  love of   you
G3   A3   Bb3  C4   D4   C4
0.33 0.23 0.34 0.67 0.33 1.3
---
REST
REST
0.17
---
It   won't be   a    stylish   marriage
D4   Eb4   D4   C4   F4,D4     C4,Bb3
0.33 0.33  0.33 0.33 0.67,0.33 0.33,1.17
---
I    can't afford    a    carriage
C4   D4    Bb3,G3    Bb3  G3,F3
0.33 0.67  0.33,0.67 0.33 0.33,1.17
---
REST
REST
0.17
---
But  you'll look sweet upon      the  seat of   a    bicycle        built for  two
F3   Bb3    D4   C4    F3,Bb3    D4   C4   D4   Eb4  F4,D4,Bb3      C4    F3   Bb3
0.33 0.67   0.33 0.67  0.33,0.67 0.33 0.34 0.33 0.33 0.34,0.33,0.33 0.67  0.33 1.5
---
REST
REST 
0.5
```

The file can then be converted to an XML format suitable for Festival, and this XML format can then be converted to WAVE using Festival:

```Bash
singdown_to_xml --filein=Daisy.sd --fileout=Daisy.xml --bpm=60

text2wave -mode singing Daisy.xml -o Daisy.wav

play Daisy.wav
```

Alternative voices can be used:

```Bash
text2wave -mode singing Daisy.xml -o Daisy.wav -eval "(voice_ked_diphone)"
```

# harmony

Harmonies can be created using multiple Singdown files:

```Bash
singdown_to_xml --filein Spice_1.sd --fileout Spice_1.xml
singdown_to_xml --filein Spice_2.sd --fileout Spice_2.xml
singdown_to_xml --filein Spice_3.sd --fileout Spice_3.xml
singdown_to_xml --filein Spice_4.sd --fileout Spice_4.xml

text2wave -mode singing Spice_1.xml -o Spice_1.wav
text2wave -mode singing Spice_2.xml -o Spice_2.wav
text2wave -mode singing Spice_3.xml -o Spice_3.wav
text2wave -mode singing Spice_4.xml -o Spice_4.wav

ch_wave -o Spice.wav -pc longest Spice*.wav
```
