#function that reverse
def reverse_string(string):
    list_correct = []
    list_reverse = []
    #append the characters in a list for easy reverse
    for letters in string:
        list_correct.append(letters)
    #counter definied to iterate with the list
    count = len(list_correct)-1
    #append the list backward
    for i in range(len(list_correct)):
        list_reverse.append(list_correct[count])
        count -= 1
    #convert list to string
    string_reverse = ''.join(list_reverse)
    #return string
    return string_reverse

#main functon
if __name__ == "__main__":
    word = input('Enter with the string to be reversed:\n')
    print(reverse_string(word))

#this script is capable of reverse a text with all kinds of caracteres
#it was used least built-in functions as possible