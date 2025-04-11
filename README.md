# Novelty-Translation
This is a tool to make translating Novelty engine Visual Novels easier. Just download novelty.exe
from the Releases section, place it in the same folder as the game execultable, and run it. This
will generate a file named "translation.txt", which contains two version of each line of text,
one Original, and one Translated (obviously they are both the same at first). When you are done,
run novelty.exe again, and it will reinsert the file. From there, you can distribute the
NVZ file (but not the "OLD_" one, that's a backup).

Please note that NVZ files are actually just ZIP files, so if you rename one you can
extract its contents. From there, you can edit the files using the actual Novelty
editor (don't just change things yourself and re-zip, it won't work). I made this
tool because I find a single text file easier to work with than the whole graphical
editor, but if you want to use it (or have images to translate0, it can be found
here: http://www.visualnovelty.com/download.html.

Finally, the file zipfileF.py was not made by me, and is not covered under this
repository's Creative Commons Zero license. It was instead made by BjarniRunar
as part of their fork of Pyzipper: https://github.com/BjarniRunar/pyzipper.
I needed that fork instead of regular pyzipper or zipfile because it actually
lets me delete files in zip archives, so thanks!
