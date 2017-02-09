user_input = raw_input('enter a path to a file (there is no fool protection, so be careful):\n')
f = open(user_input, 'r+')
l = list(f)
str1 = ''.join(l).replace(' ', '.')
str1 = '\n' + str1
f.write(str1)
f.close()