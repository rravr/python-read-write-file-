from typing import ValuesView

fn = open ("file1.txt","a+",)
ve = 'view'
while(ve =='view'):
    employee= open("file1.txt", "r+")
    
    print ( "                     +++ ENTER view TO VIEW File Content  +++ ")
    print (  "                     ++  ENTER no TO CREATE NEW ENTRY ++"          )
    ve = input("     To read file ... ENTER view 0R ENTER no FOR NEW ENTRY:")
    print ("                                                     ")
    if ve == 'view':
        
        a= ' '
        fn.seek(0)
        while (a):

            
            a=fn.readline()
            print(a)
            
            

    if ve == 'view':

        print("                  File Content  ")

        exit()


        
else:
    pass
   

word='yes'
while(word=='yes'):
    username=input ("Enter your UserName :  ")
    password = input("Enter your Password : " )
    Url = input("Enter your URL : ")
    Resource = input("Resource  : ")

    fn.write(str(username) +"  Password = "+password +" URL = "+Url +" Resource = "+Resource+"\n")
    fn.flush()
    word= input ("To make another New Entry .. ENTER yes or ENTER exit : ")
print ("                                        ")
print ("             +++ NEW ENTRY ADDED SUCCESSFULLY +++")
s =' '
fn.seek(0)
while(s):
    
    s=fn.readline()
    print(s)
fn.close()



