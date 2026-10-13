def ib_to_gpa(ib_score):
    " " "Converts total IB score (0-45) into an approximate US GPA (0-4.0)" " "
    ib_score < 24:
        return 0.0 #failing grade
    elif ib_score >= 45:
        return 4.0
    else:
        gpa = 2.0 + (ib_score -24) * (2.0 / 21)
        return round(gpa, 2)
def get_valid_score():
    while True:
        try:
            score = int(input("Your total IB score (0-45): "))
            if 0 <= score <= 45:
                return score
            print("Please enter a number between 0 and 45.")
        except ValueError:
            print("Plwase enter a valid number.")

def main():
    print("IB-to-US-GPA Calculator")
    score = get_valid_score()
    gpa = ib_to_gpa(score)
    print(f"IB {score}/45 corresponds to an approximate US GPA of {gpa}")
if __name__ == "__main__":
    main()
    
def ib_to_gpa(ib_score):
    " " "Converts IB-score (0-45) in an approximate US-GPA (0-4.0)" " "
    if ib_score < 24:
        return 0.0 