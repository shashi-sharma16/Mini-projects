def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")

num_people = int(input("How many people are splitting the bill?: "))
names = []

for i in range(num_people):
    name = input(f"Enter the name of person #{i+1}:").strip()
    names.append(name)

total_bill = get_float("Enter the bill amount in number ony: ")

share = round(total_bill / num_people, 2)

print("\n" + "-" * 40)
print(f"\nTotal bill: {total_bill}")
print(f"\nEach person owes: {share}")

for name in names:
    print(f"{name} owes {share} rupees")

print("\n" + "-" * 40)