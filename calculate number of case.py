def string_test(s):
    d = {"u_case": 0, "l_case": 0}
    for c in s:
        if c.isupper():
            d["u_case"] += 1
        elif c.islower():
            d["l_case"] += 1
        else:
            pass
    print("The number of Uppercase characters : ", d["u_case"])
    print("The number of Lowercase characters : ", d["l_case"])


sentence = input("Enter a string : ")
string_test(sentence)
