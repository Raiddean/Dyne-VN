

#characters
image dh = "Dyne Happy.png"
image da = "Dyne_Arcade.png"

define e = Character("DYNE")

show dh

label start:

e "Hey there big boi."

e "Wanna play darkstalkers with me?"

menu:
        "Why not":
            "Alright, lets go."




label da:

         show da:
         jump arcade


label arcade:
         menu:
           "Placeholder":
                         e "Wow, that sure was fun! Say, I'm having a party at my apartment, wanna come?"




    # This ends the game.
