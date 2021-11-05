import datetime

x = datetime.datetime.now()

def start():
        print("Hello you, I am Python")
        print("What is your name?")
        
        name = input('')
        
        print(f"Hello" + name)
        print (f"The current time is")
        print (x)

        print(name + "Do you want to do it again")
        answer = input("Type y or n;")

        if answer.lower() == "y":
            start()
        else:
            print("Until next time")
            exit()
    

start()