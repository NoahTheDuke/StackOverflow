"""
I have a file created by python3 using:

   of.write("{:<6f} {:<10f} {:<18f} {:<10f}\n".format((betah), test, (torque*13605.698066), (mom)))

The output file looks like:

$cat pout
15.0     47.13    0.0594315908872    0.933333333334
25.0     29.07    0.143582198404     0.96
20.0     35.95    0.220373446813     0.95
5.0     124.12    0.230837577743     0.800090803982
4.0     146.71    0.239706979471     0.750671150402
0.5     263.24    0.239785533064     0.163953413739
1.0     250.20    0.240498520899     0.313035285499

Now, I want to sort the list.

The expected output of sorting will be:

25.0     29.07    0.143582198404     0.96
20.0     35.95    0.220373446813     0.95
15.0     47.13    0.0594315908872    0.933333333334
5.0     124.12    0.230837577743     0.800090803982
4.0     146.71    0.239706979471     0.750671150402
1.0     250.20    0.240498520899     0.313035285499
0.5     263.24    0.239785533064     0.163953413739

I tried this and tuples example in this but they are yielding the output as

['0.500000 263.240000 0.239786           0.163953  \n',  '15.000000 47.130000  0.059432           0.933333  \n', '1.000000 250.200000 0.240499           0.313035  \n',  '25.000000 29.070000  0.143582           0.960000  \n', '20.000000 35.950000  0.220373           0.950000  \n',  '4.000000 146.710000 0.239707           0.750671  \n',  '5.000000 124.120000 0.230838           0.800091  \n']

Please, don't try to match the numbers of input and output, because both of them are truncated for brevity.

As an example for my own try for the sorting with help from 1 is like:

f = open("tmp", "r")
lines = [line for line in f if line.strip()]
print(lines)
f.close()

Kindly help me sorting the file properly.
"""

pout = [
"15.0     47.13    0.0594315908872    0.933333333334",
"25.0     29.07    0.143582198404     0.96          ",
"20.0     35.95    0.220373446813     0.95          ",
"5.0     124.12    0.230837577743     0.800090803982",
"4.0     146.71    0.239706979471     0.750671150402",
"0.5     263.24    0.239785533064     0.163953413739",
"1.0     250.20    0.240498520899     0.313035285499"]

with open('test.txt', 'w') as thefile:
    for item in pout:
        thefile.write(str("{}\n".format(item)))

lines = [line.strip() for line in open('test.txt')]
acc = []
for strings in lines:
    words = strings.split()
    words = [float(word) for word in words]
    acc.append(words)
lines = sorted(acc, reverse=True)

with open('test.txt', 'w') as thefile:
    for item in lines:
        #temp = [str(word) for word in item]
        thefile.write("{:<6f} {:<10f} {:<18f} {:<10f}\n".format(item))
