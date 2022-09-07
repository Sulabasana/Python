with open('file.txt') as f:
    reader = f.readline()
    line_count = 0
    for row in reader:
        print(row)