# This small programs will show some properties of the "for loop".

for letter in "Joana Mucogllava":
    print(letter)


friends = ["Joana", "Utku", "Nora"]

for friend in friends:
    print(friend)


for index in range(10):
    print(index)

for index in range(6, 10):
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First Interation")
    else:
        print("Not first")
