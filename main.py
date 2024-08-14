def main():
    user_input = input("Do you want all players to get Black Jake? Y/N\n")
    all_black_jacks = True if (user_input=='Y') else False
    print(all_black_jacks)
    user_input = input("How many milliseconds per shuffle?")
    try:
        val = int(user_input)
        txt = "I'll print a new shuffle every {} milliseconds.".format(val)
        print(txt)
    except ValueError:
        print("I need a number. Please rerun the program.")

if __name__ == "__main__":
    main()
