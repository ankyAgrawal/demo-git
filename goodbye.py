def say_good_bue():
    print("Goodbye, World!")

def broadcast_goodbye_to_entire_class():
    for student in range(1, 31):  # Assuming a class of 30 students
        print(f"Goodbye, Student {student}!")


def __main__():
    say_good_bue()
    broadcast_goodbye_to_entire_class()