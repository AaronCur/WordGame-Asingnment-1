# WordGame!
## Assignment #1 - Web Development & Databases

When started, your WordGame program selects a word of seven or more letters from a dictionary.
This word is known as the source word. The source word is displayed on screen, and the game
records the current timestamp value.
The user of the game now has to think up seven three-or-more letter words made up from the letters
contained within the source word(entering one at a time), and they have to do this as quickly as possible. Each word is
entered into the game which then – once the seven words are entered – records another timestamp
value.

### Upon receipt of the seven words, the game checks to ensure that:
1. each word is made up from letters contained within the source word,
2. each word exists within the dictionary (i.e., it's a “real” word),
3. the words all have three letters or more,
4. there are no duplicates, and
5. none of the seven submitted words is the source word.

If the seven words meet the above criteria, the game computes how long the process took using the
two timestamp values, recording the amount of time taken. The game then asks for the user's name
to add to the Top Scorers List.
Upon receipt of the name, the game adds the user's name and their time into the appropriate place
within the Top Scorers List then displays the current “Top 10” entries from the Top Scorers List.
And, of course, because this game is so cool, the user willingly accepts your kind offer to play again
(or, if they’re a spoilsport, they quit).

### Points to note:
1. If one or more of the seven words are invalid, the game needs to tell the user which words
were wrong, and display an appropriate “error” message2.
2. If the user does not make the Top 10, they should be told where they were placed within the
list (e.g., “Nice try, Rafael: You were ranked 4396th. Better luck next time.”).
3. Case is not an issue here. So, “PET” is the same as “Pet” - that is, they are NOT two different
words.

## Installation and Deployment
Code runs out of the box and can be ran through command prompt(cmd) or equivellent(anaconda prompt)
In your prompt window navigate to where you saved the wordgame folder
Then type "python wordgame.py" to run the game!
When testing this game things got very competitve in the lab trying to beat everyones top scores.
Feel free to download this game and try climb the leaderboard and get into that top 10!
A highscore table is provided with scores from some of my class mates for you to try compete against! (One was incredibly quick)
However if you want to start from fresh you can delete the "highscoretable.pickle" file and the game will create a blank new one !
Enjoy!

## Credit
Aaron Curry
