import turing_machine as tm

#increment a binary number by one
sym = "01B"
tape_inc = "B0101B"
p_inc = ["00R","01R","1BL","21L","10L","f1N","20L","21L","fBR"]

#Find if a number has the same number of 0 and 1
sym_eq = "01AB"
tape_eq = "B001100B"
p_eq=["1BR","2BR","0BR","f1N","10R","3AL","1AR","f0N","3AL","21R","2AR","f0N","30L","31L","3AL","0BR"]

#reverse a binary number
sym_r = "01AB"
tape_r = "B1010110BBBBBBBBB"
p_r = ["00R","01R","","1BL","2AR","3AR","","fBN","20R","21R","","40L","30R","31R","","51L","40L","41L","10L","","50L","51L","11L"]

print(tm.comp(p_r,tape_r,sym_r))

