**Python OOPs assignment **

This repository contains solutions to five object-oriented programming (OOP) practice problems in Python. Each question demonstrates key OOP concepts like inheritance, polymorphism, method overriding, multiple inheritance, and method overloading simulation.

---

## 1. Drone Fleet Management
- *Concepts Used*: Multiple Inheritance
- *Description*: Designed a system to manage a fleet of drones. A Device class stores basic info, a Flyer class simulates flight, and the Drone class inherits both and includes capture_image().

## 2. Library Access System
- *Concepts Used*: Inheritance, Instance Attributes
- *Description*: Developed a simple library system. Member is the base class, and StudentMember allows borrowing, returning books, and viewing status.

## 3. Online Learning Platform
- *Concepts Used*: Multi-Level Inheritance, Method Overriding
- *Description*: A class hierarchy of User, Instructor, and CourseCreator was implemented. Each class overrides display_info() to reflect specific roles.

## 4. Smart Home Appliance
- *Concepts Used*: Polymorphism
- *Description*: A base class Appliance is extended by Fan, Light, and AC, each overriding the status() method. Devices are stored in a list and demonstrate polymorphism.

## 5. Geometry Toolkit
- *Concepts Used*: Method Overloading (Simulated with default parameters)
- *Description*: A single method area() behaves differently based on the number of arguments — calculates area of a circle or rectangle accordingly.

---

## How to Run

Each question is implemented in a separate Python file (q1.py, q2.py, etc.)  
Run them using:

```bash
python q1.py
