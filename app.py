from message import Message
from colors import Colors

def header():
    print("")


def main():
    Message.line(Colors.YELLOW)
    Message.title("{} Welcome to Python - PCEP-30 {} ".format(Message.smiling_face_with_smiling_eyes(),Message.smiling_face_with_smiling_eyes()))
    Message.line(Colors.YELLOW)

    print('''--> This program is designed to assist you in preparatory \nstudies for the PCEP-30 certification.\n''')
    
    print("--> To get started, choose one of the options below:")
    
    
    Message.line_equal(Colors.YELLOW)


    #Message.help_emoticons()
    

if __name__ == "__main__":
    main()