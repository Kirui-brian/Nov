# Declaring global variables.
calculation_to_units = 24
name_of_units = "hours"


# Declaring a function and local variables.
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"


def validate_and_execute():
    # Nested if statements validating user input using conditional to ensure user input is non-negative or zero.
    if user_input.isdigit():
        # Casting input() into an integer and storing it in a variable called user_input_number.
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("There is no 0 days! Please enter a valid positive integer.")
    else:
        print("Your input is not a valid number. You will crash this program!")


# Prompting user to enter the number of days.
user_input = input("Hi! Enter a number of days and I will convert it to hours:\n")
validate_and_execute()
