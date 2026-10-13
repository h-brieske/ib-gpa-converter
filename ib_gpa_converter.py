def ib_to_gpa(ib_score):
    " " "Converts total IB score (0-45) into an approximate US GPA (0-4.0)" " "
    if ib_score < 24:
        return 0.0
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
            print("Please enter a valid number.")

def get_subject_scores():
    " " "Prompts user for 6 subject scores (1-7) and returns them as a list." " "
    scores = []
    print("Enter your 6 subject scores (1-7): ")
    for i in range(1, 7):
        while True:
            try:
                score = int(input(f" Subject {i} grade (1-7): "))
                if 1 <= score <= 7:
                    scores.append(score)
                    break
                print(" --> Please enter a grade between 1 and 7.")
            except ValueError:
                print(" --> Invalid input. Please enter a whole number.")
    return scores

def get_core_bonus():
    " " "Prompts user for Theory of Knowledge / Extended Essay bonus points (0-3). " " "
    while True:
        try:
            bonus = int(input("Enter EE/TOK bonus points (0-3): "))
            if 0 <= bonus <= 3:
                return bonus
            print(" --> Core points must be between 0 and 3.")
        except ValueError:
            print(" --> Invalid input. Please enter a whole number.")
        
def calculate_total_ib(subject_scores, core_bonus):
    " " "Calculates total IB score from 6 subject grades + EE/TOK core bonus." " "
    return sum(subject_scores) + core_bonus

def main():
    print("==========================================")
    print("      IB-to-US-GPA Calculator      ")
    print("==========================================")
    
    scores = get_subject_scores()
    bonus = get_core_bonus()
    
    total_score = calculate_total_ib(scores, bonus)
    
    gpa = ib_to_gpa(total_score)
    
    print("\n------------------------------------------")
    print(f"Total IB Score : {total_score} / 45")
    print(f"Subject Grades : {scores}")
    print(f"Bonus Points   : {bonus}")
    print(f"Approx. US GPA : {gpa} / 4.0")
    print("------------------------------------------")

if __name__ == "__main__":
    main()
