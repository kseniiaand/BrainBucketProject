# Exercise 1
keep_going = True
while keep_going:
    user_input = input("Type anything ,or type STOP to exit\n").lower()
    if user_input == "stop":
        break
    print("You typed '", user_input, "'")


# Exercise 2
my_dict = {'Jake': '$100K', 'Anand': '$120K'}
for key, value in my_dict.items():
    print(key, "makes ", value,  "a year")


# Exercise 3
my_tuple = (4, 30, 2017, 2, 27)
print('{} {} {} {} {}'.format(my_tuple[3], my_tuple[4], my_tuple[2], my_tuple[0], my_tuple[1]))