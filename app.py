
from message import Message
from colors import Colors


def header():
    Message.line(Colors.YELLOW)
    Message.title("{} Welcome to Python - PCEP-30 {} ".format(Message.smiling_face_with_smiling_eyes(),Message.smiling_face_with_smiling_eyes()))
    Message.line(Colors.YELLOW)

    print('''--> This program is designed to assist you in preparatory \nstudies for the PCEP-30 certification.\n''')
    
    print("--> To get started, choose one of the options below:")

def menu_principal():
    Message.line()
    Message.title("MAIN MENU",False)
    Message.line()
    print("[1] - EXAMS")
    print("[2] - HELP")
    print("")
    return input("Option: ")
    

def menu_exams():
    Message.line()
    Message.title("EXAMS",False)
    Message.line()
    print("[1] - Exam1")
    print("[2] - Exam2")
    print("[3] - Exam3")
    print("[4] - Exam4")
    print("")
    return input("Option: ")

def menu_help():
    print("[1] - View Emoticons")
    print("[2] - About")

def footer():
    print("")
    Message.line_dotted(Colors.YELLOW)
    print("* Developer: André Monteiro")
    print("* Email: monteiro.hat@gmail.com")
    print("* Github: monteirohat")
    Message.line_dotted(Colors.YELLOW)
    Message.line_arrows(Colors.YELLOW)


def choice_menu(function,options):
    opt = None

    while(opt not in options):
        try:
            opt = int(function())

            if opt not in options:
                print("")
                Message.fail("--->>> Invalid option! <<<---")

        except Exception:
            pass

    
    return opt

def main():
    header()

    #Menu principal
    optm1 = (1,2)
    optm2 = (1,2,3,4)
    optm3 = (1,2)

    rmenu = choice_menu(menu_principal,optm1)

    if rmenu == 1:
        rexams = choice_menu(menu_exams,optm2)

        if rexams == 1:
            Message.blue("Exam 1")
        elif rexams == 2:
            Message.blue("Exam 2")
        elif rexams == 3:
            Message.blue("Exam 3")
        elif rexams == 4:
            Message.blue("Exam 4")


    elif rmenu == 2:
        rhelp = choice_menu(menu_help,optm3)

        if rhelp == 1:
            Message.help_emoticons()
        elif rhelp ==2:
            print("About...")


    footer()

    
    

if __name__ == "__main__":
    main()