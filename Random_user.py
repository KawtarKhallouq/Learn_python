from randomuser import RandomUser
import pandas as pd
#create a random user object
r = RandomUser()
#get a list of random 10 users
some_list = r.generate_users(10)
some_list

name = r.get_full_name()
for user in some_list:
    print (user.get_full_name()," ",user.get_email())
    
#generate photos ofthe random 10 users

for user in some_list:
    print (user.get_picture())
    
#generate table of informations
def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)     

get_users()

#generate data frame
df1 = pd.DataFrame(get_users())  


