# ==============================
#  Typing Practice CLI by Utkarsh — 10 Level Edition
# ==============================

import time

def clear():
    print("\n" * 2)

def wait():
    input("\nPress ENTER to continue...")

def age_check():
    print("Hyy there, My name is Utkarsh Raj and I am the creator of this App...")
    print("In this Application you will be provided with an interface where you can practice and enhance your writing skills..")
    print("Enter your age:")
    try:
        age = int(input(": "))
    except:
        print("Invalid Input! Please enter a number.")
        quit()

    if age > 18:
        print("\nWelcome To Typing Practice by Utk.corp:")
        print("Thank You For Choosing this App..")
    elif age > 0:
        print("\nWelcome To Typing Practice by Utk.corp,")
        print("As you are a junior you can not get Access to the Advance Package!")
    else:
        print("!!Invalid Age!!")
        quit()

def measure_typing(text):
    print("\n--->", text)
    start_time = time.time()
    user_input = input("Type here: ")
    end_time = time.time()
    duration = end_time - start_time

    words_typed = len(user_input.split())
    wpm = round((words_typed / duration) * 60, 2)
    correct = int(user_input == text)
    return correct, wpm

def typing_level(lines, level_no):
    clear()
    print(f"========== Level {level_no} ==========")
    print("Type the exact text shown.\n")

    correct_count = 0
    total_wpm = 0

    for text in lines:
        correct, wpm = measure_typing(text)
        total_wpm += wpm
        correct_count += correct
        if correct:
            print(f"✔ Correct  | WPM: {wpm}")
        else:
            print(f"✘ Incorrect | WPM: {wpm}")

    accuracy = (correct_count / len(lines)) * 100
    avg_wpm = total_wpm / len(lines)

    print(f"\nAccuracy: {accuracy:.1f}%")
    print(f"Average WPM: {avg_wpm:.1f}")

    return accuracy, avg_wpm


def main():
    age_check()
    wait()
    clear()

    levels = [
        [
            "Python is an interpreted object-oriented high-level programming language with dynamic semantics",
            "Its high-level built in data structures combined with dynamic typing and dynamic binding make",
            "as well as for use as a scripting or glue language to connect existing components together"
        ],
        [
            "In Python, no need to take care about low-level details such as managing the memory used by the program.",
            "Linux: Python comes preinstalled with popular Linux distros such as Ubuntu and Fedora.",
            "There are no separate compilation and execution steps like C and C++."
        ],
        [
            "The Zen of Python emphasizes simplicity and readability.",
            "Indentation is used to define code blocks instead of curly braces.",
            "Python supports functional, object oriented and procedural programming styles."
        ],
        [
            "A variable in Python does not need a declared type.",
            "Python’s garbage collection handles memory cleanup automatically.",
            "List comprehensions provide a concise way to create lists."
        ],
        [
            "The print function can display formatted output using f-strings.",
            "Python supports exception handling through try and except blocks.",
            "Tuples are immutable sequences in Python."
        ],
        [
            "Dictionaries store data in key value pairs.",
            "The range function generates integer sequences efficiently.",
            "String slicing allows extracting substrings easily."
        ],
        [
            "Recursion is supported in Python but has a default depth limit.",
            "Generators yield items one at a time using the yield keyword.",
            "Lambda functions allow small anonymous operations."
        ],
        [
            "Modular programming is encouraged by dividing code into reusable modules.",
            "The standard library provides extensive built in functionality.",
            "Virtual environments isolate project dependencies."
        ],
        [
            "External packages can be installed using pip.",
            "PEP guidelines standardize Python coding styles.",
            "The community driven nature of Python accelerates improvements."
        ],
        [
            "Python remains one of the most popular languages globally.",
            "Its flexibility makes it suitable for beginners and professionals alike.",
            "You have now completed this 10 level typing challenge!"
        ]
    ]

    for i in range(10):
        acc, wpm = typing_level(levels[i], i + 1)
        
        if acc < 60:
            print("\n❗ Result: FAILED — Your accuracy is too low.")
            print("Try again to improve!")
            return
        
        print("\n🎉 Level Passed!")
        wait()

    print("\n===================================")
    print("🎉🎉 CONGRATULATIONS — You completed all 10 levels!!! 🎉🎉")
    print("===================================")

# ============================
#  Start Application
# ============================

main()
