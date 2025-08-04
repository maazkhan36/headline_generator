import random

subjects=[
    "babar azam",
    "virat kohli",
    "shahrukhan",
    "ronaldo",
    "john cena",
    "a group of monkeys",
    "prime minister",
]

actions=[
    "launches",
    "cencels",
    "dances with monkey",
    "declares war on",
    "orders",
    "celebrates",
]

places_or_things=[
    "at red fort",
    "in local train",
    "a plate of samosa",
    "inside parliment",
    "in ganga",
    "during match",
    "at gate"
]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(places_or_things)
    
    headline=f"BREAKING NEWS:  {subject} {action} {place_or_thing}"
    print("\n" + headline)
    
    user_input = input("do you want another headline (yes/no)").strip().lower()
    if user_input=="no":
        break
    
print("\nThanks for using the Fake News headline Generator.")