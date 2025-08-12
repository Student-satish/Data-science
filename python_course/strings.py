# single quoted strings

a = 'satish';

# double quoted strings

b = 'satish';

# triple quoted strings


c = '''This is 
a multi-line string
'''

print(a);
print(b);
print(c);

# indexing

text = "harikrishna";

print(text[0]);
print(text[1]);
print(text[5]);

# how to print characters from last
 
print(text[-1]);
print(text[-2]);

print(text[-11]);

# len(text) - 1 = -1
# len(text) - 2 = -2

print(len(text));


# string slicing

name = "satish kuruba";

print(name[0:6])
print(name[:6]);
print(name[6:]);
print(name[::3]);
#start:end:step
print(name[-4:12:1]);


# string methods

greet = " hello world ";
print(greet.upper());
print(greet.lower());
print(greet.strip())