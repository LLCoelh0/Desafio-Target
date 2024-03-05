#function to chek the number
def is_in_fibo(number):
    #varaibales used in the calculations
    fibo_ant = 0
    fibo = 1
    temp = 0
    list_fibo = [0, 1]
    #stop condition
    while fibo < number:
        temp = fibo
        fibo += fibo_ant
        fibo_ant = temp
        #storaged sequence
        list_fibo.append(fibo)
    #check if is in or not
    if number in list_fibo:
        is_in = True
    else:
        is_in = False
    #returning the results
    return(is_in)
#main function
if __name__ == "__main__":
    number = int(input('Enter with the number would you like to chek if is in Fibonacci:\n'))
    print(is_in_fibo(number))