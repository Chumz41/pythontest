import modone

mod1.get_user_name()



def introduction2(name):
    print(f" {name}! Intro \nEven in the cold there exist creatures that thrive in it. seems that they are not very keen on visitors.")
    print("Scene \nNearing the other side of the detour starts hearing un natural noises. Slowly turn to see dire wolfs")
    print("Player actions \n-	Move closer to figure out what they are doing\n-	See what would have been a small campsite\n-	Oh no got to close agro them\n-	face head on die (Return to chap 1)")
    print("-	Run away while still getting attacked (Stamina dropping fast)\n-	Survive 1 HP left")


def main():
    user_name = get_user_name()
    introduction2(user_name)

    print("You are infront of the wolves. What do you do?")
    print("1. Run away")
    print("2. Face them head on")

    user_choice = input("Type 1 for choice 1 or type 2 for choice 2: ")

    if user_choice == '1':
        print("You live but are gravely injured")
    elif user_choice == '2':
        print("You have died at the hand of the wolves restart from chap 1")


if __name__ == "__main__":
    main()


