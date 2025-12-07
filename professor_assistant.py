import random

def load_question_bank(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n") for line in f]
    except Exception as e:
        print("Error opening file:", e)
        return None

    if len(lines) % 2 != 0:
        print("Warning: question bank doesn't have an even number of lines.")
     
    pairs = []
    for i in range(0, len(lines) - 1, 2):
        q = lines[i].strip()
        a = lines[i+1].strip()
        if q != "" and a != "":
            pairs.append((q, a))
    return pairs

def create_exam(pairs, num, out_path, professor_name):
    if pairs is None or len(pairs) == 0:
        print("No valid question-answer pairs to use.")
        return False

    available = len(pairs)
    if num > available:
        print("Requested", num, "pairs but only", available, "available. Using all available.")
        num = available

    selected_indices = set()
    while len(selected_indices) < num:
        idx = random.randint(0, available - 1)
        selected_indices.add(idx)

    selected_indices = list(selected_indices)

    try:
        with open(out_path, "w", encoding="utf-8") as out:
            out.write("Professor: " + professor_name + "\n\n")
            out.write("Exam (" + str(num) + " questions)\n\n")
            qnum = 1
            for idx in selected_indices:
                q, a = pairs[idx]
                out.write(str(qnum) + ". " + q + "\n")
                out.write("Answer: " + a + "\n\n")  
                qnum += 1
    except Exception as e:
        print("Error writing exam file:", e)
        return False

    return True

def main():
    print("Welcome to professor assistant version 1.0.")
    prof_name = input("Please Enter Your Name: ").strip()
    if prof_name == "":
        prof_name = "Professor"

    print("Hello Professor.", prof_name + ", I am here to help you create exams from a question bank.")

    while True:
        choice = input("Do you want me to help you create an exam (Yes to proceed | No to quit the program)? ").strip().lower()
        if choice == "no" or choice == "n":
            print("Thank you professor", prof_name + ". Have a good day!")
            break
        elif choice == "yes" or choice == "y":
            path = input("Please Enter the Path to the Question Bank: ").strip()
            pairs = load_question_bank(path)
            if pairs is None:
                print("Could not load question bank. Try again.")
                continue
            print("Yes, indeed the path you provided includes questions and answers.") if len(pairs) > 0 else print("No valid pairs found.")

            try:
                num_str = input("How many question-answer pairs do you want to include in your exam? ").strip()
                num = int(num_str)
                if num <= 0:
                    print("Number must be positive. Using 1.")
                    num = 1
            except:
                print("Invalid number. Using 1.")
                num = 1

            out_file = input("Where do you want to save your exam? ").strip()
            if out_file == "":
                out_file = "exam.txt"

            success = create_exam(pairs, num, out_file, prof_name)
            if success:
                print("Congratulations Professor", prof_name + ". Your exam is created and saved in", out_file + ".")
            else:
                print("Failed to create exam. Try again.")

            again = input("Do you want me to help you create another exam (Yes to proceed | No to quit the program)? ").strip().lower()
            if again == "no" or again == "n":
                print("Thank you professor", prof_name + ". Have a good day!")
                break
            else:
                pass
        else:
            print("Please answer Yes or No.")

if __name__ == "__main__":
    main()
