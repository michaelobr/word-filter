# Project Name: Word Filter

# Description 
The purpose of this project is to be able to filter certain words from an inputted string. At first I started with mapped values of swear words to symbols such as #&$!, however I soon found out that arrays accomplished the task at hand much more easily. Also, letting the user pick which words (whether they be appropriate or inappropriate) to filter instead of having a predefined set, voids the potential of people reading the source code to become disgruntled. 

Example
```
Please enter the words (case sensitive) that you'd like to filter out: Marx
Enter some words: Karl Marx was a distinguished individual. 
Karl %^#$ was a distinguished individual. 
```

# Known Bugs
The currently only know bug is when a word that is desired to be filtered out is attached with any form of punctuation (i.e. ,!.?), the word is not properly bleeped. 
