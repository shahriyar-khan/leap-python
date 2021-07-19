age = int(input("What is your age?\n"))
decades = age // 10
years = age % 10

print("You are {} decades and {} years old.".format(str(decades), str(years)))