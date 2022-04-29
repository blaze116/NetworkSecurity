## Practical Assignment 5

#### Implementation of El Gamal algorithm 

##### <u>*Solution Approach :*</u>

------

El Gamal encryption is public-key cryptosystem which uses asymmetric key encryption for communicating between two parties and encrypting the message. 

Let’s understand the idea using a simple example : 

Suppose A wants to communicate with B,

<ol>    
  <li> B will generate his public and private keys : </li>
<ul>
  <li> He will choose a very large number q and a cyclic group Fq. </li>
  <li>  From the group, he will choose two elements g and a such that GCD(q , a) = 1.</li>
  <li>  Computes h = g^a.</li>
  <li>  He then publishes F,h = g^a, q and g as his public key and a as private key.</li>
 </ul>
  <li> A encrypts the data using B’s public key : </li>
  <ul>
  <li>  A selects an element k from cyclic group F such that GCD(q,k) = 1.</li>
  <li>  Then, he computes p = g^k  and s = h^k = g^(ak).</li>
  <li>  Multiples s with M.</li>
  <li>  Then sends (p,M*s) = (g^k,M*s).</li>
  </ul>
<li> B decrypts the message : </li>
  <ul>
  <li>  B calculates s’ = p^a = g^(ak) .</li>
  <li>  He divides M*s by s’ to obtain M as s = s’.</li>
  </ul>
 </ol>



##### Example :

```
Original Message : Nezuko looks so cute !

g used :  24392065974739255689202895290594915984914430210544

h = g^a used :  11315145189069183108971223442415720513209865063846

g^k used :  9115583457659973621032020826186829483684309916088

g^ak used :  19381339233658317043918287618215625907519496712452

Decrypted Message : Nezuko looks so cute !
```

