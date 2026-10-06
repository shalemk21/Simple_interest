def sim_int(p,t,r):
    simp_int=(p*t*r)/100
    return simp_int
if __name__=="__main__":
    p=10000
    t=2
    r=5
    print("Simple Interest:", sim_int(p,t,r))
