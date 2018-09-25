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
- [ ] [Factors of a Number](#factors-of-a-number)
- [ ] [Countdown Clock](#countdown-clock)
- [ ] [Turn Based Pokemon Style Game](#turn-based-pokemon-style-game)
- [ ] [A Variation of 21](#a-variation-of-21)
- [ ] [Compare Recent reddit Karma](#compare-recent-reddit-karma)
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
