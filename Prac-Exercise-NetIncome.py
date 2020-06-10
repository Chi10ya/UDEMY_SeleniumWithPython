"""
Calculate the net income after fedaral and state tax
:param gross: Gross Income
:param state: State Name
:return: Net Income
"""


def calculateNetIncome(gross, state):

    state_tax= {'CA': 10, 'NY' : 9, 'TX' : 0, 'NJ' : 6}

    # Calculate net income after fedaral tax
    net= gross-(gross * .10)

    # Calculate net income after state tax
    if state in state_tax:
        net= net-(gross * state_tax[state] / 100)
        print("Your net income after all the taxes is : "+str(net))
        return net
    else:
        print("State not in the list")
        return None


calculateNetIncome(200000, 'CA')


print("========== 2: Find out whose name is having more than 5 characters =========")


def namelistsize(namesList):

     print(namesList)
     print("....")
     greater5count= 0
     less5count= 0

     for i in namesList:
          namelen= len(i)
          print(f"Name Length ==> {namelen}")
          if namelen >=5:
               greater5count+=1
               print(f"The name {i} is {len(i)} characters and greater than 5 characters")
          else:
               less5count+=1
               print(f"The name {i} is {len(i)} characters and less than 5 characters")

     print(f"  G5 Count : {greater5count}")
     print(f"  L5 Count : {less5count}")

namesList= ['Chaitanya', 'Ambica', 'Yashvir', 'Dhiyanshi', 'abcd', 'klm', 'Dublin']
namelistsize(namesList)

print("========== 3: Exception Handling Exercise try, except, finally =========")


def dictcar(myDicts):
     try:
          for i in myDicts:
                print("In Try block")
                print(f"Key is : {i} : value is : {myDicts[i]}")
                print(myDicts["COLOR"])
     except:

            print("In Except block")
            print("Didn't execute the retrieval of dictionary values")

     finally:

            print("In Finally block")


myDicts= {'MAKE':'Peugeot', 'MODEL':'3008', 'YEAR': '2020'}
dictcar(myDicts)

