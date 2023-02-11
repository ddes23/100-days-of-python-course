#https://datagy.io/python-get-dictionary-key-with-max-value/

bid_records = {
    "Dustin": 45,
    "Rachel": 85,
    "Andreas": 105,
    "Tucker": 26,
}

#this is printing the max, but going in alpabetical order of the keys in the dicitonary
max_age = max(bid_records)

#The max function is looking for the highest value in 'ages' but because told the function the key to use is the ages.get which will pull the values of the keys in 'ages'
winner = max(bid_records, key=bid_records.get)
print(winner)

print(bid_records["Dustin"])
print(bid_records.get("Dustin"))