"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730405513"
 $ python -m exercises.ex01_chardle
Enter a 5-character word: snake
Enter a single character: e
Searching for e in snake
e found at index 4
1 instance of e found in snake

$ python -m exercises.ex01_chardle
Enter a 5-character word: ships
Enter a single character: s
Searching for s in ships
s found at index 0
s found at index 4
2 instances of e found in ships

$ python -m exercises.ex01_chardle
Enter a 5-character word: ships
Enter a single character: f
Searching for f in ships
No instances of f found in ships

$ python -m exercises.ex01_chardle             
Enter a 5-character word: dill
Error: Word must contain 5 characters

$ python -m exercises.ex01_chardle
Enter a 5-character word: candles
Error: Word must contain 5 characters

$ python -m exercises.ex01_chardle
Enter a 5-character word: ships
Enter a single character: car
Error: Character must be a single character.

$ python -m exercises.ex01_chardle
Enter a 5-character word: ships
Enter a single character: 
Error: Character must be a single character.

$ python -m exercises.ex01_chardle
Enter a 5-character word: ships
Enter a single character: h
Searching for h in ships
h found at index 1
1 instance of h found in ships
