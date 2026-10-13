
import csv
from pathlib import Path
from statistics import mean

FILE = Path("students.csv")
students = []


def load_students():
    if not FILE.exists():
        return

    with FILE.open("r", newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            students.append({
                "name": row["name"],
                "marks": float(row["marks"])
            })


def save_students():
    with FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["name", "marks"]
        )
        writer.writeheader()
        writer.writerows(students)


def add_student():
    name = input("Student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        marks = float(input("Marks (0-100): "))
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    students.append({"name": name, "marks": marks})
    save_students()
    print(f"Student {name} added successfully!")


def show_students():
    if not students:
        print("No student records found.")
        return

    for student in sorted(
        students, key=lambda item: item["marks"], reverse=True
    ):
        print(f"{student['name']}: {student['marks']:.2f}")


def show_analytics():
    if not students:
        print("Add students before viewing analytics.")
        return

    average = mean(s["marks"] for s in students)
    topper = max(students, key=lambda s: s["marks"])

    print(f"\nNumber of students: {len(students)}")
    print(f"Class average: {average:.2f}")
    print(f"Topper: {topper['name']} ({topper['marks']:.2f})")


def main():
    load_students()

    while True:
        print("\n=== AI & ML Student Toolkit ===")
        print("1. Add student")
        print("2. View students and ranking")
        print("3. View analytics")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            show_analytics()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1-4.")


if __name__ == "__main__":
    main()
