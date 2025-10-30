import random

secret_number=random.randint(1,100)

print("\n👋Hello Gamers😊")

print("\n🎉🎉Welcome to The Guessing the Number game!!!🎉🎉")

print("\n🤔Let me think of a number")


attempts=0
#Game Loop

while True:
    guess=input("Enter your guess, if you want to give up type 'exit'\n")

    if guess.lower()=="exit":
        print(f"Oh my!! You gave up, but the number was {secret_number}")
        print("😜 😝 😆 😂 🤪 😏 😛 😹 🤭")
        break
    
    if not guess.isdigit():
        print("User please enter a valid number.")
        continue
    
    attempts += 1
    guess=int(guess)

    if(guess>secret_number):
        print("📈Too High!, Try again😂")
    elif(guess<secret_number):
        print("📉Too low!!, Try again😂")
    else:
        print(f"🎉 Congrats!!. You got the right number in {attempts} attempts")
        break
