def friendship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2)
    vowels = set('aeiou')

    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10
    
    return min(score, 100)

def message(score):
    if score >= 80:
        return "⭐ Best Friends Forever!!! ⭐"
    elif score >= 60:
        return "🤗 Great Friendship Potential.."
    elif score >= 40:
        return "☺️ A Good Friendship With Room To Grow! "
    elif score >= 20:
        return "😇 You Have Some Things In Common! "
    else:
        return "💗 Every Friendship Starts Somewhere! "

def run_friendship_calculator():
    print("❤️ Friendship Compatibility calculator ❤️")
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")

    score = friendship_score(name1, name2)

    print(f"\nFriendship score: {score}")
    print(message(score))

run_friendship_calculator()