def get_user_name():
    name = input("Enter your name for the game: ")
    return name

def introduction(name):
    print(f"Welcome, {name}! Your story begins now.")
    print("I am walking on snow that never seems to end. The cold winds howl at you as if to envelop you more in its domain.")
    print("Scene \nThief is walking around the snow trying to get a place that is not cold.")
    print("Player actions \n-Just walking, walking on uneven snow (take 1 damage of cold)\n- Nears a tall snowy mountain-Cannot go right through\n- elects to turn around it (take 1 damage of cold))")



def main():
    user_name = get_user_name()
    introduction(user_name)


if __name__ == "__main__":
    main()
