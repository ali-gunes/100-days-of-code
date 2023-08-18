# On day 3, we are: Studying Control Flow and Logical Operators

# Project 3 - Escape From Jail Cell: Use conditional statements and create a little choice game

print('''     
     \                  ###########                  /
      \                  #########                  /
       \                                           /
        \                                         /
         \                                       /
          \                                     /
           \                                   /
            \_________________________________/
            |                                 |
            |                                 |
            |                                 |
            |            _________            |
            |           |         |           |
            |           |   ___   |           |
            |           I  |___|  |           |
            |           |         |           |
            |           |         |           |
            |           |        _|           |
            |           |       |#|           |  ;,
    -- ___  |           |         |           |   ;'
    H*/   ` |           |         |      _____|    .,`
    */     )|           I         |     \_____\     ;'
    /___.,';|           |         |     \\     \     ."`
    |     ; |___________|_________|______\\     \      ;:
    | ._,'  /                             \\     \      .
    |,'    /                               \\     \
    ||    /                                 \\_____\
    ||   /                                   \_____|
    ||  /              ___________                \
    || /              / =====o    |                \
    ||/              /  |   /-\   |                 \
    //              /   |         |                  \
   //              /    |   ____  |______             \
  //              /    (O) |    | |      \             \
 //              /         |____| |  0    \             \
//              /          o----  |________\             \
/              /                  |     |  |              \
              /                   |        |               \
             /                    |        |             leb
            /                     |        |
''')

print("You woke up in an empty jail cell where no guards can be seen.\nLast night was blurry and your head still "
      "pounds from the cheap booze you shoved down your throat.")
action = input("What do you want to do?\n- Call guards [call]\n- Try to find an escape [search]\n- Lay down and do "
               "nothing [lay]\n").lower()

if action == "search":
    print("You are searching for an escape. You found there is an empty hole behind the toilet. You wiggle it a bit "
          "and discover a tunnel.")
    action = input("What do you want to do?\n- Go through the tunnel [forward]\n- Cover the tunnel and try to forget "
                   "the whole thing [give up]\n").lower()
    if action == "forward":
        print(
            "You head to the tunnel until you saw a beam of light leaking through the end. You rushed to reach it until you hear a noise from the back of your shoulders. They are closing the tunnel. You are stuck here, there is no light no food and no hope. The gods banished you and your misery crushed you. This is the end...")
    else:
        print(
            "You backdown from the tunnel and hide it as best as you can. You sit by the wall with your hands around your head, crying slowly before loosing it hysterically. You try to forget every bit of your existence. Sun starts the set down, soon it will be dark in the cell and you will have no one to turn to, even the mirror won't recognize you. Maybe you should end it all before taking any more pain. Some mistakes are too costly to fix, you got caught in one. Maybe even death is too merciful for you.")
else:
    print("Guards came to check on you, laughed at you and left you to rot. This is a harsh punishment for your life "
          "long actions. You pound your head against the door and repeat the words... *I deserve this*")
