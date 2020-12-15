#!/usr/bin/python


def main():
    dico = {19:1,20:2,14:3,0:4,9:5,1:6}
    prev = 1
    max = 30000001
    for turn in range(7 ,max):
        if prev in dico:
            turnspoken = dico[prev]
            speak = turn - 1 - turnspoken
        else:
            speak = 0
        dico[prev]=turn - 1
        prev = speak

    print(turn,speak)



if __name__ == "__main__":
    # execute only if run as a script
    main()


