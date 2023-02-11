import os
import art

def clear():
    os.system('clear')

print(art.logo)

bid_records = {}
auction_open = True

while auction_open:
    name = input("\nWhat is your name?: ")
    bid = int((input("What is your bid?: $")))
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ")
    bid_records[name] = bid
    if other_bidder == "yes":
        auction_open == True
        clear()
    else:
        auction_open = False
        clear()

winner = max(bid_records, key=bid_records.get)
print(f"The winner is {winner} with a bid of ${bid_records[winner]}")




