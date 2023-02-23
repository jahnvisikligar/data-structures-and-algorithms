"data structures-arrays"
#assignment 1
expenses={'January':2200, 'February':2350,'March':2000,'April':2130,'May':2190}
#1. In Feb, how many dollars you spent extra compare to January?
#print((expenses['February']-expenses['January']))
print('Excess expenditure from previous month: $',(expenses['February']-expenses['January']))
#2. Find out your total expense in first quarter (first three months) of the year.
print('Expenditure in Q1: $',(expenses['January']+expenses['February']+expenses['March']))
#3. Find out if you spent exactly 2000 dollars in any month
NUM_VAL=2000
if NUM_VAL in expenses.values():
    print('Expense of $2000 in month')
else:
    print('No expense of $2000 in any month')
#4.June month just finished and your expense is 1980 dollar
#Add this item to our monthly expense list
expenses.update({'June':1980})
print(expenses)
#5.You returned an item that you bought in a month of April and got a refund of 200$
#Make a correction to your monthly expense list based on this
NEW_AMT_APR=expenses['April']-200
expenses['April']=NEW_AMT_APR
print(expenses)
#assignment 2
heros=['spider man','thor','hulk','iron man','captain america']
#1. Length of the list
print('length of an array:',len(heros))
#2. Add 'black panther' at the end of this list
heros.append('black panther')
print('New list of avengers:', heros)
#3.You realize that you need to add 'black panther' after 'hulk'.
# #remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
print('The list is set to original one')
heros.insert(3, 'black panther')
print('New list of heros:', heros)
#4.Now you don't like thor and hulk because they get angry easily :)
#To remove thor and hulk from list and replace them with doctor strange (because he is cool)
# Do that with one line of code.
heros[1:3]=['doctor strange']
print(heros)
#5.Sort the heros list in alphabetical order
#(Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print('sorted list in ascending order:',heros)
#assignment 3
#Create a list of all odd numbers between 1 and a max number
#Max number is something you need to take from a user using input() function
n=int(input('Enter a number'))
odd_num=[]
for i in range(1,n+1):
    if i%2!=0:
        odd_num.append(i)
        print(i)
print('\n')