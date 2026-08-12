def calculate_grade(score):
    if score >= 90 and score <=100:
        return "A".strip()
    elif score >= 80 and score <=89:
        return "B".strip()
    elif score >= 70 and score <= 79:
        return "C".strip()
    elif score >= 60 and score <=69:
        return "D".strip()
    else:
        return "You Need work hard"
print(calculate_grade(90))
print(calculate_grade(81))
print(calculate_grade(55))


if __name__ == "__main__":
 print("Error")
 