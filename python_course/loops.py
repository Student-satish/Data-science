# print numbers from 1 to 100 using loops 

# loops are used to iterate over a sequence

# they execute a block of code repeatedly for each item in a sequence

fruits = ["apple","banana","cherry"];

for fruit in fruits:
    print(fruit,end=' ');


print('\n');



# print numbers from 1 to 100

for i in range(1, 101):
    print(i,end=' ');

while(i < 100):
    print(i);
    i += 2;





# break 


for i in range(10):
    if i == 5:
        break;
    print(i);


for i in range(10):
    if i == 5:
        continue;
    print(i);