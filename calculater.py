
def Creating_HistoryFile():
    f=open("History.txt","w")
    f.write("HISTORY")
    f.close

def Show_History():
    f=open("History.txt","r")
    lines=f.readlines()
    for line in (lines):
        print(line.strip())
    f.close

def Clear_History():
    f=open("History.txt","+w")
    f.write("HISTORY")
    f.close

def Calculater(): 
    f=open("History.txt","a+") 
    while True:
        input_1=float(input("Ente the number:"))

        operater=input("choice the operater(+,-,*,/):")
        operation=("+","-","*","/")
        while operater not in operation:
            print("The operater you hvae selected is invalid\nchoice again")
            operater=input("choice the operater(+,-,*,/):")

        input_2=float(input("Ente the number:"))

        if operater=="+":
            result=input_1+input_2
        elif operater=="-":
            result=input_1-input_2
        elif operater=="*":
            result=input_1*input_2
        elif operater=="/":
            result=input_1/input_2
        print(f"{input_1}{operater}{input_2}={result}")
        f.write(f"\n{input_1}{operater}{input_2}={result}")

        again=input("Do you want calculate again.Enter 'no' to exit:").strip().lower()
        if again=="no":
            f.close
            break
print("-------------")

def main():
    print("Welcome to 'My Calculater'")
    while True:
        choose=input("Enter calculation (+,-,*,/) or command(history,clear,exit):").strip().lower()
        if choose=="calculation":
            Calculater()
        elif choose=="history":
            Show_History()
        elif choose=="clear":
            Clear_History()
            print("The history is succesfully cleared")
        elif choose=="exit":
            print("Good bye ")
            break
        else:
            print(f"'{choose}' you have selected is invalid.Choose again")

call=main()
