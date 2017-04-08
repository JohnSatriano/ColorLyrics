from termcolor import colored, cprint

import os
import sys
import re
import string
import operator
import collections


#Prints something, uncomment sysout for debugging
def p(out,s):
  return s
  #sys.stdout.write(s)

#prints with color
def pc(out,s,color):
  if "on_" in color:
    return colored(s,on_color=color)
    #sys.stdout.write(colored(s,on_color=color))
  else:
    return colored(s,color)
    #sys.stdout.write(colored(s,color))


if (len(sys.argv) == 2):
  filename = sys.argv[1];
  inputText= open(filename).read()
else:
  inputText = sys.stdin.read();
  


inputText= re.sub('[,.!"?]|(\[.*\])','',inputText,flags=re.MULTILINE)
inputText= re.sub(' +',' ',inputText,flags=re.MULTILINE)
inputText= re.sub('^\s+','',inputText)
inputText= re.sub('\n\n','\n\n\n',inputText)
#pronunciation = os.popen("echo \""+inputText+"\" | ./espeak-1.48.04-source/src/speak --ipa -q").read() #local portable option
pronunciation = os.popen("echo \""+inputText+"\" | espeak --ipa -q").read()

#Clean up multiple spaces that confuse parser
inputText= re.sub('\n{3,}','\n\n',inputText,flags=re.MULTILINE)
pronunciation= re.sub('\n{3,}','\n\n',pronunciation,flags=re.MULTILINE)

count = dict()
#Get the frequency of vowel symbols
for i,letter in enumerate(pronunciation):
  try:
    # Skip non-vowels. This regex is inverted.
    if (re.match("[^iyɨʉɯuɪʏʊeøɘɵɤoəɛœɜɞʌɔæɐaɶɑɒ]",letter, re.IGNORECASE)):
      continue
    # This symbol indicates a long vowel. It changes the way it sounds
    elif re.match("[ː]",pronunciation[i+1]) :
      letter = letter + pronunciation[i+1] 
  except Exception:
    pass

  if not count.get(letter):
    count[letter] = 1
  else:
    count[letter] += 1


#Sort the count dictionary
count = sorted(count.items(), key=operator.itemgetter(1))
count.reverse()

colors = [
'on_red',
'on_green',
'on_yellow',
'on_blue',
'on_magenta',
'on_cyan',
'red',
'green',
'yellow',
'blue',
'magenta',
'cyan',
]

specialchars = dict()
#Assign colors to the most common symbols
for i,color  in enumerate(colors):
  if (i >= len(count)):
    continue
  specialchars[count[i][0]] = color

out = ""

#Create the output string
for i,letter in enumerate(pronunciation):
  #Check long vowel edge case
  try:
    if re.match("[ː]",pronunciation[i+1]) :
      letter = letter + pronunciation[i+1] 
    if re.match("[ː]",letter) :
      continue
  except:
    pass
  try:

    out += pc(out,letter,specialchars[letter])
  except:
    out += p(out,letter)

#Splitting output to output them together after all this processing
outLines = out.split("\n")
originalLines = re.split("[\n]",inputText)

j = 0
for i,normalLine in enumerate(originalLines):
  k = j
  colorLine = outLines[j].strip()
  #While the difference in number of words is greater than 2, continue to add words. 
  #The goal is to align all of the words together. This works, miraculously.
  while (abs(len(normalLine.split(" ")) - len(colorLine.split(" ")))>2):
    j += 1
    colorLine += " " + outLines[j]

  normalLine=normalLine.strip()
  #Strip out this character, it doesn't really help the presentation
  colorLine=colorLine.strip().replace("ˈ","")
  #Print it!
  print("%s\n%s"% (normalLine, colorLine))
  j += 1

#DONE!
