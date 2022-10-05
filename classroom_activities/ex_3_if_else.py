## 1
## Try this. Run it more than once.
import random
randomNumber = random.randint(5, 8)
print(f"Here's a random integer: {randomNumber}")


## 1b
## Copy and modify the above example so that the computer will 
## pick numbers between 1 and 4 instead.


## 1c
## Try this. Run it a few times.
import random
randomNumber = random.randint(5, 8)
print(f"Here's a random integer: {randomNumber}")
if randomNumber == 7:
    print("I think some people say this number is lucky.")


## 1d
## Copy and modify the previous example so that the computer
## will pick numbers between 7 and 10 instead.


## 1e
## Copy and modify the previous example so that if the randomly
## chosen number is 10, it will say "Wow, a two digit number!"


## 2
## Try this.
import random
name = random.choice(["bob", "susan", "joe", "anna"])
print(f"Hey {name}.") 
if name == "joe":
    print("Your name rhymes with low.") 
     

## 3
## Copy and modify the above example so that "dell" is one of the names
## that can be randomly chosen.

## 3b
## Copy and modify the above example so that 
## if the name is "dell", it will print "That’s a computer brand." 
     

## 4
## Try this.
import random
age = random.randint(18, 24)
print(f"Pretend that you are {age} years old.")
if age < 21: 
    print("You can't drink alcohol in the US yet.") 
else: 
    print("You are legally allowed to drink. Drink responsibly 😊 ") 
     

## 5
## Copy and modify the above example so that the legal drinking age is 40. (Just to be funny.) 


## 6
## Try this.
thename = input("What is your name? ")
if thename == "george":
    print("Are you named after the first US President?")
else:
    print("Hello.")


## 6b
## Change the previous example so that if the user types "bob", it will reply "Are you the painter?"


## 6c
## Try this. Notice that it will ask for input. 
name = input("What is your name? ") 
if name == "joe": 
    print("Your name rhymes with low.") 
else: 
    print(f"Hey {name}.") 

 
## 7
## Modify the above example so that if the name is "cobb", it will say "That’s a Ft Gordon building!" 


## 7b
## You'll notice that the user must type joe lowercase. Here's how to make it so any capitalization works:
name = input("What is your name? ").lower()
if name == "joe": 
    print("Your name rhymes with low.") 
else: 
    print(f"Hey {name}.") 


## 7c
## Try this. What do you think the != operator means?
name = input("What is your name? ").lower()
if name != "jay": 
    print("Your name is not Jay.") 
print("Greetings.")

    
## 7d
## Copy and modify the previous example like so:
## - Ask the user for a name
## - If the name is anything other than bob, then display "I don't think I know you. I only know Bob."

    
## 8 
## Try this. 
age = 10 
ageNextYear = age + 1 
print(ageNextYear) 
     

## 9
## Try this. Note: you will get an error. 
age = input("How old are you?") 
ageNextYear = age + 1 
print(ageNextYear) 
     

## 10 
## Try this. 
age = int(input("How old are you?")) 
ageNextYear = age + 1 
print(ageNextYear) 


## 11
## Copy and modify the previous example to do the following: 
## - Ask the user for age 
## - Say "I see you are __ years old. You will be 65 years old in __ years."
##   For example, if the user typed 45, then it would display
##      "I see you are 45 years old. You will be 65 years old in 20 years."


## 12
## Try this. Note: you will get an error. 
age = input("How old are you?") 
if age < 21: 
    print("You can't drink alcohol in the US yet.") 
else: 
    print("You are legally allowed to drink. Drink responsibly 😊 ") 
     

## 13
## Modify the above example so it works. You’ll use the `int` function. 

 
## 14
## Copy and modify the above example so that it shows how many years remain until you can drink (but only display that if you’re under the drinking age). 


## 15
## Write a program that takes a name from the user. If the name is the letter "A", say "Your name is just the letter A? That’s kinda cool".  Otherwise, say "Ok, your name is ___". 
     

## 16
## Try this: 
birthyear = 1998 
if birthyear < 2000: 
    print("You were born before 2000.") 
elif birthyear == 2000: 
    print("You were born in 2000.") 
else: 
    print("You were born after 2000.") 

    
## 16b
## Try this:
name = input("What is your name? (type it lowercase please.)")
print("Ok, let me look up that name...")
if name == "bob":
    print("That name used to be common, I think.")
elif name == "sue":
    print("Your name also refers to a legal action.")
elif name == "rob":
    print("Another abbreviation for robert, correct?")
elif name == "lacy":
    print("Does the origin of your name relate to clothing with lace?")
else:
    print("I don't know you.")
print("Done.")

          
## 16c
## Try this. How is it different from the previous example?
## (The difference is subtle, so ask if you are unsure.)
name = input("What is your name? (type it lowercase please.)")
print("Ok, let me look up that name...")
if name == "bob":
    print("That name used to be common, I think.")
if name == "sue":
    print("Your name also refers to a legal action.")
if name == "rob":
    print("Another abbreviation for robert, correct?")
if name == "lacy":
    print("Does the origin of your name relate to clothing with lace?")
else:
    print("I don't know you.")
print("Done.")


## 16d
## Here's an example of using separate if statements:
name = input("What is your name? (type it lowercase please.)").lower()
print("Ok, let me look up that name...")
if name.startswith("z"):
    print("Your name starts with a Z. That is somewhat uncommon in English.")
if len(name) < 3:
    print("Your name is less than 3 characters long.")
if len(name) > 9:
    print("Your name is more than 9 characters long.")
if name == "":
    print("Your name is empty!")


## 17
## Modify the previous example to ask the user for year of birth (using input). 

 
## 18
## Ask the user how many French fries they want. Display different responses depending on how many they request. (Examples: "That’s way too many!", etc.) 

 
## 19
## Try this. Did it print what you expected?
x = int(input("Enter a number: ")) 
if x < 20: 
    print("A") 
    print("B") 
print("C") 


## 20
## Copy and modify the previous example so that C is only printed if the number is not less than 20.
## Use the `else` keyword.

## 20b
## Copy and modify the previous example so that it acts like this:
## if x is less than 20, then print A.
## Otherwise, print C.
## After all of that is done, print Goodbye (regardless of what x was.)


## 21
## Ask the user for a number.
## If the user gives a number more than 50, 
##    then ask "What is your name?"
##    and display "Hello" followed by the name.
## If the user gives any other number,
##    then ask "How did you pick that number?"
##    and regardless of what they say, display "I see."
## After all of that, say "Have a good day."


## 22
## Write a program that takes a number from the user.
## Display the number doubled.
## Then do a sequence of creative if statements of your choice.
##   Some examples: if the number is greater than 30, display "that’s pretty big."
##   If the number is negative, display "Really? Negative? Interesting".  


## 23
## Try this.
x = float(input("Type a number between 0 and 1, for example, 0.3, 0.25, etc... "))
print("One more would be {x + 1}.")

## As you can see, you can use `float` instead of `int` when dealing with non-whole numbers.
## Sidenote: 
## (this sidenote is outside the scope of the class, but good to know)
## Using floats can cause weird rounding errors. For example:
print(1.03 - .42)
## This will print 0.6100000000000001.
## That's quite important when doing comparisons:
if .1 + .1 + .1 == .3:
    print("This will not print.")
else:
    print("This will print... what is math??")
## The reason is because the numbers are converted to binary behind the scenes.
## For more info, see https://docs.python.org/3/tutorial/floatingpoint.html
## If you plan to eventually do any "real-life" programming, then it's definitely worth reading.
## (end of sidenote)

## 23b
## Ask the user for the cost of a single item and the quantity purchased. Print the total cost. 
## Make sure this works for non-integer costs. For example, try a cost of 2.30 and quantity of 2.
## Hint: You'll use float instead of int.
 
## 24
## Modify the previous example so that the shop gives a discount of 10% if you buy at least 20 of an item.  
## For example, if one item costs $5, and you’re buying 20, total cost would be $90. 
     

## 25
## Ask the user for a number. Print the absolute value of the number without using the abs function. 


## 26
## Ask the user for a temperature in Celsius, and display the temperature in Fahrenheit. 


## 27
## Same as previous example, but backwards. 


## 28
## Combine the two previous examples: ask the user for a number and which way to convert. 
          

