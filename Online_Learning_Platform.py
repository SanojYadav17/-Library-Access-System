class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display_info(self):
        print(f"User: {self.name}, Email: {self.email}")

class Instructor(User):
    def __init__(self, name, email, experties):
        super().__init__(name, email)
        self.experties = experties
        
    def upload_content(self, content):
        print(f"Instructor: {self.name}, uploaded content: {content}")
        
    def display_info(self):
        print(f"Instructor: {self.name}, Email: {self.email}, Experties: {self.experties}")
        
class CourseCreator(Instructor):
    def __init__(self, name, email, experties, course):
        super().__init__(name, email, experties)
        self.course = course
        
    def create_course(self):
        print(f"{self.name}, created course: {self.course}")
        
    def display_info(self):
        print(f"Course Creator: {self.name}, Email: {self.email}, Experties: {self.experties}, Course: {self.course}")
        
creator =CourseCreator("Sanoj", "sanojyadav2700@gmail.com", "Data Science", "Data Science with Python")
creator.display_info()
creator.upload_content("oops module")
creator.create_course()
