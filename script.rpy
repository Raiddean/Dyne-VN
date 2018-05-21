

#characters
image dh = "Dyne_Happy.png"
image da = "Dyne_Arcade.png"

define e = Character("DYNE")

    show dh

    e "Hey there big boi."

    e "Wanna play darkstalkers with me?"


    menu:
        e "Wanna play darkstalker's with me?"
    label start:

        "Sure":
            e "Alright, lets go."

            label jump arcade:
            jump arcade

            label da:
            show da
            
            "Nah man, I'm good":
            e "get out of here you insec"
            return






















    label arcade:
           e "Wow, that sure was fun! Say, I'm having a party at my apartment, wanna come?"


































    # This ends the game.

    return
