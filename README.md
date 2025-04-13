# Novelty-Translation
This is a tool to make translating Novelty engine Visual Novels easier. Just download novelty.exe
from the Releases section, place it in the same folder as the game executable, and run it. This
will generate a file named "translation.txt", which contains two version of each line of text,
one Original, and one Translated (obviously they are both the same at first). When you are done,
run novelty.exe again, and it will insert the translated text. From there, you can distribute the
NVZ file to people (but not the "OLD_" one, that's a backup).

NOTE 1: This tool is is only designed for Windows (unless you want to try running the Python
yourself, that is). For Mac and Linux, I can only point you to WINE: https://www.winehq.org/.

NOTE 2: To determine where an option or "goto" action leads to, look for the "page-uid" section,
then find the page marker with the same uid.

NOTE 3: The characters "\&#x0A;" (without the quotes or the backslash if you can see it) in a
line of dialogue represent a line break. Novelty does not have automatic word-wrapping, so you
will have to experiment to see how many characters of your game's font fit on each line. I have
also found these other control characters so far (also without the backslash if you can see it):
- \&quot; = double quotation marks
- \&apos; = apostrophe (single quotation mark)
- \&amp; = ampersand ("&")
- \&lt; = less-than symbol ("<")
- \&gt; = greater-than symbol (">")

Also, fun fact, NVZ files are actually just ZIP files, so if you rename one you can extract its
contents. From there, you can edit the files using the actual Novelty editor (don't just change
things yourself and re-zip, it won't work). I made this tool because I find a single text file 
easier to work with than the whole graphical editor, but if you want to use it (or have images
to translate), it can be found here: http://www.visualnovelty.com/download.html.

Finally, the file zipfileF.py was not made by me, and is not covered under this repository's
Creative Commons Zero license. It was instead made by BjarniRunar as part of their fork of
Pyzipper: https://github.com/BjarniRunar/pyzipper (since I renamed it, I should clarify that the
file I used from there is "zipfile.py" in the folder "pyzipper"). I needed that fork instead of
regular pyzipper or zipfile because it actually lets me delete files in zip archives, so thanks!
