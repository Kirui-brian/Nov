# Declaring global variables.
calculation_to_units = 24
name_of_units = "hours"


# Declaring a function and local variables.
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"


def validate_and_execute():
    try:
        # Casting input() into an integer and storing it in a variable called user_input_number.
        user_input_number = int(num_of_days_element)
        # We want to do conversion for positive number of days only.
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("There is no 0 days! Please enter a valid positive integer.")
        else:
            print("You entered a negative number. There is no negative number of days!")
    except ValueError:
        print("Your input is not a valid number. You will crash this program!")


# Assign an empty string to user_input.
user_input = " "
# Evaluating using while loop.
while user_input != "exit":
    user_input = input("Hi! Enter a number of days in a comma separated list and I will convert it to hours:\n")
    for num_of_days_element in set(user_input.split(", ")):   # Split will return a list of all input values.
        validate_and_execute()
