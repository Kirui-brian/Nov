# Declaring global variables.
calculation_to_units = 24
name_of_units = "hours"


# Declaring a function and local variables.
def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")
    print(custom_message)
    print("This is how a function works in Python.")


days_to_units(365, "These are the number of days of a non leap year.")
