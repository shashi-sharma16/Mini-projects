import datetime

Name = input("What is your name?: ").strip()
Age = input("How old are you?: ").strip()
City = input("Which city do you live in?: ").strip()
Profession = input("What is your profession?: ").strip()
Hobby = input("What is your favourite hobby?: ").strip()

intro_message = (
    f" Hello! My name is {Name}. I'm {Age} years old and live in {City}. "
    f"\n I work as a {Profession}, and my favourite hobby is {Hobby}." 
    f"\n Nice to meet you!"
)

current_date = datetime.date.today().isoformat()
intro_message += f"\n Logged on: {current_date}\n"

border = "*" * 80
final_output = f"{border}\n{intro_message}\n{border}"

print("\n" + final_output)