A=int(input("A="))
B=int(input("B="))
C=int(input("C="))
D=int(input("D="))
if (A>0) and (B>0) and (C>0) and (D>0):
    if (A <= C and B <= D) or (A <=D and B <= C):
        print("A rectangle with sides A,B fits into a rectangle with sides C,D")
    if ((A > C and B > D) or (A > D and B > C)):
        print("A rectangle with sides A,B does not fit into a rectangle with sides C,D")
