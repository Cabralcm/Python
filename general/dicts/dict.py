#Python Code related to popular Dictionary expressions

def dict_keys(D):
    for k in D.keys():
        print D[k]

def dict_k_v(D):
    for k,v in D.items():
        print(k,":",v)
        print(f"{k}:{v}")
        