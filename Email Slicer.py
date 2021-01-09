email = str(input())
letters = []
count = 0

if "@" in email:
    for i in range(50):
        try:
            letters.append(email[i])
        except:
            break

    for i in range(len(letters)):
        if letters[i] == "@":
            break
        else:
            count += 1

    username = ""
    remove_letters = []

    for i in range(count):
        username += letters[i]
        remove_letters.append(letters[i])

    print(username)

    for i in range(len(remove_letters)):
        letters.remove(remove_letters[i])

    letters.remove("@")

    host = "mail."

    for i in range(len(letters)):
        host += letters[i]

    print(host)

else:
    print(f'"{email}" is not a valid email address')
    input()
    exit()