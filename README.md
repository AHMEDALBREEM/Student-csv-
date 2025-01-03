# Student Data Management System

## Video Demo:  <https://youtu.be/FTvwOBYQDsc>

## Github Demo:  <https://github.com/AHMEDALBREEM/Student-csv->


## Description

The **Student Data Management System** is a Python-based application designed to manage and process student data efficiently. The system allows users to load student data from a CSV file, categorize students based on their grades and age, filter and sort the data according to user preferences, and save the processed data in either CSV or JSON format.

## Key Features

- **Data Loading**: The system loads student data from a CSV file (`std.csv`), which includes fields such as `name`, `age`, and `grade`.
- **Categorization**:
  - **Grades**: Students are categorized into grades (A, B, C, D, F) based on their numerical grade.
  - **Age**: Students are categorized as either 'young' (age ≤ 25) or 'senior' (age > 25).
- **Filtering and Sorting**:
  - Users can filter students by grade (A, B, C) or age category (young, senior).
  - The system allows sorting of students in ascending or descending order based on their grades or age.
- **Data Export**:
  - The processed data can be saved in either CSV or JSON format.
- **User Interface**:
  - A simple command-line interface (CLI) is provided for users to interact with the system.

## How It Works

### 1. Data Loading
The system reads student data from a CSV file (`std.csv`) and categorizes each student based on their grade and age.

### 2. User Interaction
Users are presented with a menu to select options such as:
- Filtering by grade, age category, or sorting order
- Selecting the output format (CSV or JSON)
- Viewing all data

### 3. Data Processing
Based on user selections, the system filters and sorts the student data.

### 4. Data Export
The processed data is saved in the selected format (CSV or JSON) for further use or analysis.

## Example Usage

1. **Load and run the script**:
   Ensure that the `std.csv` file is in the same directory as the Python script. Run the script with the following command:

   ```bash
   python main.py
