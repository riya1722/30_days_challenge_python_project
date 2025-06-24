import random

subjects = [
    "Narendra Modi",
    "Sachin Tendulkar",
    "Virat Kohli",
    "Ratan Tata",
    "Mukesh Ambani",
    "Sundar Pichai",
    "Satya Nadella",
    "Deepika Padukone",
    "Amitabh Bachchan",
    "PV Sindhu",
    "Neeraj Chopra",
    "Dr. K. Sivan",
    "Arijit Singh",
    "Kiran Bedi",
    "Mary Kom",
    "MS Dhoni",
]

actions = [
    "does yoga",
    "teaches cricket to aliens",
    "breaks his bat",
    "adopts a dog as CEO",
    "launches internet for birds",
    "codes a chai-making robot",
    "merges Teams and WhatsApp",
    "dances on a moving train",
    "forgets movie dialogues",
    "smashes mosquito mid-match",
    "throws javelin with a love note",
    "launches rocket with GPS voice",
    "sings lullabies to traffic",
    "gives tickets on hoverboard",
    "knocks out punching bags",
    "finishes chess with helicopter move",
]

places_or_things = [
    "at the tea stall",
    "in a cricket stadium",
    "on the moon base",
    "from the Mars colony",
    "on a Bollywood set",
    "near a traffic signal",
    "at the rocket launchpad",
    "inside a chai-making robot",
    "riding a hoverboard",
    "in a helicopter",
    "at the Jio tower",
    "inside a secret laboratory",
    "from an alien spaceship",
    "inside an underwater library",
    "on a flying scooter",
    "using a quantum computer",
    "on a karaoke stage",
    "inside a virtual reality cave",
    "at a talking ATM",
    "in a WiFi-enabled cow shed",
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places_or_things)

    headline = f"\n Breaking News: {subject} {action} {place}!"
    print("\n" + headline) 

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using the Fake News Headline Generator! ")

