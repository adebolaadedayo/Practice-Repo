#Create a function to print a list of names that are greater than 4 letters
#Combine using a for loop and an if conditional statement
def print_words(words):
    for w in words:
        if len(w) > 4:
            print(w) #the result is to get the words that fulfil the condition
            
#List of words
words = ["Ability", "Man", "Adebola", "Apply"]

print_words(words)

#List of words with the variable "people"
people = ["people", "attendance"]

print_words(people)