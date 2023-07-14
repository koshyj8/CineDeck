def push(N):
    NoVowel = []
    for i in N:
        for j in i:
            if j.lower() not in ['a','e','i','o','u']:
                NoVowel.append(i)
    return NoVowel

All = []

for i in range(5):
    All.append(input("Enter Word: "))

NoVowel = push(All)

for i in NoVowel:
    print(i)
    if NoVowel.index(i) == len(NoVowel) - 1:
        print("Stack Empty")