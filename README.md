# beginner-project-solutions

## Project List
*Projects are somewhat ordered by increasing difficulty.*
- [x] [99 Bottles](#99-bottles)
- [x] [Magic 8 Ball](#magic-8-ball)
- [x] [Pythagorean Triples Checker](#pythagorean-triples-checker)
- [x] [Rock Paper Scissors Game](#rock-paper-scissors-game)
- [x] [Coin Estimator By Weight](#coin-estimator-by-weight)
- [x] [Mad Libs Story Maker](#mad-libs-story-maker)
- [x] [Change Calculator](#change-calculator)
- [x] [Mean, Median, and Mode](#mean-median-mode)
- [x] [Higher Lower Guessing Game](#higher-lower-guessing-game)
- [x] [Multiplication Table](#multiplication-table)
- [x] [Fibonacci Sequence](#fibonacci-sequence)
- [x] [Base Jumper](#base-jumper)
- [x] [Hangman Game](#hangman-game)
- [x] [Menu Calculator](#menu-calculator)
- [x] [Dice Rolling Simulator](#dice-rolling-simulator)
- [ ] [Count and Fix Green Eggs and Ham](#count-and-fix-green-eggs-and-ham)
- [x] [What's My Number?](#whats-my-number)
- [x] [Factors of a Number](#factors-of-a-number)
- [x] [Countdown Clock](#countdown-clock)
- [x] [Turn Based Pokemon Style Game](#turn-based-pokemon-style-game)
- [x] [A Variation of 21](#a-variation-of-21)
- [x] [Compare Recent reddit Karma](#compare-recent-reddit-karma)
- [ ] [Watch for New TIL Facts](#watch-for-new-til-facts)
- [ ] [Random Wikipedia Article](#random-wikipedia-article)
- [ ] [What's the Weather?](#what’s-the-weather)
- [ ] [Sierpinski Triangle](#sierpinski-triangle)
- [ ] [Two Numbers](#two-numbers)
- [ ] [Chickens and Rabbits](#chickens-and-rabbits)

### 99 Bottles
- [x] Create a program that prints out every line to the song "99 bottles of beer on the wall."
- [x] Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
- [x] Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
- [x] Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

### Magic 8 Ball
- [x] Simulate a magic 8-ball.
- [x] Allow the user to enter their question.
- [x] Display an in progress message(i.e. "thinking").
- [x] Create 20 responses, and show a random response.
- [x] Allow the user to ask another question or quit.
- [x] Bonus:
  - [x] Add a gui.
  - [x] It must have box for users to enter the question.
  - [x] It must have at least 4 buttons:
    - ask
    - clear (the text box)
    - play again
    - quit (this must close the window)
    
### Pythagorean Triples Checker
- [x] If you do not know how basic right triangles work, read this [article on wikipedia](https://en.wikipedia.org/wiki/Pythagorean_triple).
- [x] Allows the user to input the sides of any triangle in any order.
- [x] Return whether the triangle is a Pythagorean Triple or not.
- [x] Loop the program so the user can use it more than once without having to restart the program.

### Rock Paper Scissors Game
- [x] Create a rock-paper-scissors game.
- [x] Ask the player to pick rock, paper or scissors.
- [x] Have the computer chose its move.
- [x] Compare the choices and decide who wins.
- [x] Print the results.
- [x] Subgoals:
  - [x] Give the player the option to play again.
  - [x] Keep a record of the score (e.g. Player: 3 / Computer: 6).

### Coin Estimator By Weight
When some people receive change after shopping, they put it into a container and let it add up over time. Once they fill up the container, they'll roll them up in [coin wrappers](https://en.wikipedia.org/wiki/Coin_wrapper) which can then be traded in at a bank for what they are worth. While most banks will give away coin wrappers for free, it's convenient to have an idea of how many you will need. Instead of counting how many coins you have, it's easier to separate all of your coins, weigh them, and then estimate how many of each type you have and then how many wrappers you'll need.
For example, if you weigh all of your dimes and see that you have 1276.9g of them, you can estimate that you have about 563 dimes (since each one is 2.268g) and you would be able to fill 11 dime wrappers.

Here is the [weight of each coin](https://en.wikipedia.org/wiki/Coins_of_the_United_States_dollar#Coins_in_circulation) and [how many fit inside each type of wrapper](https://en.wikipedia.org/wiki/Coin_wrapper#Amount_in_a_roll_in_the_United_States).
- [x] Allow the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters).
- [x] Print out how many of each type of coin wrapper they would need, how many coins they have, and the estimated total value of all of their 
money.
- [x] Subgoals:
  - [x] Round all numbers printed out to the nearest whole number.
  - [x] Allow the user to select whether they want to submit the weight in either grams or pounds.

### Mad Libs Story Maker
Ever played [Mad Libs](https://en.wikipedia.org/wiki/Mad_Libs)? If you haven't, here are the basics:

"Mad Libs consist of a book that has a short story on each page with many key words replaced with blanks. Beneath each blank is specified a lexical or other category, such as "noun," "verb," "place," or "part of the body." One player asks the other players, in turn, to contribute some word for the specified type for each blank, but without revealing the context for that word. Finally, the completed story is read aloud. The result is usually comic, surreal and somewhat nonsensical."

- [x] Create a Mad Libs style game, where the program asks the user for certain types of words, and then prints out a story with the words that the user inputted.
- [x] The story doesn't have to be too long, but it should have some sort of story line.
- Tip: it's easiest to write out a quick story on a piece of paper or a word document, and then go back through and see which words the user should be able to change.
- [x] Subgoals:
  - [x] If the user has to put in a name, change the first letter to a capital letter.
  - [x] Change the word "a" to "an" when the next word in the sentence begins with a vowel.

### Change Calculator
- Imagine that your friend is a cashier, but has a hard time counting back change to customers.
- [x] Create a program that allows him to input a certain amount of change, and then print how how many quarters, dimes, nickels, and pennies are needed to make up the amount needed.
Example: if he inputs 1.47, the program will say that he needs 5 quarters, 2 dimes, 0 nickels, and 2 pennies.
- [x] Subgoals:
  - [x] So your friend doesn't have to calculate how much change is needed, allow him to type in the amount of money given to him and the price of the item. The program should then tell him the amount of each coin he needs like usual.
  - [x] To make the program even easier to use, loop the program back to the top so your friend can continue to use the program without having to close and open it every time he needs to count change.

### Mean, Median, and Mode
In a set of numbers, the mean is the average, the mode is the number that occurs the most, and if you rearrange all the numbers numerically, the median is the number in the middle.
- [x] Create three functions that allow the user to find the mean, median, and mode of a list of numbers. If you have access or know of functions that already complete these tasks, do not use them.
- [x] Subgoals
  - [x] In the mean function, give the user a way to select how many decimal places they want the answer to be rounded to.
  - [x] If there is an even number of numbers in the list, return both numbers that could be considered the median.
  - [x] If there are multiple modes, return all of them.    
  
### Higher Lower Guessing Game
- [x] Create a simple game where the computer randomly selects a number between 1 and 100 and the user has to guess what the number is.
- [x] After every guess, the computer should tell the user if the guess is higher or lower than the answer.
- [x] When the user guesses the correct number, print out a congratulatory message.
- [x] Subgoals:
  - [x] Add an introductory message that explains to the user how to play your game.
  - [x] In addition to the congratulatory message at the end of the game, also print out how many guesses were taken before the user arrived at the correct answer.
  - [x] At the end of the game, allow the user to decide if they want to play again (without having to restart the program).

### Multiplication Table
- [x] Create a program that prints out a multiplication table for the numbers 1 through 9.
- [x] It should include the numbers 1 through 9 on the top and left axises, and it should be relatively easy to find the product of two numbers. Do not simply write out every line manually (ie print('7 14 21 28 35 49 56 63') ).
- [x] Subgoals:
  - [x] As your products get larger, your columns will start to get crooked from the number of characters on each line. Clean up your table by evenly spacing columns so it is very easy to find the product of two numbers.
  - [x] Allow the user to choose a number to change the size of the table (so if they type in 12, the table printed out should be a 12x12 multiplication table).

### Fibonacci Sequence
If you do not know about the Fibonacci Sequence, read about it [here](https://en.wikipedia.org/wiki/Fibonacci_number).
- [x] Define a function that allows the user to find the value of the nth term in the sequence.
- [x] To make sure you've written your function correctly, test the first 10 numbers of the sequence.
- You can assume either that the first two terms are 0 and 1 or that they are both 1.
- There are two methods you can employ to solve the problem. One way is to solve it using a loop and the other way is to use recursion.
- [x] Try implementing a solution using both methods.

### Base Jumper
- [x] Create a program that converts an integer to the specified base.
- [x] The program should ask for 3 inputs. The number to convert. The base the number is in. And the base to convert the number to.
- [x] The program should accept a base that is in the range of 2 to 16 inclusive.
- [x] Display the result to the user and ask if they want to exit or convert another number.
- [x] Subgoals:
  - [x] Do not display leading zero's in the result.
  - [x] Validate that the number entered is valid for the specified base

### Hangman Game
- [x] Create a program that selects a random word and then allows the user to guess it in a game of hangman.
- [x] Like the real game, there should be blank spots for each letter in the word, and a part of the body should be added each time the user guesses a letter than is not in the answer.
- [x] You may choose how many wrong turns the user can make until the game ends.
- [x] Subgoals:
  - [x] If the user loses, print out the word at the end of the game.
  - [x] Create a "give up" option.

### Menu Calculator
Imagine you have started up a small restaurant and are trying to make it easier to take and calculate orders. Since your restaurant only sells 9 different items, you assign each one to a number, as shown below.

- 1. Chicken Strips - $3.50
- 2. French Fries - $2.50
- 3. Hamburger - $4.00
- 4. Hotdog - $3.50
- 5. Large Drink - $1.75
- 6. Medium Drink - $1.50
- 7. Milk Shake - $2.25
- 8. Salad - $3.75
- 9. Small Drink - $1.25

- [x] To quickly take orders, your program should allow the user to type in a string of numbers and then it should calculate the cost of the order. For example, if one large drink, two small drinks, two hamburgers, one hotdog, and a salad are ordered, the user should type in 5993348, and the program should say that it costs $19.50. 
- [x] Also, make sure that the program loops so the user can take multiple orders without having to restart the program each time.
- [x] Subgoals:
  - [x] If you decide to, print out the items and prices every time before the user types in an order.
  - [x] Once the user has entered an order, print out how many of each item have been ordered, as well as the total price.
  - [x] If an item was not ordered at all, then it should not show up.

### Dice Rolling Simulator
By using the random module, Python can do things like pseudo-random number generation.
- [x] Allow the user to input the amount of sides on a dice and how many times it should be rolled.
- [x] Your program should simulate dice rolls and keep track of how many times each number comes up (this does not have to be displayed).
- [x] Finally, print out how many times each number came up.
- [x] Subgoals:
  - [x] Adjust your program so that if the user does not type in a number when they need to, the program will keep prompting them to type in a real number until they do so.
  - [x] Put the program into a loop so that the user can continue to simulate dice rolls without having to restart the entire program.
  - [x] In addition to printing out how many times each side appeared, also print out the percentage it appeared. If you can, round the percentage to 4 digits total OR two decimal places.
- [ ] Bonus:
  - You are about to play a board game, but you realize you don't have any dice. Fortunately you have this program.
  - [ ] Create a program that opens a new window and draws 2 six-sided dice
  - [ ] Allow the user to quit, or roll again
  - [ ] Allow the user to select the number of dice to be drawn on screen(1-4) 
  - [ ] Add up the total of the dice and display it

### Count and Fix Green Eggs and Ham
Some of you may remember the Dr. Sues story "Green Eggs and Ham". For those of you that don't remember it or have never heard of it, [here](http://pastebin.com/XMY48CnN) is the story. However, there is a problem with the story I gave you - every time the word I is used, it is lowercase.

Because of this problem, your job is to do the following:

- [ ] Copy the story I gave you into a regular text file.
- [ ] Create a program that reads through the story and makes the letter i uppercase any time it should be. (Make sure to change it when it's used in sam-I-am's name too.)
- [ ] Have your program make a new file, and have it write out the story correctly.
- [ ] Print out how many errors were corrected.
- [ ] When you're finished, you should have corrected [this many](https://i.imgur.com/GRkj3yz.jpg) errors.

### What’s My Number?
Between 1 and 1000, there is only 1 number that meets the following criteria:

- [x] The number has two or more digits.
- [x] The number is prime.
- [x] The number does NOT contain a 1 or 7 in it.
- [x] The sum of all of the digits is less than or equal to 10.
- [x] The first two digits add up to be odd.
- [x] The second to last digit is even and greater than 1.
- [x] The last digit is equal to how many digits are in the number.

To find out if you have the correct number, click [here](https://i.imgur.com/jbz4nJ4.jpg).

### Factors of a Number
- [x] Define a function that creates a list of all the numbers that are factors of the user's number.
  For example, if the function is called factor, `factor(36)` should return `[1, 2, 3, 4, 6, 9, 12, 18, 36]`.
- [x] The numbers in your list should be sorted from least to greatest, and 1 and the original number should be included.
- [x] Remember to consider negative numbers as well as 0.
- [x] Bonus:
  - [x] Have the program print the factors of the users number in a comma separated string, without a comma after the last number, and without the brackets of a Python list.
  - [x] If the user's number is prime, note it.

### Countdown Clock
- [x] Create a program that allows the user to choose a time and date, and then prints out a message at given intervals (such as every second) that tells the user how much longer there is until the selected time.
- [x] Subgoals:
  - [x] If the selected time has already passed, have the program tell the user to start over.
  - [ ] If your program asks for the year, month, day, hour, etc. separately, allow the user to be able to type in either the month name or its number.
  - TIP: Making use of built in modules such as time and datetime can change this project from a nightmare into a much simpler task.

### Turn Based Pokemon Style Game
- [x] Write a simple game that allows the user and the computer to take turns selecting moves to use against each other.
- [x] Both the computer and the player should start out at the same amount of health (such as 100), and should be able to choose between the three moves:
  - [x] The first move should do moderate damage and has a small range (such as 18-25).
  - [x] The second move should have a large range of damage and can deal high or low damage (such as 10-35).
  - [x] The third move should heal whoever casts it a moderate amount, similar to the first move.
- [x] After each move, a message should be printed out that tells the user what just happened, and how much health the user and computer have. Once the user or the computer's health reaches 0, the game should end.
- [x] Subgoals:
  - [x] When someone is defeated, make sure the game prints out that their health has reached 0, and not a negative number.
  - [x] When the computer's health reaches a set amount (such as 35%), increase it's chance to cast heal.
  - [x] Give each move a name.

### A Variation of 21
If you do not know how 21 (AKA Blackjack) is played, reading the first couple of paragraphs of [this](https://en.wikipedia.org/wiki/Blackjack) wikipedia article may be beneficial.

In this project, you will make a game similar to Blackjack. In this version:
- [x] There is only one player.
- [x] There are two types of scores: the game score and the round score.
- [x] The game score will begin at 100, and the game will last for five rounds.
- [x] At the beginning of the round, the player is given two random cards from a deck and they will be added together to make the player's round score.
- [x] From here, the player has two options - draw another card to try to get their round score closer to 21, or they can end the round.
- [x] The player can draw as many cards as they want until they end the round or their round score exceeds 21.
- [x] At the end of the round, the difference between 21 and the round score is subtracted from the game score, and then the next round begins. After the five rounds, the player is given their total score and the game is over.

---Other Information About The Game---
- Aces are only worth 1.
- If a player busts, 21 is subtracted from their total score.
- All face cards are worth 10.
- So the point of your program is to allow the user to play the game described above.

- [x] Subgoals:
  - [x] At the beginning of each round, print the round number (1 to 5).
  - [x] Since this is a text base game, tell the user what is happening. For example, tell him/her when he/she draws a card, the name of the card, when they bust, etc.
  - [x] Create a ranking system at the end of the game and tell the user their rank. For example, if the player finishes with 50-59 points they get an F, 60-69 is a D, 70-79 is a C, 80-89 is a B, and 90-100 is an A.
  - [x] At the end of each round, print out the user's total score.
  - [x] This may be the hardest part of the project, depending on how you wrote it. Make sure the deck has 4 of each type of card, and then remove cards as they are drawn. At the end of each round, make the deck have all of the cards again.

### Compare Recent reddit Karma
Since we're all redditors here, let's make something dealing with reddit. If you go to a user's profile and add .json to the end of it, you can get the all sorts of Json data about the user (think of Json as a giant dictionary of smaller dictionaries and lists). For example, if I go to my own profile and view it's Json data, it would look like this[1]. At first it might look intimidating, but if you break it down, you can see it's just one giant dictionary with all sorts of information about my latest posts.

- [x] Create a program that gets information about two different users, and then sees whose most recent post received the most karma.
- [x] The program should then print out which user received more karma, and what the difference was.
- This is a pretty open project, so I encourage you to take it further by adding more features if you find it interesting.
- Remember - Elements in a list are referenced by their index numbers while entries in a dictionary are referenced by their keys.
- [x] Subgoals:
  - [x] Allow the user to put in the name of two different users when the program first begins.
  - [x] If one of the names of the users does not exist (because of a spelling error), print out a message saying so.
  - [x] Allow the user to keep comparing other users until the program is closed.
  - [x] Display the amount of upvotes and downvotes each user received for their posts.
- Not sure how to turn json data into usable python data? Check [this](http://www.pythonforbeginners.com/python-on-the-web/parse-json-objects-in-python/) out.

### Watch for new TIL facts
If you finished the previous [project](https://github.com/alfredmuffin/Beginner-Projects#compare-recent-reddit-karma) which compared the karma of two new comments, hopefully you learned a thing or two about receiving data from Reddit's API. Now you're going to take this a step further, and even have the opportunity to make a basic twitter bot.
- Create a program that receives data from the [/r/todayilearned](https://reddit.com/r/todayilearned) subreddit, and looks for new facts that have been posted.
- Each time the program comes across a new fact, the fact should be printed into the command line. However, phrases like "TIL ", "TIL that", etc should be removed so the only thing that is printed is the fact.

[New TIL API data here](https://www.reddit.com/r/todayilearned/new/.json)

There are a couple things to note about this since you'll more than likely be using a loop to check for new posts. According to Reddit's [API Access Rules Page](https://github.com/reddit/reddit/wiki/API), the API pages are only updated once every thirty seconds, so you'll have to have your code pause for at least thirty seconds before it tries to find more posts. Secondly, if for some reason you decide to try to get data sooner than every thirty seconds, make sure to not send more than thirty requests per minute. That is the maximum you are allowed to do.

There is actually a lot you can do once your program starts receiving facts. Instead of simply printing the facts, here are some ideas for what you can do with them. If you currently do not feel like you can accomplish these ideas, feel free to come back later when you have more experience.
- [ ] Print the link to the source of the fact too.
- [ ] Try to further clean up the fact by adding punctuation to the end if it is missing, capitalize the first word, etc.
- [ ] Write the facts to a separate text file so you end up with a giant compilation of random facts.
- [ ] Create a bot that posts the facts to twitter. This may sound hard, but it's actually pretty simple by using the [Python Twitter Tools](https://pypi.python.org/pypi/twitter) module and following the guide posted [here](https://wilsonericn.wordpress.com/2011/08/22/tweeting-in-python-the-easy-way/).
- [ ] Remember, the maximum amount of characters you can use in a tweet is only 140, so you'll have to filter out facts that are longer than that.
- [ ] By now you should be pretty familiar with python, so if you get ideas for improving your program, go for it!

### Random Wikipedia Article
If you've been to Wikipedia, you may have noticed that there is a link to a random article on the left side of the screen. While it can be fun to see what article you get taken to, sometimes it would be nice to see the name of the article so you can skip it if it sounds boring. Luckily, Wikipedia has an API that allows us to do so [Click here](https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json).
However, there is a dilemma. Since Wikipedia has articles about topics from all over the world, some of them have special characters in the title. For example, the article about the spanish painter [Erasto Cortés Juárez](https://en.wikipedia.org/wiki/Erasto_Cort%C3%A9s_Ju%C3%A1rez) has é and á in it. If you look at this specific article's [API](https://en.wikipedia.org/w/api.php?action=query&prop=info&pageids=39608394&inprop=url&format=json), you will see that the title is "Erasto Cort\u00e9s Ju\u00e1rez" and that the \u00e9 and \u00e1 are replacing the two previously mentioned letters. (For information about what this is, start by checking out the first half of [this page](https://docs.python.org/2/howto/unicode.html) in the documentation). To make your program work, you're going to have to handle this problem somehow.
- [ ] Create a program that pulls titles from the official Wikipedia API and then asks the user one by one if he or she would like to read about that article.
- Example:
  - [ ] If the first title is Reddit, then the program should ask something along the lines of "Would you like to read about Reddit?" If the user says yes, then the program should open up the article for the user to read.
  - HINT: Click [here](https://en.wikipedia.org/wiki?curid=39608394) to see how the article's ID can be used to access the actual article.
- [ ] Subgoals:
  - [ ] As mentioned before, do something about the possibility of unicode appearing in the title.
  - [ ] Whether you want your program to simply filter out these articles or you want to actually turn the codes into readable characters, that's up to you.
  - [ ] Make the program pause once the user has selected an article to read, and allow him or her to continue browsing different article titles once finished reading.
  - [ ] Allow the user to simply press ENTER to be asked about a new article.

### What’s the Weather?
If you would like to know the basics of what an API is, check out [this](http://www.reddit.com/r/explainlikeimfive/comments/qowts/eli5_what_is_api/c3z9kok) post by iamapizza.
- [ ] Create a program that pulls data from OpenWeatherMap.org and prints out information about the current weather, such as the high, the low, and the amount of rain for wherever you live.
- [ ] Subgoals:
  - [ ] Print out data for the next 5-7 days so you have a 5 day/week long forecast.
  - [ ] Print the data to another file that you can open up and view at, instead of viewing the information in the command line.
  - [ ] If you know html, write a file that you can print information to so that your project is more interesting. Here is an example of the results from what I threw together.[3]
- Tips:
  - APIs that are in Json are essentially lists and dictionaries. Remember that to reference something in a list, you must refer to it by what number element it is in the list, and to reference a key in a dictionary, you must refer to it by it's name.
  - Don't like Celsius? Add &units=imperial to the end of the URL of the API to receive your data in Fahrenheit.

### Sierpinski Triangle

The [Sierpinski triangle](https://en.wikipedia.org/wiki/Sierpinski_triangle) (also with the original orthography Sierpinski), also called the Sierpinski gasket or the Sierpinski Sieve, is a fractal and attractive fixed set with the overall shape of an equilateral triangle, subdivided recursively into smaller equilateral triangles. Originally constructed as a curve, this is one of the basic examples of self-similar sets, i.e., it is a mathematically generated pattern that can be reproducible at any magnification or reduction. It is named after the Polish mathematician _Waclaw Sierpinski_, but appeared as a decorative pattern many centuries prior to the work of Sierpinski.

Task in hand :

-  [ ] create and visualize a fractal generator that forms a standard ***sierpinski triangle***.
- [ ] perform this using recursive calls.

- [ ] Subgoals :
  - [ ] Also accept ***depth*** for which the fractal should be generated.

### Two Numbers

Given an array of integers, return indices of the ***two numbers*** such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
```
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```
### Chickens and Rabbits

Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.
