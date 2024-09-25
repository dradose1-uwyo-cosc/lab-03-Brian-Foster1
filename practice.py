names = ["Brandon", "Brian", "Yousef", "Meshref"]
print("Original", names)

del names[1]
print ("without me", names)

names.append("Ben")
print(names)

for name in names:
    print(f"{name} is at my table")