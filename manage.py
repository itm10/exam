from examm import *

# def user_details():
#    check=True
#    while check:
#     firstname=input("First name: ")
#     lastname=input("Last name: ")
#     birth_day=input("YYYY-MM-DD: ")
#     phones=input("Phone: ")
#     usernames=input("Username: ")
#     password1=input("password: ")
#     password2=input("confirm password: ") 

#     if password1==password2:
#        check=False
#        data=dict(
#           firstname=firstname,
#           lastname=lastname,
#           birth_day=birth_day,
#           phones=phones,
#           usernames=usernames,
#           password2=password2
#        )
#     else:
#          check=True

#     return data
   
# def cource_details():
#    name=input("Name of cource: ")
#    limit=int(input("Cource limit: "))
#    data1=dict(
#       name=name,
#       limit=limit
#    )
#    return data1
show()
malumot()
print("1.Register\n2. Cource add\n3.Login\n4.Show active cources")
verify=int(input("Enter: "))
if verify==1:
    check=True
    while check:
        firstname=input("First name: ")
        lastname=input("Last name: ")
        birth_day=input("YYYY-MM-DD: ")
        phones=input("Phone: ")
        usernames=input("Username: ")
        password1=input("password: ")
        password2=input("confirm password: ") 
    
        if password1==password2:
            if is_exist('username',usernames):
                print("This user is already exists")
                check=True
            else:
                check=False
                data=dict(
                   firstname=firstname,
                   lastname=lastname,
                   birth_day=birth_day,
                   phones=phones,
                   usernames=usernames,
                   password1=password1
                )
                insert_users(data)
                
elif verify==2:
    check=True
    while check:
        name=input("Name: ")
        numbers=int(input("Number of cources: "))
        if is_cource_exist('name',name):
            print("This cource is already exists")
        else:
            check=False
            data1=dict(
                name=name,
                numbers=numbers
            )
            cource_insert(data1)
            


elif verify==3:
    username=input("Username: ")
    password=input("password: ")
    ss1=get_id(username,password)
    
    if ss1:
        show()
        malumot()
        
    

           
              
      
        
    