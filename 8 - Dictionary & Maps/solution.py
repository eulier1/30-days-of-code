n = int(input())

phone_book = {}

for i in range(0, n):
    data = str(input()).split(" ")
    name = data[0]
    phone = int(data[1])
    phone_book[name] = phone

while True:
    try:
        name = str(input())
        if name in phone_book:
            print("{}={}".format(name,phone_book[name]))
        else:
            print("Not found")
    except EOFError:
        break
