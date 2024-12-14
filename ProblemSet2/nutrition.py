
'''
Problem Set 2
Program: Nutrition Facts
Alexis Varas Ortiz
'''

def main():
    #Dict for fruits(keys) and calories(values)
    fruit_calories = {
        "apple" : "130",
        "avocado" : "50",
        "banana" : "110",
        "cantaloupe" : "50",
        "grapefruit" : "60",
        "grapes" : "90",
        "honeydew" : "50",
        "kiwifruit" : "90",
        "lemon" : "15",
        "lime" : "20",
        "nectarine" : "60",
        "orange" : "80",
        "peach" : "60",
        "pear" : "100",
        "pineapple" : "50",
        "plums" : "70",
        "strawberries" : "50",
        "sweet cherries" : "100",
        "tangerine" : "50",
        "watermelon" : "80"
    }

    #Prompt user to enter a fruit(convert the str to lowercase)
    fruit = input("Item: ").lower()

    #Output the calories(value) of the respective fruit if it is found in the dict
    if fruit in fruit_calories:
        print(f"Calories: {fruit_calories[fruit]}")


main()
