def TOH(n,a,b,c):
    if n > 0:
        TOH(n-1,a,c,b)
        print(f"From {a} to {c}")
        TOH(n-1,b,a,c)
        

TOH(5,1,2,3)