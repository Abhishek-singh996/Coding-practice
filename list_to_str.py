# def listToStr(list):
#     str1 = ""
#     for i in list:
#         str1 = i + str1
#     return str1
# list = ["my","name","is","abhishek"]
# q = listToStr(list)
# print(f"string is : {q}")
# List is converting into string  
def convertList(list1):  
    str = ''  # initializing the empty string  
  
    for i in list1: #Iterating and adding the list element to the str variable  
        str += i 
  
    return str  
  
list1 = ["Hello"," My", " Name is ","Devansh"] #passing string   
print(convertList(list1)) # Printin the converted string value  