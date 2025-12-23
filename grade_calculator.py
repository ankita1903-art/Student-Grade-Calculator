def marks(b): 
     if 90 <= b <= 100:
        return "A", "EXCELLENT!Keep it up."
     elif 80 <= b <= 89:
        return "B", "Very good!Try to improve more."
     elif 70 <= b <= 79:
        return "C", "Focus more in your study."
     elif 60 <= b <= 69:
        return "D", "Poor!work haed." 
     else:
        return "F", "Don't give up learn and try."
def main():
    while True:
        a = input("Enter student's name: ")
        
        try:
            b= int(input("Enter marks(0-100): "))
            if 0<= b <= 100:
                break
            else:
                print("Invalid input!please enter number between 0-100")
                
        except ValueError:
            print("Please enter numerics only.")
            continue
            
    grade, message = marks(b)
     
    print("\n RESULT FOR", a)
    print(f"Marks: {b}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")

main()
     
     
