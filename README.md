War cards game project: By Mordechai Stulman

main file runs the game manager class, which asks for your name, and start a new game



the game manager calls the game class which created a new list with cards, then mix them 1000
times automatically, and devide them card by card to each player.


after that, it calls the function "new_round" which both players cards,
pop the first card, check who wins, and add them to the wiiner packed if someone win,
if noone wins, it doesn't change


after each round there's a called function that check if anyone ran out of cards, and if so
it, return a winner and stops the game

if the user press "Exit" in the main menu, it calls a function that checks who had more card,
find it, returns the winner and stops the game
