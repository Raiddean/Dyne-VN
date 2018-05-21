

    #characters
    image dh = "Dyne Happy.png"
    image da = "Dyne_Arcade.png"

    define e = Character("DYNE")

    label start:

    scene bg_conceptv2

    show dh

    e "Hey there big boi."

    e "Wanna play darkstalkers with me?"

    menu:
        "Why not":
            jump ok

        "I'm not playing with you":
            jump destruction

    label destruction:

    e "I will crush you"

    "Oh no I'm going to die"

    return

    label ok:


    e "Alright let's go"

    jump arcade


    label arcade:

    hide dh

    show da

    menu:
        "Play":
            jump existence

    label existence:

    e "Wow, that sure was fun! Say, I'm having a party at my apartment, wanna come?"

    return



    # This ends the game.
