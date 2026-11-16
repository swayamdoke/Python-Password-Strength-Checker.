
import re

def check_password(password):
    score = 0

    if len(password) >= 12:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[@#$%&*!]", password):
        score += 1

    print("\n--- Password Security Report ---")

    if score <= 2:
        print("Password Strength: Weak")
    elif score <= 4:
        print("Password Strength: Medium")
    else:
        print("Password Strength: Strong")

    print("Security Score:", score, "/ 5")


print("===== PASSWORD STRENGTH CHECKER =====")

password = input("Enter a sample password: ")
check_password(password)
