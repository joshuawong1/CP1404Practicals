import random
def main():
    number_limit = 6
    minimum_number = 1
    maximum_number = 45
    number_of_quick_picks = int(input("Enter amount of quick picks: "))
    while number_of_quick_picks < 0:
        print("Enter a valid number of quick picks: ")
        number_of_quick_picks = int(input("Enter amount of quick picks: "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(number_limit):
            number = random.randint(minimum_number, maximum_number)
            while number in quick_pick:
                number = random.randint(minimum_number, maximum_number)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
