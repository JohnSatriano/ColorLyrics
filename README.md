# ColorLyrics
This program converts lyrics to a colorized phonetic form. It highlights the rhyming patterns by coloring the most used vowel sounds rendered by IPA. See http://jsat.io/blog/2015/10/14/synesthetic-phonetics/ for more details. 

# Usage

~~~~ $ sudo apt-get install espeak
~~~~ $ python3 colorLyrics songFilename
~~~~ $ echo "lyrics" | python3 colorLyrics 
~~~~ $ cat songFilename | python3 colorLyrics 
