from termcolor import colored, cprint

import os
import sys
import re
import string
import operator
import collections


#Prints something
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
  inputText= open(filename).read();
else:
  inputText = sys.stdin.read();
  

pronunciation = os.popen("echo \""+inputText+"\" | espeak --ipa -q").read()
#os.popen("./pronounce " + re.escape(s)).read()
#accentMode = True
accentMode = False

count = dict()
#pronunciation = pronunciation.replace("iː","ɪ")
for i,letter in enumerate(pronunciation):
  try:
    if (re.match("[^iyɨʉɯuɪʏʊeøɘɵɤoəɛœɜɞʌɔæɐaɶɑɒ]",letter, re.IGNORECASE)):
    #if re.match("[ː ʃŋɡˈˌ\nð]",letter) or (re.match("[a-z]",letter,re.IGNORECASE) and re.match("[^aeiou]",letter, re.IGNORECASE)):
      continue
    #elif re.match("[ˈː]",pronunciation[i+1]):
    elif re.match("[ː]",pronunciation[i+1]) :
      letter = letter + pronunciation[i+1] 
    #elif letter == "ˈ" or letter == " " or letter == "\n" or lek
  except Exception:
    pass

  if not count.get(letter):
    count[letter] = 1
  else:
    count[letter] += 1


count = sorted(count.items(), key=operator.itemgetter(1))
count.reverse()
#print (count)

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
#print(pronunciation)
for i,color  in enumerate(colors):
  specialchars[count[i][0]] = color
#print (specialchars)
out = ""

for i,letter in enumerate(pronunciation):
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

#print(out)
outLines = out.split("\n")
originalLines = re.split("[\n,]",inputText)
j = 0
for i,normalLine in enumerate(originalLines):
  k = j
  colorLine = outLines[j].strip()
  while (abs(len(normalLine.split(" ")) - len(colorLine.split(" ")))>2):
    #print(len(line.split(" ")) )
    #print(len(colorLine.split(" ")))
    j += 1
    colorLine += " " + outLines[j]

  normalLine=normalLine.strip()
  colorLine=colorLine.strip()
  #for i
  print("%s\n%s"% (normalLine, colorLine))
  #print("%-80s %s"% (normalLine, colorLine))
  j += 1
#sys.stdout.write(out)


