# WebScraping-
WebScraping with Python

Charles Huang 10/28/2016
github.com/chuang93

Project Goals:

The project will use python webscraping to analyze your current head-to-head fantasy matchup with an opponent, maximizing your chances of winning. It will see which of the categories (e.g points, rebounds) you are losing to your opponents in and by how much. It will then find players based on averages and projections and see if you can trade for these players or pick them up off the waiver wire in order to help you beat your opponents before the end of the week. The program will find which players you should drop in order to mitigate "loss categories" and see if you can trade them for players that will help you bump up "win categories", and determine the number of additional categories you could win by the end of the week if you make these changes. The program will be able to scrape data and make predictions at any time.

Definitions:

1. Categories: 9-Category fantasy leagues include total points, rebounds, assists, turnovers, steals, blocks, 3PT made, FG% and FT%. 
2. Loss Categories: Categories where dropping players can improve them including FG%, FT%, and Turnovers.
3. Win Categories: Categories that improve when adding players including points, rebounds, assists, steals, blocks, and 3PT made. 


Stories:

1. Program can display current running totals of 9 categories for your team as well as for the other team, and calculate differences in order to determine amount needed to beat opponent.
2. Program can determine players on your team that should be dropped to minimize "loss categories".
3. Program can determine players on waiver wire that can be picked up to maximize chances of winning "win categories".
4. Program can determine trades between other teams in your league that will improve chances of winning specific categories for the week.



Dependencies:

1. lxml -> html
2. requests