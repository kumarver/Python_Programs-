with open("aaa.csv", "r") as f:
    data = f.read()
    list = []
    for line in data:
        print "*******"
        print line
