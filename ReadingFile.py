def ReadFile(file):
    tuples_list = []

    f = open(file)
    cont = 0

    for line in f:
        if line:
            prefix, value = line.split(' ', 1)

            if prefix == '1':
                tuples_list.append([value.rstrip(), ""])

            elif prefix == '2':
                tuples_list[cont][1] = value.rstrip()
                cont +=1

    print(tuples_list)

    f.close()

ReadFile('IRIDIUM33.txt')