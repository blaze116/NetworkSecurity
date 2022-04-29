## *Practical Assignment 4 (PA4)*

#### PRNG - 1 : Linear Congruential Generator 

Linear Congruential Generator is most common and oldest algorithm for generating pseudo-randomized numbers. The generator is defined by the recurrence relation:


​                             Xn+1 = (a*Xn + c) mod m

Where

```
    Xn+1 = (aXn + c) mod m
    where X is the sequence of pseudo-random values
    m, 0 < m  - modulus 
    a, 0 < a < m  - multiplier
    c, 0 ≤ c < m  - increment
    x0, 0 ≤ x0 < m  - the seed or start value
```



##### Approach: 

- Choose the seed value X0, Modulus parameter m, Multiplier term a, and increment term c.

- Initialize the required amount of random numbers to generate

- Define a storage to keep the generated random numbers (here, vector is considered) of size equal to number of generated random numbers.

- Initialize the 0th index of the vector with the seed value.

- For rest of the indexes follow the Linear Congruential Method to generate the random numbers.

     

  ```
   randomNums[i] = ((randomNums[i – 1] * a) + c) % m 
  ```

  

- Finally, return the random numbers.

#### **PRNG - 1 : Mersenne Twister** 

The Mersenne Twister is a strong pseudo-random number generator. In non-rigorous terms, a strong PRNG has a long period (how many values it generates before repeating itself) and a statistically uniform distribution of values (bits 0 and 1 are equally likely to appear regardless of previous values). A version of the Mersenne Twister available in many programming languages, MT19937, has an impressive period of 219937-1. Sequences with too short a period can be observed, recorded, and reused by an attacker. Sequences with long periods force the adversary to select alternate attack methods.