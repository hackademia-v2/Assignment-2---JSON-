import json
user_data=[]
while True:
 print("SIGNUP/SIGNIN")
 CHOOSE=int(input("signup(1) or signin(2)"))


 if CHOOSE==1:
  username=str(input("enter your username: "))
  password=input("enter your password: ")
  phone=input("enter your phone number: ")
  user_data = {"username": username, "password": password, "phone": phone}

  print("signup successful")

  with open('Info.json', 'a') as f:
    json.dump(user_data,f)


 elif CHOOSE==2:

  username=str(input("enter your username: "))
  password=input("enter your password: ")
  with open('Info.json', 'r') as f: 
    data1=json.load(f)
    print(data1)
    if username in user_data and user_data[username]['password'] == password:
        print("Welcome USER")
    else:
        print("Incorrect username or password.")
            

    
 
    

 
  

  




  

 