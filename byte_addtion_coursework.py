

from gates import NOR, NAND, NOT, AND, XOR, OR


# function to take input
def take_input():
    return input('Enter two   decimal numbers: (Enter with empty string to exit) :').split()


# validate if there are 2 and only 2 elements entered
def validate_count(nums):
    if len(nums) == 2:
        return True
    else:
        print('Error in input format. Enter again.')
        return False


# validate if the entered numbers are actually integers
def validate_int(nums):
    try:
       
        int(nums[0]) and int(nums[1])
        return True
    except:
       
        print('Invalid Data Type.')
        return False


# validate if the numbers entered are within range of (0 to 255)
def validate_size(nums):
   
    if 0 <= int(nums[0]) <= 255 and 0 <= int(nums[1]) <= 255:
        return True
    else:
      
        print('The integer is out of bounds (0-255)')
        return False


def is_valid(nums):
    # return true if all validation rules are satisfied
    return validate_count(nums) and validate_int(nums) and validate_size(nums)


# function that adds two bits, along with carry
def add_bits(a, b, cin):
    # simulating the bit-adder
    
    m = XOR(a, b)
    x = NAND(m, cin)
    y = OR(m, cin)
    s = AND(x, y)
    n = AND(a, b)
    p = AND(m, cin)
    r = NOR(n, p)
    cout = NOT(r)
    return (s, cout)


# function that returns binary representation of a number
def get_bin_string(num):
    # get binary value of num as string
    s = "{0:b}".format(num)
    # since we need exactly 8 bits in both numbers
    # create new list and apppend 0s in front if there are less than 8 bits
    binstr = ['0']*(8 - len(s))
    # after that append every bits in s to binstr
    for ch in s:
        binstr.append(ch)
    # at this point, binstr will be exactly have 8 bits
    # return a string joining the bits in the list binstr
    return ''.join(binstr)


# function that adds two bytes
def add_bytes(a, b):
    checker =1
    # get binary representation of the numbers in 8 bits
    num1 = get_bin_string(a)
    num2 = get_bin_string(b)
    # initializing carry-in as 0 initially
    cin = 0
    # list that will store the bits after
    res = []
    # for every bits in the binary representation (equivalently, every column in addition)
    for i in range(1, 8+1):
        # take out individual bits from bit-string, as integers, starting from the last (hence, -i)
        bit1 = int(num1[-i])
        bit2 = int(num2[-i])
        # add the bits, get sum and carry-out
        s, cout = add_bits(bit1, bit2, cin)
        # carry-in for next column will be carry-out for this column
        cin = cout
        # insert the sum bit at the very beginning
        res.insert(0, str(s))
  
    # create a bit-string by joining the bits in the list
    res = ''.join(res)
    # return the integer value when the bit-string is parsed as binary-string.
    return int(res, 2)


# if this file is run as main program
if __name__ == "__main__":
    # take the numbers input
    nums = take_input()
    # while there is something entered,
    while nums:
        # check if what user entered is valid
        if is_valid(nums):
            # convert the input numbers from string into integers
            num1 = int(nums[0])
            num2 = int(nums[1])
            # calculate the result of byte addition
            result = (add_bytes(num1, num2))
            result = (bin(result).replace("0b",""))
             #  initializing empty list 
            fill = []
            c = 0
            n = 8-len(result)

            for i in range(0,n):
                 fill.append("0")

            for i in range(n,8):
                fill.append(result[c])
                c +=1
            print("The result is ", fill)

        # checking condition to continue next instance
        
        condition = input("Do u want take next instance?(y/n) :")
        if  condition == "n":
            print("Closed")
            checker ==0

        else:
                nums = take_input()
  

    
