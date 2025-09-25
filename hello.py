def say_hello():
    print("Hello, World!")

def broadcast_hello_to_entire_class():
    for student in range(1, 31):  # Assuming a class of 30 students
        print(f"Hello, Student {student}!")




if __name__ == "__main__":
    say_hello()
    broadcast_hello_to_entire_class()

