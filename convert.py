CONVERSION_FACTOR = 1.8

def convert_temp(unit_in, unit_out, temp):
    """Convert fahrenheit <-> celsius and return results.

    - unit_in: either "f" or "c"
    - unit-out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # YOUR CODE HERE

    converted_temp = temp

    if unit_in == "f" and unit_out == "c":
        converted_temp = (temp - 32) * (1 / CONVERSION_FACTOR)
    elif unit_in == "c" and unit_out == "f":
        converted_temp = (temp * CONVERSION_FACTOR) + 32
    elif not unit_in == "f" and not unit_in == "c":
        return (f"Invalid input unit {unit_in}")
    elif not unit_out == "f" and not unit_out == "c":
        return (f"Invalid output unit {unit_out}")

    return converted_temp

print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")
