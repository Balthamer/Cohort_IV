import hashlib

hashed = hashlib.md5(input("What do you want to hash? ").encode("UTF-8")).hexdigest()
with open("shadow.txt","w") as file:
    file.write(f"{hashed}\n")
