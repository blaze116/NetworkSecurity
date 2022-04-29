
from main import Mersenne
SEED = 0
Rand = Mersenne(SEED)

def chi_square_uniformity_test(data_set, confidence_level, num_samples):
    
    chi_sq_value = 0.0                          # This is our test statistic, this will be an accumulated value, as we loop through the data set
    degrees_of_freedom = num_samples - 1

   
    expected_val = num_samples / 10.0           # We're doing 10 equal section, so need to divide our number samples by 10,
                                                # Assuming uniform distribution, to get an expected value. All values should be same
                                                # If our distro is actually uniform.

   
    for observed_val in data_set:
        chi_sq_value += (pow((expected_val - data_set[observed_val]), 2) / expected_val)  # Loop through a dictionary and get every count
                                                                                            # The observed value is going to be our count 
                                                                                            # at each key, and then we can do chi-square

    return chi_sq_value

def main(NUMBER_OF_SAMPLES):
    # We divide all observations in 10 parts
    section = {"1":  0, "2":  0, "3":  0, "4":  0, "5":  0, "6":  0, "7":  0, "8":  0, "9":  0, "10": 0}
    for num in range(NUMBER_OF_SAMPLES):
        num = Rand.random()
        if num < 0.1:
            section["1"] += 1
        elif num < 0.2:
            section["2"] += 1
        elif num < 0.3:
            section["3"] += 1
        elif num < 0.4:
            section["4"] += 1
        elif num < 0.5:
            section["5"] += 1
        elif num < 0.6:
            section["6"] += 1
        elif num < 0.7:
            section["7"] += 1
        elif num < 0.8:
            section["8"] += 1
        elif num < 0.9:
            section["9"] += 1
        elif num < 1.0:
            section["10"] += 1

    print("---------CHI-SQ_TEST-----------")
    chi_sq_result = chi_square_uniformity_test(section, 0, NUMBER_OF_SAMPLES)
    critical_value_95_confidence = 9767.5368

    print("Chi Sq: " + str(chi_sq_result))
    print("Critical Value: " + str(critical_value_95_confidence))
    if chi_sq_result <= critical_value_95_confidence:
        print("Fail To Reject null hypothesis")
    else: 
        print("Reject null hypothesis")

if __name__ == '__main__':
    NUMBER_OF_SAMPLES = 10**5
    main(NUMBER_OF_SAMPLES)