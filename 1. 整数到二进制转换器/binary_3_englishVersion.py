# to run: python3 1.binaryEng.py
# To convert integer to binary, start with the integer in question and divide it by 2 keeping notice of the quotient and the remainder. Continue dividing the quotient by 2 until you get a quotient of zero. Then just write out the remainders in the reverse order.

def reverseString(string):    
    return string[::-1]  

userInput = input('Please input an integer:') 
inputtedInteger = int(userInput)         

binaryString = "" 

while (int(inputtedInteger) >= 1):
    remainder = inputtedInteger % 2             
    if remainder == 1:
      binaryString += "1"           
    else: 
      binaryString += "0"    
    inputtedInteger = int(inputtedInteger / 2)  

reversedBinaryString = reverseString(binaryString)
print(reversedBinaryString) 


