life = 3
moves = 0

while True:
    if moves >= 10:
        life -= 1
        print("you lost a life you have",life,"life(s) left")
        moves = 0
        if life == 0:
            print("you lost")
            break

    move = "You are in the magic maze. Which way to go? (N,S,E,W): "
    move = input(move)
    moves += 1

    if move == "S":
        move1 = "right! enter the 2nd command: "
        move1 = input(move1)
        moves += 1

        if move1 == "S":
            move2 = "right! enter the 3rd command"
            move2 = input(move2)
            moves += 1

            if move2 == "N":
                move3 = "right! enter the 4th command"
                move3 = input(move3)
                moves += 1


                if move3 == "W":
                    move4 = "right! enter the 5th command"
                    move4 = input(move4)
                    moves += 1

                    if move4 == "E":
                        move5 = "right! enter the 6th command"
                        move5 = input(move5)
                        moves += 1

                        if move5 == "S":
                            print("congrats you won with",moves,"moves")
                            break
                        else:
                            print("you got wrong try again form the beginning")
                            moves += 1
                            continue
                    else:
                        print("you got wrong try again form the beginning")
                        moves += 1
                        continue
                else:
                    print("you got wrong try again form the beginning")
                    moves += 1
                    continue
            else:
                print("you got wrong try again form the beginning")
                moves += 1
                continue
        else:
            print("you got wrong try again form the beginning")
            moves += 1
            continue
    else:
        print("you got wrong try again form the beginning")
        moves += 1
        continue