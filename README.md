# Highest-ASCII-value


Write a program to analyze the characters in a given string Str and find N, the number of occurrences of the character having the highest ASC value Then print the character having the lowest ASCII value in Str, N times. The string Str can contain either special characters or alphanumerics or strip of all. The string can be present in any case: lowercase, uppercase or both.
<br>
Read the input from STDIN and print the output to STDOUT. Do not write arbitrary strings anywhere in the program, as these contribute to the standard output and testcases will fail.
<br>
Constraints:<br>

The length of Str> 0  <br>

Input: <br>

The input will be the string to be analyzed, Str
<br>
Output:
<br>
The output contains the lowest ASCII value character printed N times.
<br>
Sample Input2: 9856zeltab'ugzG*
<br>
Sample Output2:!! <br>
Explanation2:
<br>
From the sample input2, given string Str is "9856ze!tab'ugzG** ASCII value of 9 is 57.<br>
8=56<br>
5=53<br>
6=54<br>
z=122<br>
e=101<br>
!=33<br>
t=166<br>
a=97<br>
b=98<br>
'= 39<br>
u=117<br>
g=103<br>
z= 122<br>
G=71<br>
* = 42<br>
<br>
Among all, the highest ASCII value is of "z" at 122 and "z" occurs twice (N=2) in Str. The lowest ASCII value character in Str is 33, which is "!". So "!!" printed as output.<br>
Sample Input2:<br>

ABOVEtheheight<br>

Sample Output2:<br>

AA <br>

Explanation2:
From the sample input, given string Str is "ABOVEtheheight".<br>
ASCII value of A:65<br>
ASCII value of B:66<br>
ASCII value of 0:79<br>
ASCII value of V:86<br>
ASCII value of E:69<br>
ASCII value of t:116<br>
ASCII value of h:104<br>
ASCII value of e:101<br>
ASCII value of h:104<br>

