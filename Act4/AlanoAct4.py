import os
import pickle

class StudentRecord:
    def __init__(self, student_id, full_name, class_standing, major_exam):
        self.student_id = student_id
        self.full_name = full_name
        self.class_standing = class_standing
        self.major_exam = major_exam

    def __repr__(self):
        return f"ID: {self.student_id}, Name: {self.full_name[0]} {self.full_name[1]}, Class Standing: {self.class_standing}, Major Exam: {self.major_exam}"

def calculate_grade(class_standing, major_exam):
    return (class_standing * 0.6) + (major_exam * 0.4)

def open_file(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    return []

def save_file(filename, records):
    with open(filename, 'wb') as file:
        pickle.dump(records, file)

def show_all_records(records):
    for record in records:
        print(record)

def order_by_last_name(records):
    return sorted(records, key=lambda x: x.full_name[1])

def order_by_grade(records):
    return sorted(records, key=lambda x: calculate_grade(x.class_standing, x.major_exam), reverse=True)

def show_student_record(records, student_id):
    for record in records:
        if record.student_id == student_id:
            print(record)
            return
    print("Student not found.")

def add_record(records, student_id, full_name, class_standing, major_exam):
    records.append(StudentRecord(student_id, full_name, class_standing, major_exam))

def edit_record(records, student_id, full_name=None, class_standing=None, major_exam=None):
    for record in records:
        if record.student_id == student_id:
            if full_name:
                record.full_name = full_name
            if class_standing:
                record.class_standing = class_standing
            if major_exam:
                record.major_exam = major_exam
            return
    print("Student not found.")

def delete_record(records, student_id):
    for record in records:
        if record.student_id == student_id:
            records.remove(record)
            return
    print("Student not found.")

def main():
    records = []
    filename = None

    while True:
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter filename to open: ")
            records = open_file(filename)
        elif choice == '2':
            if filename:
                save_file(filename, records)
            else:
                print("No file opened.")
        elif choice == '3':
            filename = input("Enter filename to save as: ")
            save_file(filename, records)
        elif choice == '4':
            show_all_records(records)
        elif choice == '5':
            records = order_by_last_name(records)
            show_all_records(records)
        elif choice == '6':
            records = order_by_grade(records)
            show_all_records(records)
        elif choice == '7':
            student_id = input("Enter student ID: ")
            show_student_record(records, student_id)
        elif choice == '8':
            student_id = input("Enter student ID: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            class_standing = float(input("Enter class standing grade: "))
            major_exam = float(input("Enter major exam grade: "))
            add_record(records, student_id, (first_name, last_name), class_standing, major_exam)
        elif choice == '9':
            student_id = input("Enter student ID: ")
            first_name = input("Enter new first name (leave blank to keep current): ")
            last_name = input("Enter new last name (leave blank to keep current): ")
            class_standing = input("Enter new class standing grade (leave blank to keep current): ")
            major_exam = input("Enter new major exam grade (leave blank to keep current): ")
            edit_record(records, student_id, 
                        (first_name, last_name) if first_name and last_name else None, 
                        float(class_standing) if class_standing else None, 
                        float(major_exam) if major_exam else None)
        elif choice == '10':
            student_id = input("Enter student ID: ")
            delete_record(records, student_id)
        elif choice == '11':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()