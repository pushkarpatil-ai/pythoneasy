
import csv
from pathlib import Path
import matplotlib.pyplot as plt

FILE = Path("students.csv")


def main():
    if not FILE.exists():
        print("No student data found. Run student_toolkit.py first.")
        return

    with FILE.open("r", newline="", encoding="utf-8") as file:
        students = list(csv.DictReader(file))

    if not students:
        print("No student records available.")
        return

    names = [row["name"] for row in students]
    marks = [float(row["marks"]) for row in students]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(names, marks)

    plt.title("Student Performance Analysis")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.ylim(0, 100)
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    for bar, mark in zip(bars, marks):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            mark + 1,
            f"{mark:.0f}",
            ha="center"
        )

    plt.tight_layout()
    plt.savefig("student_performance.png")
    print("Chart saved as student_performance.png")

    plt.show()


if __name__ == "__main__":
    main()
