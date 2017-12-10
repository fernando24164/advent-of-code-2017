# part 1
valid_passphrase = 0
with open('data.txt', 'r') as input_data:
    for line in input_data:
        words=line.replace('\n','').split(' ')

        if(len(words) == len(set(words))):
            valid_passphrase += 1

print(valid_passphrase)

# part 2
valid_passphrase = 0
with open('data.txt', 'r') as input_data:
    for line in input_data:
        words=line.replace('\n','').split(' ')

        for index, element in enumerate(words):
            words[index] = ''.join(sorted(element))

        if(len(words) == len(set(words))):
            valid_passphrase += 1

print(valid_passphrase)