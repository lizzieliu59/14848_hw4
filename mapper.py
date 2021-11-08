import sys

valid_set = {'0', '1', '4', '5', '9'}

for line in sys.stdin:
    line = line.strip()
    date = line[15:23]
    temperature = line[87:92]
    if temperature[1:] == '9999':
        continue
    quality = line[92]
    if quality not in valid_set:
        continue
    print('%s\t%s' % (date, temperature))