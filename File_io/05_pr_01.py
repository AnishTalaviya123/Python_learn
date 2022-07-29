with open("poems.txt", "r") as f:
    if('Twinkle 'in f.read()):
        print("Yes Twinkle  is present")
    else:
        print("The Word Twinkle is not present")