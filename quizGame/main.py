# Build a simple quiz game that asks random questions from a predefined list. 
# Handle user input errors and calculate the final score.


#THE PLAN
#--------

#try:  @
#   open --> question file. @

#   preprocessing
#   loop --> 1 to n:
#         print ---> question
#         try:
#           input <------ user input
#           if input ans is correct:
#                   score ----> +1
#           else:
#                 no score (score ----> +0)
#         except:
#            if type error ---> print ---> input type error
#   return score -----> print---> score 

#except: @
#   print --> error @



import random as r

try:
    try:
        myFile = open("C:\\Users\\adity\\OneDrive\\Documents\\programming\\python\\myProjects\\quizGame\\assets\\qustn.txt", "r")
    except:
        print("file not found!")    
    openFile = myFile.read()
    qtnLst = openFile.split("#")
    score = 0 
    while True:
        count = r.randint(0,(len(qtnLst)-1))
        slctQtn = qtnLst[count].split("*")
        print(slctQtn[0])
        try:
            userIn = input("\nselect option: A, B, C, D: ")
            val = userIn.upper()
            if val in ["A","B","C","D"]:
                if val in slctQtn[1]:
                    print("\ncorrect")
                    score += 1
                else:
                    print("\nwrong")
                qtnLst.pop(count)    
            else:
                print("\ninvalid entry!")
        except:
            print("\ninvalid entry!") 
        slctQtn.clear()    
        if len(qtnLst) < 0:
            break
                                   
except:
    print("your score is: ",score)    
