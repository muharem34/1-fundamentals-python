inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow.values():
        total_inches = total_inches + inches

    print("Total snow inches: ", total_inches)


print_total_snowfall(inches_snow)

new_value = int(input("How many inches fell on Thursday?"))
inches_snow["Thursday"] = new_value
# call the print_total_snowfall() again
print_total_snowfall(inches_snow)
