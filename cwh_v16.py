# Quiz1-> creat a list and print all numbers lesser than 6 using for loop
l1 = [1,4,6,2,"sk",9,100,"delhi", 5,10,"ghy",3,"hr"]
for item in l1:
    if type(item) == int and item < 6 :
        print(item)