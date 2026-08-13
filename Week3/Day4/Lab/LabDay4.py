
# Practice: List Comprehension Basics

numbers = [1, 2, 3, 4, 5] # Exprsion
#  # comperhenshon Line 3,  atretion
squares = [
    number ** 2
    for number in numbers    # => close
    if number %2 ==1      # =>  filltring

]

print(squares)



# Practice: Math Operations in List Comprehension

prices = [10, 25, 40]

pricees_with_vat = [
    round(price * 1.15, 2)
    for price in prices
    
]
print(pricees_with_vat)



# Practice: Filtering with Conditions

scores = [42, 67, 91, 58, 75]

passing_score = [
    score
    for score in scores
    if score >= 60
]

print(passing_score)



# Practice: String Manipulation in Comprehensions

raw_names = ["sara","", "OMAR", "  lina"]

clean_names = [
    name.strip().title()
    for name in raw_names
    if name.strip()

]
print(clean_names)



# Practice: Nested Loops in List Comprehension

numbers = [1, 2, "F"]

letters = ["A", "B"]

pairs = [
    (number, letter)
    for number in numbers 
    for letter in letters
]
print(pairs)



# Practice: If-Else (Ternary) in Comprehensions

scores = [42, 67, 91]

labels = [
    "pass" if score >= 60 else "retry"
    for score in scores
]
print(labels)



# Practice: Set Comprehensions

emails = [
    "SARA@EXAMPLE.com",
    "omer@example.com",
    "lina@school.sa"
]

domains = {
    email.split("@")[1].lower()
    for email in emails
}
print(domains)



# Practice: Dictionary Comprehensions

numbers = range(1, 10)

squares = {
    number : number **2
    for number in numbers
   
    
}
print(squares)