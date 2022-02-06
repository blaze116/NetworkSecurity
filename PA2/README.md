# NETWORK SECURITY

### *Practical Assignment 2 (PA2)*

Perform experiments to explore the Avalanche Effect progression across the DES rounds. Use (i) 5 different plaintexts (ii) 5 different Hamming distances (HD) (iii) 5 different secret keys. Report plots of HD against round number.

------

### **Avalanche Effect:**

​	A desirable property of any encryption algorithm is that a small change in either the plaintext or the key should produce a significant change in the ciphertext. In particular, a change in one bit of the plaintext or one bit of the key should produce a change in many bits of the ciphertext. This is referred to as the avalanche effect. If the change were small, this might provide a way to reduce the size of the plaintext or keyspace to be searched

**1) TEST 1:  Avalanche Effect in DES ( Change in Plaintext )**

Here I’ve considered 5 different Plain Texts with Hamming distances(HD) 1,2,3,4 and 5 respectively and one constant key

**The original plaintext** : “10111100” (64 bit string)

**The original Key** : "00011100" (64 bit string)

text_list = ["±0111100", "ñ0111100", "60111100", "Á0111100", "10É11100"]

##### Point plot of Hamming distance vs No. of Rounds

<img src="images\test 1.png alt="test" style="zoom:67%;" />

------

Here I’ve considered 5 different Keys with Hamming distances(HD) as 1,2,3,4 and 5 respectively and one constant Plain Text

**The original plaintext** : “10100100” (64 bit string)

**The original Key** : "00011100" (64 bit string)

key_list = ["p0011100" ,"°0011100" ,"°0451±00" ,"d0451±00" ,"µút11100"]

##### Point plot of Hamming distance vs No. of Rounds

<img src="images\test 2.png" alt="test" style="zoom:67%;" />

------

