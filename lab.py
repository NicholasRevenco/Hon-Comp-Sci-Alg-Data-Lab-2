"""
Name: Homework Night
Purpose: This is a text-based interactive game known as "Homework Night" where you, 
    the student, is situation in a dark room and need to manage your time before 
    starting the day. As part of the night, you are required to eat sleep, and complete 
    your homework before going to school the next day. Set in a quiet night where 
    the serenity outside contrasts with the mental activity within the room, you have 
    to navigate through the options, grappling with the realistic trade-offs between nourishment,
    rest, and academic diligence, all enveloped in a ticking clock racing towards a new day.

Date: September 26, 2023
"""

# Only used for math questions
import random

# Global variables
time = 1 
homework_count = 0
has_eaten = False
has_slept = False

# Satisfies 1
def display_choices(wake_up_message: str, repeat_wake_up: int = 1) -> None:
    """
    Choices to pick from are displayed

    Parameters:
    wake_up_message (str): Message to user
    repeat_wake_up (int, optional): Repeats the message to user

    Returns:
    None
    """

    print("\n")

    # Message to user repeats
    for i in range(repeat_wake_up):
        print(wake_up_message)
    
    # Game time display
    print(f"It's currently {time % 12}:00 AM! ")

    # Choices displayed
    print("1. Go to bed")
    print("2. Go eat")
    print("3. Do math homework")


# Satisfies 4, 6
def option_func(message: str = "What choice do you want to make?") -> int:
    """
    Asking the user for the option to make

    Parameters:
    message (str, optional): Message asking user the option to make

    Returns:
    Int
    """

    while True:
        try:
            choice = int(input(message))
            # Has to pick an integer from 1 to 3
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a number.")

# Satisfies 11
def user_option_display(value: int) -> None:
    """
    Prints the user's option

    Parameters:
    value (int): User's option

    Returns:
    None
    """

    # Branches off based on input
    if isinstance(value, int):
        return
    elif isinstance(value, str):
        # Displays the user their option
        print("You picked option ", str(value), ".")
        return
    else:
        raise ValueError("Unsupported data type")

# Satisfies 5
def math_complete_message(user_option: str, add_message: str,) -> None:
    """
    Message to user when all of math is complete

    Parameters:
    user_option (int): User's option of completion (3)
    add_message (str): Message to user about completion

    Returns:
    None
    """

    print("You picked option ", str(user_option), " twice!")
    print(add_message)

# Satisfies 7, 12
def addition_math_question(*args: int) -> list:
    """
    Random addition math question to user

    Parameters:
    args (tuple): All of integers for the user to add

    Returns:
    List
    """

    numbers = args
    total = sum(numbers)

    # Interesting use of join(map(str, numbers)) that I did not know how to use 
    # before. It first converst each integer in `numbers` to a string, and 
    # then it constructs a string by concatenating each integer with a " + "
    # between each pair of integers. Used Stack Overflow to find and understand.
    print("What is:", " + ".join(map(str, numbers)), "?")
    
    # To check if the user inputed an integer
    while True:
        try:
            user_input = int(input("Answer: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Returns correct answer and user's input
    return total, user_input

# Satisfies 2, 12
def multi_math_question(num_1: int, num_2: int) -> list:
    """
    Random multiplication math question to user

    Parameters:
    num_1 (int): First integer
    num_2 (int): Second integer

    Returns:
    List
    """

    print("What is: ", str(num_1), " times ", str(num_2), "?")
    
    # To check if the user inputed an integer
    while True:
        try:
            user_input = int(input("Answer: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Returns correct answer and user's input
    return num_1 * num_2, user_input

# Satisfies 3
def check_morning(given_time: int) -> bool:
    """
    Checks if the time is 8:00 AM

    Parameters:
    given_time (int): Time of player

    Returns:
    Boolean
    """

    return given_time >= 8

# Satisfies 8
def print_summary(**kwargs) -> None:
    """
    Displays the tasks the user has completed

    Parameters:
    **kwargs (dictionary): Task name and status for task

    Returns:
    None
    """

    # Creates a list of strings, each representing a key-value pair from the
    # 'kwargs' dictionary. It then iterates through each pair, and constructs
    # "key: value" using an f-string. Used Stack Overflow to find and understand.
    summary_strings = [f"{key}: {value}" for key, value in kwargs.items()]

    # Similar concept to statement used in addition_math_question() function
    print(", ".join(summary_strings))

# Satisfies 10
def math_homework_type(*, user_request: str, invalid_message: str) -> str:
    """
    Checks the homework type of request

    Parameters:
    user_request (str): Message form user asking for input
    invalid_message (str): Wrong input for user message

    Returns:
    String
    """

    # Keeps asking for correct form of input until correct form
    while True:
        math_type = input(user_request)
        if math_type in ['a', 'm']:
            return math_type
        else:
            print(invalid_message)

# Satisfies 9
def initial_greeting(name: str, place: str, /, add_message: str) -> None:
    """
    First message to user explaining where they are

    Parameters:
    name (str): Name of user
    place (str): Place of location next day
    add_message (str): An additional message for the user

    Returns:
    None
    """

    print(name, ", you are in your room at 12:00 AM, and have so much homework to do. You also did not eat dinner, and would like to eat dinner at some point before ", place,". Get some rest if you are able to before", place, ".", add_message)

def main():
    global time, homework_count, has_eaten, has_slept

    print("\n")

    # Satisfies 9, 13
    try:
        initial_greeting(name="Fellow student", place="school", add_message="Good luck!")
    except TypeError as e:
        initial_greeting("Fellow Student", "school", "Good luck!")
        print(f"Error: {e}", " This satisfies requirement 13.")
        
    # Loop keeps running while the user has not reached morning
    # Satisfies 3
    while not check_morning(time):
        # Satisfies 1
        display_choices("Wakey wakey!", repeat_wake_up=1)

        # Identifies the user's option of what to do
        if time == 5:
            # Satisfies 4, 6
            user_option = option_func(message="What option do you pick?")
        else: 
            # Satisfies 6
            user_option = option_func()

        # Print if the user has completed all of their homework
        if homework_count == 2:
            # Satisfies 5
            math_complete_message(3, add_message="You completed all of your homewokr!",)
        
        # Satisfies 11
        user_option_display(user_option)

        # Changes status of what the user has completed
        if user_option == 1:
            time += 2
            has_slept = True
        elif user_option == 2:
            time += 1
            has_eaten = True
        elif user_option == 3:
            time += 1
            homework_count += 1

            # Asks the user if they want to do multiplication or addition
            # Satisfies 10, 14
            try: 
                math_type = math_homework_type("Do you want to do addition or multiplication? (a/m): ", "Invalid input. Please enter 'a' for addition or 'm' for multiplication.")
            except Exception as e:
                math_type = math_homework_type(user_request="Do you want to do addition or multiplication? (a/m): ", invalid_message="Invalid input. Please enter 'a' for addition or 'm' for multiplication.")
                print(f"Error: {e}", " This satisfies requirement 14.")
            
            # Makes an addition math question if requested
            if math_type == 'a':
                """ A generator expression is used to create a sequence of random 
                integers, each between 1 and 10, with the total count of these 
                integers being a random number between 2 and 5. The asterisk * 
                operator is used to unpack this sequence of random integers into 
                individual arguments. """
                # Satisfies 7, 12
                correct_answer, user_answer = addition_math_question(*(random.randint(1, 10) for i in range(random.randint(2, 5))))

            # Makes a multiplication math question if requested
            else:
                # Satisfies 2, 12
                correct_answer, user_answer = multi_math_question(random.randint(1, 10), random.randint(1, 10))
            
            # If the user answers the math question incorrectly, they use an hour of sleep
            if correct_answer != user_answer:
                print("Incorrect answer, you lose an hour of sleep.")
                time += 1
            else:
                print("Correct! Good job!")
        # In case the user picks an option that is not available
        else:
            print("You can't do that right now.")

        # Satisfies 8
        print_summary(homework_completed=homework_count, has_eaten=has_eaten, has_slept=has_slept)

    # Winning message and losing message
    if homework_count >= 2 and has_eaten and has_slept:
        print("Congratulations! You managed to complete all tasks by 8:00 AM! You are going to have an amazing day!")
    else:
        print("Game over. You didn't manage to complete all tasks 8:00 AM! You are going to have a terrible day!")

main()