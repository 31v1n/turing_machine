def comp(p,x,sym):
    i = 1 #head position
    q = 0 #current state
    x1 = list(x) #convert the tape (which is a string) into an array
    state = "" 
    while state != "f":
        #print the tape and the current position of the head along with the state
        print(len(x)*"-")
        print("".join(x1))
        print(" "*i + "^")
        print("state = " + str(q))
        print("-"*len(x))
        aux = p[len(sym)*q + sym.index(x1[i])]
        state = aux[0]
        q = int(state) if state!="f" else 0
        x1[i] = aux[1]
        if(aux[2]=="R"):
            i =  i +1
        elif aux[2] == "L":
            i = i - 1
    return "".join(x1)

