def Armstrong_number(x):
    sum=0
    temp=x
    while temp>0:
        digit=temp % 10
        sum+=digit ** 3
        temp//= 10
    if x==sum:
        return True
    else:
        return False
def divisible_by_5(x):
    if x % 5 == 0:
        return True
    else:
        return False
def largest_number(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z
def check_Even_or_Odd(x):
    if x % 2 == 0:
        return True
    else:
        return False
if __name__ == "__main__":

    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))
    z = int(input("Enter the value of z: "))

    Armstrong = Armstrong_number(x)
    print(Armstrong)

    div = divisible_by_5(x)
    print(div)

    largest = largest_number(x, y, z)
    print(largest)

    EvenorOdd = check_Even_or_Odd(x)
    print(EvenorOdd)