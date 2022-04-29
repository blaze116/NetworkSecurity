# Implementation of Linear Congruential Generator PRNG

"""
LCG - generates as many random numbers, using a Linear Congruential Generator
                 X_(i+1) = (aX_i + c) mod m
"""
class LCG():
    def __init__(self):
        # Initialize variables
        self.x_value = 123456789.0    # seed, or X_0 = 123456789
        self.a = 101427               # Multiplier term
        self.c = 321                  # Increment term
        self.m = (2 ** 16)            # Modulus parameter


    def random_array(self, NUMBER_OF_SAMPLES):
        # Get the random values using the formula
        random_numbers = []

        for i in range(NUMBER_OF_SAMPLES): 
            # Store value of each iteration 
            self.x_value = (self.a * self.x_value + self.c) % self.m

            # Get the value in U[0, 1) by divide x_value by m
            rand_val = self.x_value / self.m

            # Append the value to list
            random_numbers.append(rand_val)
        return random_numbers
