import datetime

entry = input("What did you learn today? : ").strip()

now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d - %I:%M %p")

journal_entry = (
    f"\n {'-' * 50}"
    f"\n 🗓️ {date_string}"
    f"\n {entry}"
)

while True:
    rating = input("⭐ Rate your productivity today (1-5): ").strip()

    if rating in ["1", "2", "3", "4", "5"]:
        break

    print("Please enter a number between 1 and 5.")

journal_entry += f"\n {'-' * 50}"

with open("learning_journal.txt", "a", encoding="utf-8") as f:
    f.write(journal_entry)

print(f"\n Your journal entry has been saved to 'learning_journal.txt' file")

