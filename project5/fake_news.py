import random

subjects = ["Narendra Modi", "Sachin Tendulkar"]
actions = ["does yoga", "breaks his bat"]
places = ["on the moon base", "at the tea stall"]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    print(f"\n📰 Breaking News: {subject} {action} {place}!")

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using the Fake News Headline Generator! 😂")
