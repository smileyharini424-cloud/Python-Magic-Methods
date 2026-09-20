# Python Magic Methods

## Explanation

Magic methods are special methods in Python that begin and end with double underscores (`__`).

They allow objects to behave like built-in Python objects. In this program, `__str__`, `__len__`, and `__eq__` are demonstrated.

## Problem Statement

Write a Python program to demonstrate magic methods using a Student class.

The program should:

* Display a student object using `__str__`
* Find the number of subjects using `__len__`
* Compare two students using `__eq__`

## Features

* Demonstrates Python magic methods
* Uses classes and objects
* Demonstrates object comparison
* Demonstrates custom string representation
* Demonstrates custom length behavior

## How It Works

1. A `Student` class is created.
2. The constructor stores the student's name and marks.
3. `__str__` defines how the object is displayed.
4. `__len__` returns the number of subjects.
5. `__eq__` compares the marks of two students.
6. Two student objects are created and tested.

## Technologies Used

* Python 3

## Data Structure Used

* List

## Methods Used

* `__init__()`
* `__str__()`
* `__len__()`
* `__eq__()`

## Program Flow

1. Create the `Student` class.
2. Initialize student details.
3. Override the required magic methods.
4. Create two student objects.
5. Display the first student.
6. Find the number of subjects.
7. Compare the marks of both students.

## Sample Input

The program uses the following student data:

```text
Harini: [80, 90, 85]
Anu: [80, 90, 85]
```

## Sample Output

```text
Student Name: Harini, Marks: [80, 90, 85]
Number of Subjects: 3
Same Marks: True
```

## Key Learning

* Understanding magic methods
* Understanding double-underscore methods
* Customizing object behavior
* Using `__str__`, `__len__`, and `__eq__`
* Working with Python classes and objects

## File Location

```text
Python-Magic-Methods/magic_methods.py
```

## Repository Structure

```text
Python-Magic-Methods/
│
├── magic_methods.py
└── README.md
```

## Author

V.Harini
