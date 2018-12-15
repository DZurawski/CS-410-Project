import pandas as pd

important = []
emails = pd.read_csv("emails_300_set_3.csv")["content"]

for i, email in enumerate(emails):
    print(email)
    response = ""
    while response not in ("y", "n"):
        print(f"({len(important)}, {i}) Is this e-mail important? (y/n)")
        response = input()[0]
        if response == "y":
            important.append(i)
            
print(important)
with open("important_300_set_3.txt", "w") as file:
    print(" ".join(map(str, important)), file=file)