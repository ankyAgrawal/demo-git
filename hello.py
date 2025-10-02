def say_hello():
    print("Hello, World!")

def broadcast_hello_to_entire_class():
    for student in range(1, 31):  # Assuming a class of 30 students
        print(f"Hello, Student {student}!")

ßß
def return_a_list_of_random_numbers():
    import random
    return [random.randint(1, 100) for _ in range(10)]  # List of 10 random numbers between 1 and 100


if __name__ == "__main__":
    say_hello()
    broadcast_hello_to_entire_class()
    random_numbers = return_a_list_of_random_numbers()
    print("Random Numbers:", random_numbers)

