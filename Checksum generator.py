#0201314152

runningtotal = 0
counter = 10
odd = 0
even = 0
user_account = (input("Enter a number: "))
for i in user_account:
    digit = int(i) #Convert each character to an int
    runningtotal += digit * counter #Multiply digit by the current counter
    print(f"Digit: {digit}, Counter: {counter}, Running Total: {runningtotal}")
    counter -= 1
next_multiple_of_11 = (runningtotal // 11 + 1) * 11 #The next multiple of 11
checksum_digit = next_multiple_of_11 - runningtotal
if checksum_digit == 10:
    checksum_digit = "X"
print(f"10 digit ISBN number: {user_account}{checksum_digit}")
    











