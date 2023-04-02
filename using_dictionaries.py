# Declaring a function and local variables.
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "Unsupported unit."


def validate_and_execute():
    try:
        # Casting input() into an integer and storing it in a variable called user_input_number.
        user_input_number = int(days_and_unit_dictionary["days"])
        # We want to do conversion for positive number of days only.
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
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
    user_input = input("Hi! Enter a number of days and conversion unit:\n")
    days_and_unit = user_input.split(":")   # Split will return a list of all input values.
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute()
