import time

def typing_speed_test():
    text = (
        "Python is a powerful programming language used for web development "
        "data science artificial intelligence and automation"
    )

    print("\nTyping Speed Test")
    print("-" * 50)
    print("Type the given text:\n")
    print(text)
    print("\n click enter when ready\n")
    input()

    start_time = time.time()
    typed_text = input("Type here:\n")
    end_time = time.time()

    time_taken = end_time - start_time

    words = typed_text.split()
    word_count = len(words)

    wpm = (word_count / time_taken) * 60

    correct_chars = 0
    for i in range(min(len(text), len(typed_text))):
        if text[i] == typed_text[i]:
            correct_chars += 1

    accuracy = (correct_chars / len(text)) * 100

    print("\nResults")
    print("-" * 50)
    print(f"Time Taken     : {round(time_taken, 2)} seconds")
    print(f"Typing Speed   : {round(wpm, 2)} WPM")
    print(f"Accuracy       : {round(accuracy, 2)} %")

typing_speed_test()
