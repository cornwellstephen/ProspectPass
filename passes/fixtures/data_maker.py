import sys
import readline

count = 1
print('[')

max = 5207
f = open("ptondirectory", "r")

while count < max:
    line = str.split(f.readline())
    print('\t\t{')
    print('\t\t\t\"model\": \"passes.Student\",')
    sys.stdout.write('\t\t\t\"pk\": ')
    sys.stdout.write(str(count))
    print(',')

    print('\t\t\t\t\"fields\": {')
    sys.stdout.write('\t\t\t\t\t \"username\": \"')
    sys.stdout.write(line[2])
    print('\",')
    sys.stdout.write('\t\t\t\t\t \"NetId\": \"')
    sys.stdout.write(line[2])
    print('\",')
    sys.stdout.write('\t\t\t\t\t \"first_name\": \"')
    sys.stdout.write(line[0])
    print('\",')
    sys.stdout.write('\t\t\t\t\t \"last_name\": \"')
    sys.stdout.write(line[1])
    print('\",')
    sys.stdout.write('\t\t\t\t\t \"user_club\": \"')
    sys.stdout.write('None')
    print('\"')

    print('\t\t\t}')
    sys.stdout.write('\t\t}')
    if count < max - 1:
        print(',')
    else:
        print('')
    count = count + 1

print(']')

f.close()