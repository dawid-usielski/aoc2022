with open('input.txt', 'r') as file:
    sum = 0
    arr = []
    for line in file:
        if line.strip('\n') != "":
            sum += int(line.strip('\n'))
        if line.strip('\n') == "":
            arr.append(sum)
            sum = 0
    print(max(arr))