user_data = open('gender_seperator/user_data.txt', "r")

male = open('gender_seperator/male.txt', "w")
female = open('gender_seperator/female.txt', "w")
other = open('gender_seperator/other.txt', "w")

for line in user_data:
    # name_list = name.split()
    name_list = line.split(" ")
    # hint  - name        - gender      - age    
    # print(name_list[0], name_list[1], name_list[2])

    # male
    if name_list[1] == 'M':
        male.write(line)

    # female
    if name_list[1] == 'F':
        female.write(line)

    # other
    if name_list[1] == 'O':
        other.write(line)