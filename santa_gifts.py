"""
A script to exchange Christmas gifts between people.
List of people write into people.txt file.
Output with connected people will be in santas_list.txt file.
"""

import random


def main():
    people = []
    with open("people.txt") as f:
        for line in f:
            people.append(line.strip("\n"))

    result = draw(people)
    while result == False:
        result = draw(people)

    with open("santas_list.txt", "w") as f:
        for k in result:
            f.write(f"{k} : {result[k]}\n")
        f.write("\nHappy Christmas!\n")


def draw(people):
    choosen = [False for person in people]
    result = {}
    for i, person in enumerate(people):
        rand = random.randint(0, len(people) - 1)
        attempts = 0
        while rand == i or choosen[rand] == True:
            if attempts >= len(people):
                return False
            rand = random.randint(0, len(people) - 1)
            attempts += 1
        choosen[rand] = True
        result[person] = people[rand]

    return result


if __name__ == "__main__":
    main()
