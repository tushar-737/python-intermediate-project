import time

sentence = "Python is a powerful programming language"

print("Type this sentence:")
print(sentence)

input("Press Enter when ready...")

start = time.time()

typed = input("Start typing: ")

end = time.time()

time_taken = end - start

words = len(sentence.split())
speed = words / (time_taken / 60)

print("Time taken:", round(time_taken, 2), "seconds")
print("Typing speed:", round(speed, 2), "WPM")

if typed == sentence:
    print("Perfect typing!")
else:
    print("There were mistakes.")