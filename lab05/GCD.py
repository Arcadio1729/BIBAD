def calculate_GCD(nr1, nr2):
    temp_max=max(nr1,nr2)
    temp_min=min(nr1,nr2)
    current_difference=temp_max-temp_min
    while current_difference!=0:
        temp_max=max(current_difference,max(current_difference,temp_min))
        temp_min=min(current_difference,min(current_difference,temp_min))
        current_difference=temp_max-temp_min
    return temp_max

if __name__ == "__main__":
    print("Enter two integer numbers:")
    print("Number 1: ")
    nr1=int(input())
    print("Number 2: ")
    nr2=int(input())
    GCD=calculate_GCD(nr1,nr2)
    try_again=True
    print("Guess GCD: ")
    nr=input()

    if int(nr)==GCD:
        print("Congratulations you won!!!")
        try_again=False
    while try_again:
        print("Sorry, it's wrong. Try again: ")
        nr=input()
        if int(nr)==GCD:
            print("Congratulations you won!!!")
            try_again=False
