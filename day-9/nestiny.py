#Can nest list and dictionaries in dictionaries. Can you lists or other dictionaries as the Value to the key in the dictionary

# fruit_examples = ["Apple", "Orange", "Bananas"]
# fruit_defintion = "the sweet and fleshy product of a tree or other plant that contains seed and can be eaten as food."
# fruits = {
#     "Examples": fruit_examples,
#     "Definition": fruit_defintion,
# }
# print(fruits["Definition"])

#Other Nesting Example
nesting = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a List in a Dictionary. Each key can only have one value.

travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stugggart"],
        "total_visits": 5
    },
]

print(travel_log[0])

