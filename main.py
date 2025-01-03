import csv
import json
from collections import defaultdict

def categorize_grades(grade):
    """Categorize grade based on given grade value."""
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

def categorize_age(age):
    """Categorize age based on given age value."""
    age = int(age)
    if age <= 25:
        return 'young'
    else:
        return 'senior'

def load_students_data(file_path):
    """Load and process student data from CSV file."""
    students_by_category = defaultdict(list)
    all_students = []
    student_id = 1
    
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                grade = int(row['grade'])
                age = int(row['age'])
                grade_category = categorize_grades(grade)
                age_category = categorize_age(age)
                category = f'{grade_category}_{age_category}'
                
                student_data = {
                    'id': student_id,
                    'name': row['name'],
                    'age': row['age'],
                    'grade': row['grade']
                }
                
                students_by_category[category].append(student_data)
                all_students.append(student_data)
                student_id += 1
    except FileNotFoundError:
        print("Error: The file 'std.csv' was not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None
    
    return students_by_category, all_students

def save_data_to_csv(data, file_name):
    """Save the given data to a CSV file."""
    try:
        # Flatten the grouped data
        flattened_data = []
        for category, students in data.items():
            for student in students:
                flattened_data.append(student)
        
        # Write flattened data to CSV
        with open(file_name, 'w', newline='') as csvfile:
            fieldnames = ['number', 'name', 'age', 'grade']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(flattened_data)
        print(f"\nData successfully saved to {file_name}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")


def save_data_to_json(data, file_name):
    """Save the given data to a JSON file."""
    try:
        with open(file_name, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=2)
        print(f"\nData successfully saved to {file_name}")
    except Exception as e:
        print(f"Error saving data to JSON: {e}")

def display_menu():
    """Display the main menu for the user."""
    print("\nStudent Data Selector")
    print("=====================")
    print("1. Select by Grade (A, B, C)")
    print("2. Select by Age Category (senior, young)")
    print("3. Select Output Format (CSV, JSON)")
    print("4. Show All Data")
    print("5. Exit")

def get_user_selection():
    """Get user selections for grade, age category, and output format."""
    selections = {}
    
    # Get grade selection
    while True:
        grade = input("\nEnter grade (A, B, C) or 'all': ").upper()
        if grade in ['A', 'B', 'C', 'ALL']:
            selections['grade'] = grade
            break
        print("Invalid input. Please enter A, B, C, or all.")
    
    # Get age category selection
    while True:
        age_cat = input("Enter age category (senior, young) or 'all': ").lower()
        if age_cat in ['senior', 'young', 'all']:
            selections['age_category'] = age_cat
            break
        print("Invalid input. Please enter senior, young, or all.")
    
    # Get output format selection
    while True:
        output_format = input("Enter output format (csv, json): ").lower()
        if output_format in ['csv', 'json']:
            selections['output_format'] = output_format
            break
        print("Invalid input. Please enter csv or json.")
    
    # Get sorting order
    while True:
        sort_order = input("Enter sorting order (asc, desc): ").lower()
        if sort_order in ['asc', 'desc']:
            selections['sort_order'] = sort_order
            break
        print("Invalid input. Please enter asc or desc.")
    
    return selections

def filter_students_data(categorized_data, selections):
    """Filter the students based on the given selection criteria."""
    filtered = []
    for category, students in categorized_data.items():
        grade, age_cat = category.split('_')
        
        # Check grade and age category match
        grade_match = selections['grade'] == 'all' or selections['grade'] == grade
        age_match = selections['age_category'] == 'all' or selections['age_category'] == age_cat
        
        if grade_match and age_match:
            filtered.extend(students)
    
    return filtered

def sort_and_group_students(filtered_students, sort_order):
    """Sort and group students by grade and age, and add numbering."""
    grouped = defaultdict(list)
    
    sorted_students = sorted(filtered_students, key=lambda x: (x['grade'], x['age']), reverse=(sort_order == 'desc'))
    
    # Group students by grade
    for student in sorted_students:
        grade_category = categorize_grades(int(student['grade']))
        age_category = categorize_age(int(student['age']))
        category = f'{grade_category}_{age_category}'
        grouped[category].append(student)
    
    # Numbering groups and students
    grouped_with_numbers = {}
    for category, students in grouped.items():
        grouped_with_numbers[category] = []
        for index, student in enumerate(students, 1):
            student_data = student.copy()
            student_data['Position'] = index
            grouped_with_numbers[category].append(student_data)
    
    return grouped_with_numbers

def main():
    """Main program function to drive the student data processing."""
    categorized_data, all_data = load_students_data('std.csv')
    if categorized_data is None or all_data is None:
        return

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            grade = input("Enter grade to view (A, B, C): ").upper()
            if grade in ['A', 'B', 'C']:
                filtered = [s for s in all_data if categorize_grades(int(s['grade'])) == grade]
                selections = get_user_selection()
                sorted_and_grouped = sort_and_group_students(filtered, selections['sort_order'])
                print(f"\nStudents with grade {grade}:")
                for category, students in sorted_and_grouped.items():
                    print(f"\nCategory: {category}")
                    for student in students:
                        print(f"  {student['number']}: {student['name']} - Grade: {student['grade']} - Age: {student['age']}")
            else:
                print("Invalid grade selection.")
        
        elif choice == '2':
            age_cat = input("Enter age category (senior, young): ").lower()
            if age_cat in ['senior', 'young']:
                filtered = [s for s in all_data if categorize_age(int(s['age'])) == age_cat]
                selections = get_user_selection()
                sorted_and_grouped = sort_and_group_students(filtered, selections['sort_order'])
                print(f"\n{age_cat.capitalize()} students:")
                for category, students in sorted_and_grouped.items():
                    print(f"\nCategory: {category}")
                    for student in students:
                        print(f"  {student['number']}: {student['name']} - Age: {student['age']} - Grade: {student['grade']}")
            else:
                print("Invalid age category.")
        
        elif choice == '3':
            selections = get_user_selection()
            filtered = filter_students_data(categorized_data, selections)
            sorted_and_grouped = sort_and_group_students(filtered, selections['sort_order'])
            if selections['output_format'] == 'csv':
                save_data_to_csv(sorted_and_grouped, 'selected_students.csv')
            else:
                save_data_to_json(sorted_and_grouped, 'selected_students.json')
        
        elif choice == '4':
            print("\nAll Student Data:")
            for student in all_data:
                print(f"{student['id']}: {student['name']} - Age: {student['age']} - Grade: {student['grade']}")
        
        elif choice == '5':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
