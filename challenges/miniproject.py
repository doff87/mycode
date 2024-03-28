#!/usr/bin/env python3

def ffxivclasspicker():
    #overall function

    #role choice
    def rolepicker():

        #elicts input from the user to pick a general class archetype
        role_input = input("Please select the number which corresponds to the role you'd like to play in the party:\n" + "1) Tank \n" + "2) Healer\n" + "3) Damage Dealer\n")

        if role_input == "1":
            role = "tank"

        elif role_input == "2":
            role = "healer"

        elif role_input == "3":
            role = "dps"

        else:
            print("You did not make a valid selection.\n")
            rolepicker()

        return role

    #class picker for tanks
    def tankpicker():

        tank_input = input("Please select the number which corresponds to the weapon you'd like to use:\n" + "1) Sword and Shield \n" + "2) Two-handed Axe \n" + "3) Two-handed Sword \n" + "4) Gunblade\n")
    
        if tank_input == "1":
            tank = "Paladin"

        elif tank_input == "2":
            tank = "Warrior"

        elif tank_input == "3":
            tank = "Dark Knight"

        elif tank_input == "4":
            tank = "Gunbreaker"

        else:
            print("You did not make a valid selection.\n")
            tankpicker()

        return tank

    #class picker for healers
    def healerpicker():

        healer_input = input("Please select the number which corresponds to the weapon you'd like to use:\n" + "1) A magical staff\n" + "2) A literal book with fairy companion \n" + "3) A floating globe and deck of cards \n" + "4) Flying swords that also fire lasers \n")

        if healer_input == "1":
            healer = "White Mage"

        elif healer_input == "2":
            healer = "Scholar"

        elif healer_input == "3":
            healer = "Astrologian"

        elif healer_input == "4":
            healer = "Sage"

        else:
            print("You did not make a valid selection.\n")
            healerpicker()

        return healer
    
    #dps are more numerous and have subtypes so this is defining the subfunction for the overall dps class picker
    def dpstypepicker():
        
        dpstype_input = input("Please select the number that corresponds to the type of damage dealer you'd like to play as:\n" + "1) Melee\n" + "2) Physical Ranged\n" + "3) Magical Ranged\n")

        if dpstype_input == "1":
            dpstype = "melee"

        elif dpstype_input == "2":
            dpstype = "ranged"

        elif dpstype_input == "3":
            dpstype = "magical"

        else:
            print("You did not make a valid selection.\n")
            dpstypepicker()

        print("You have selected to play as a", dpstype + "!\n")
        return dpstype

    #the opum magnus of this script, it contains nested if functions and calls on another function to try and get the user to a choice amongst the broadest category of classes
    def dpspicker():

        dpstype = dpstypepicker()

        if dpstype == "melee":
            melee_input = input("Please select the number that corresponds to the weapon you'd like to use:\n" + "1) You bare fists (like a real man)\n" + "2) A spear and the ability to jump higher than airplanes\n" + "3) Daggers and Ninjutsu\n" + "4) A katana and spontaneous cherry blossoms\n" + "5) A scythe and edginess\n")

            if melee_input == "1":
                dps = "Monk"

            elif melee_input == "2":
                dps = "Dragoon"

            elif melee_input == "3":
                dps = "Ninja"

            elif melee_input == "4":
                dps = "Samurai"

            elif melee_input == "5":
                dps = "Reaper"

            else:
                print("You did not make a valid selection.\n")
                dpspicker()

            return dps

        elif dpstype == "ranged":
            ranged_input = input("Please select the number that corresponds to the weapon you'd like to use:\n" + "1) A bow, panache, and a singing voice\n" + "2) Guns and robots \n" + "3) Chakrams and footloose\n")

            if ranged_input == "1":
                dps = "Bard"

            elif ranged_input == "2":
                dps = "Machinist"

            elif ranged_input == "3":
                dps = "Dancer"

            else:
                print("You did not make a valid selection.\n")
                dpspicker()
        
        elif dpstype == "magical":
            magical_input = input("Please select the number that corresponds to the weapon you'd like to use:\n" + "1) A magical staff and forbidden magicks\n" + "2) A literal book and the ability to summon personified elements\n" + "3) A rapier and a whole lot of style\n" + "4) The ability to copy monster abilities and a lower level cap than everyone else")

            if magical_input == "1":
                dps = "Black Mage"

            elif magical_input == "2":
                dps = "Summoner"

            elif magical_input == "3":
                dps = "Red Mage"

            elif magical_input == "4":
                dps = "Blue Mage"

            else:
                print("You did not make a valid selection.\n")
                dpspicker()
        else:
            print("You did not make a valid selection.\n")
            dpspicker()

        return dps

    role = rolepicker()

    print("You have selected to be a", role + "!\n")

    if role == "tank":
        tank = tankpicker()
        print("You should play as a", tank + "!\n")

    elif role == "healer":
        healer = healerpicker()
        print("You should play as a", healer + "!\n")

    elif role == "dps":
       dps = dpspicker()
       print("You should play as a", dps + "!\n")

    else:
        print("You did not make a valid selection.\n")
        ffxivclasspicker()

ffxivclasspicker()
