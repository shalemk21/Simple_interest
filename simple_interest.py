import sys
def sim_int(p,t,r):
    simp_int=(p*t*r)/100
    return simp_int
if __name__=="__main__":
    p=int(sys.argv[1])
    t=int(sys.argv[2])
    r=int(sys.argv[3])
    print("Simple Interest:", sim_int(p,t,r))
