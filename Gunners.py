import turtle

pen = turtle.Turtle()
pen.speed(1)

# def square():
#     for i in range (4):
#         pen.forward(100)
#         pen.left(90)
         

# square()
 
def star():
       for _ in range(50):
              pen.forward(200)
              pen.right(170)

star()

def circle(): 
        pen.circle(120)

circle()

# t = turtle.Turtle()
# for  i in range(36):
#         t.foward(100)
#         t.right(170)   small change creates a cool star pattern
# turtle.done


 

def check_attendance(student_name, attendance_record):

  
    if student_name in attendance_record:
            is_present = attendance_record[student_name]
        if is_present:
            return f"{student_name} is Present."
        else:
            return f"{student_name} is Absent."
   else:
        
        return f"{student_name} was not found in the attendance record."

class_attendance = {
    "Alice": True,
    "Bob": False,
    "Charlie": True,
    "David": False
}


student1 = "Alice"
print(check_attendance(student1, class_attendance))

student2 = "Bob"
print(check_attendance(student2, class_attendance))
student3 = "Eve"
print(check_attendance(student3, class_atdance))


class_attendance["Eve"] = True 
print(check_attendance("Eve", class_attendance))
             