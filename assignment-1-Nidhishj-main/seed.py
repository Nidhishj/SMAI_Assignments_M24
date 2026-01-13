import hashlib
seed = int(hashlib.sha256("nidhish.jain".encode()).hexdigest(),16) %(2**32)
with open("seed.txt", "w") as f:
    f.write(str(seed))