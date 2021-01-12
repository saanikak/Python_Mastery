#reading and writing files... different modes
# 'w' ==> write mode, 'a' ==> append mode, 'r' ==> read mode

f = open('/Users/saanikak/Documents/Internships/PythonPractice/funny.txt', 'w')
f.write('I love Python\n')
f.close()

f = open('/Users/saanikak/Documents/Internships/PythonPractice/funny.txt', 'a')
f.write('I love JavaScript\n')
f.write('I love C++ to a certain extent\n')
f.close()

f2 = open('/Users/saanikak/Documents/Internships/PythonPractice/skills.txt', 'r')
print(f2.read())
f2.close()

f2 = open('/Users/saanikak/Documents/Internships/PythonPractice/skills.txt', 'r')
for line in f2:
    tokens = line.split(' ')
    print(str(len(tokens)) + '  ' + line)
f2.close()