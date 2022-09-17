with open('file.txt') as f:
    reader = f.readlines()
    line_count = 0
    # print(reader)
    for row in reader:
        print(row)
        word = "02"
        if row.find(word) == 0:
            print("Found")