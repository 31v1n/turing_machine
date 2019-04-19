sym = "01B"

tape_inc = "B0101B"
p_inc = ["00R","01R","1BL","21L","10L","f1N","20L","21L","fBR"]

sym_eq = "01AB"
tape_eq = "B001100B"
p_eq=["1BR","2BR","0BR","f1N","10R","3AL","1AR","f0N","3AL","21R","2AR","f0N","30L","31L","3AL","0BR"]

sym_r = "01AB"
tape_r = "B1001BBBBBBB"
p_r = ["","","","","","","",""]

def comp(p,x,sym):
    i = 1 #head position
    q = 0 #current state
    x1 = list(x) #convert the tape (which is a string) into an array
    state = "" 
    while state != "f":
        print "-"*len(x)
        print "".join(x1)
        print " "*i + "^" + "\t" + "state = " + str(q)
        print "-"*len(x)
        aux = p[len(sym)*q + sym.index(x1[i])]
        state = aux[0]
        q = int(state) if state!="f" else 0
        x1[i] = aux[1]
        if(aux[2]=="R"):
            i =  i +1
        elif aux[2] == "L":
            i = i - 1
    return "".join(x1)

print comp(p_eq,tape_eq,sym_eq)
