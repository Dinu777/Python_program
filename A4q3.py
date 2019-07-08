# Q3. Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”, then look for the third word and keep a running count of each
# of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Sample Execution:
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

fname = input("Enter file name : ")
fhandle = open(fname)
frd = fhandle.read()
a = frd.splitlines()
b = list()
for i in a:
    i = i.lstrip()
    if 'From' not in i:
        continue
    b.append(i)

c = list()

for i in range(len(b)-1):
    b[i] = b[i].split()
    temp = b[i]
    if len(temp) > 2:
        c.append(temp[2])

day = list()

for i in c:
    if i not in day:
        day.append(i)

day_count = {day[i]: c.count(day[i]) for i in range(len(day))}

print(day_count)
