with open('words_alpha.txt', 'r') as infile:
    with open('dictionary.txt', 'w') as outfile:
        for line in infile:
            if len(line[:-1]) > 4:
                outfile.write(line)