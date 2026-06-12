import textwrap

Name = input("Enter your name: ").strip()
Profession = input("Enter your profession: ").strip()
Passion = input("Enter your passion in one line: ").strip()
Emoji = input("Enter your favourite emoji: ").strip()
Website = input("Enter your website: ").strip()

print("\nChoose your style: ")
print("1. Simple lines ")
print("2. Vertical flair ")
print("3. Emoji sandwich ")

style = input("Enter 1, 2 or 3: ").strip()

def generate_bio(style):
    if style == "1":
        return f" {Name} {Emoji} \n {Profession} \n my passion is {Passion} \n website: {Website}"
    elif style == "2":
        return f" {Emoji} {Name} \n {Profession}💼 \n {Passion} \n 🌐: {Website}"
    elif style == "3":
        return f" {Emoji*3}\n {Name} - {Profession}⭐🏢💼\n {Passion}\n {Website}🔗 \n {Emoji*3}"
bio = generate_bio(style)
print("\n Your stylish bio: \n")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)

save = input("Do you want to save this bio to a text file? (yes/no): ").lower()

if save == "yes":
    filename = f"{Name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print("file saved")