bid_total = {}

name = input("What is your name")
bid = int(input("what is your bid").replace("$", ""))
continue_flow = input("Is anyone in room? Yes/No")
bid_total[name] = bid


while continue_flow == "Yes":
    name = input("What is your name")
    bid = int(input("what is your bid").replace("$", ""))
    continue_flow = input("Is anyone in room? Yes/No")
    bid_total[name] = bid



max_bid = max(bid_total.values())

winner_list = list()
for key in bid_total:
    if bid_total[key] == max_bid:
        winner_list.append(key)


print(f"{winner_list} is the winner")