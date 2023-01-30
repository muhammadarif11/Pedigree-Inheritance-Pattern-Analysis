
def main():
    text = "PEDIGREE INHERITANCE PATTERN ANALYSIS. (^-^*)/"
    ins = "Instructions: "
    inst = "Please read the prompt and answer accordingly and answer after the 'A: '\n'1' for YES, and '0' for NO."
    print("")
    title = "\033[1m" + "\u0332".join(text) + "\033[0m"
    print(title)
    # Intro
    bolded_string = "\033[1m" + ins + inst + "\033[0m"
    print(bolded_string)
    print("")
    value = int(input("Is the DNA passed exclusively from the mother to all her children? A: "))
    if value > 0:
        print("Mitochondrial Inheritance")
    elif value < 1:
        second = int(input("Is the trait affecting only boys and their father? A: "))
        if second > 0:
            print("\nYour result is....\nY-linked inheritance")
        elif second < 1:
            third = int(input("Is there equal dispersion between the sexes? A: "))
            if third > 0:
                forth = int(input("Is there a generational skip? A: "))
                if forth > 0:
                    print("\nYour result is....\nAutosomal Recessive")
                elif forth < 1:
                    print("\nYour result is....\nAutosomal Dominant")
            elif third < 1:
                fifth = int(input("Is there a generational skip? A: "))
                if fifth < 1:
                    sixth = int(input("Do all the boys have an (only) affected mother, \nand all the affected daughters have one affected parent? A: "))
                    if sixth > 0:
                        print("\nYour result is....\nX-linked dominant")
                    elif sixth < 1:
                        seventh = int(input("Are all the daughters of affected fathers all carriers,\n and is there lack of father-to-son inheritance? A: "))
                        if seventh > 0:
                            print("\nYour result is....\nX-linked recessive")
                        elif seventh == 0:
                            print("Hmm that doesn't make sense. Review your data and try again.")
                elif fifth > 0:
                    eighth = int(input("Are all the daughters of affected fathers all carriers, \nand is there lack of father to son inheritance? A: "))
                    if eighth > 0:
                        print("\nYour result is....\nX-linked recessive")
                    elif eighth < 1:
                        ninth = int(input("Do all the boys have an (only) affected mother,\nand all the affected daughters have one affected parent?"))
                        if ninth > 0:
                            print("\nYour result is....\nX-linked dominant")
                        elif ninth < 1:
                            print("Hmm that really does not make sense. Try again after reviewing your data.")
    else:
        print("Hmm that doesn't make sense. Try again and review your data.")

    restart = input("Do you want to try again? Please enter 'yes' or 'no' ").lower()
    if restart == "yes":
        main()
    else:
        print("Bye! ")


main()
