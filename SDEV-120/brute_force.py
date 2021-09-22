import hashlib
import string
import itertools
with open ("shadow.txt","r") as fShadow:
    for line in fShadow:
        for x in range(1,25):
            res = itertools.product(string.printable[:-6],repeat = x)
            for i in res:
                hashed = hashlib.md5(''.join(i).encode("UTF-8")).hexdigest()
                if hashed == line[:-1]:
                    print(f"\n\nCRACKED\n\n{hashed}    {''.join(i)}\n\nThe password is {''.join(i)}")
                    quit()
