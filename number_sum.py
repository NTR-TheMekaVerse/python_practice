'''
Steps:

1: Prompting for Input: Write a Python program that prompts the user to enter a series of numbers.

2: Looping with a while Loop: Use a while loop to continuously read numbers until the user enters a negative number to stop the loop.

3: Calculating Running Total and Outputting Sum: Within the loop, calculate the running total of the entered numbers. After the loop ends, output the total sum.

4: Putting all together from Step 1-3 into 1 program: 

    Write a Python program that prompts the user to enter a series of numbers.
    Use a while loop to continuously read numbers until the user enters a negative number to stop the loop.
    Within the loop, calculate the running total of the entered numbers.
    After the loop ends, output the total sum.

'''

# Number container
numbers = []

# While loop to capture and calculate input
while True:
    num = int(input("Enter any number (negative number to stop): "))
    if num < 0:
        break
    numbers.append(num)
    total_sum = sum(numbers)
print(f"The sum of the entered numbers is: {total_sum}")