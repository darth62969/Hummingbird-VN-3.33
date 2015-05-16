# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image eileen happy = "Hirohito.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:

    show eileen happy
   
    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return
