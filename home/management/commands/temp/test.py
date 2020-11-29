import ast

with open("addresses.csv", "r") as data:
    dictionary = ast.literal_eval(data.read())
    for a in dictionary:
        for b in dictionary[a]:
            for c in dictionary[a][b]:
                if " linn" in c:
                    print(c)
