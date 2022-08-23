from bgcolors import bcolors

sizeline = 60

class Message:
    

    def blue(text):
        print(f"{bcolors.BLUE}{text}{bcolors.ENDC}")

    def cyan(text):
        print(f"{bcolors.CYAN}{text}{bcolors.ENDC}")

    def green(text):
        print(f"{bcolors.GREEN}{text}{bcolors.ENDC}")

    def warning(text):
        print(f"{bcolors.YELLOW}{text}{bcolors.ENDC}")

    def fail(text):
        print(f"{bcolors.RED}{text}{bcolors.ENDC}")

    def bold(text):
        print(f"{bcolors.BOLD}{text}{bcolors.ENDC}")

    def underline(text):
        print(f"{bcolors.UNDERLINE}{text}{bcolors.ENDC}")

    def line(color=""):
        line = "\u2500"*sizeline
        if color == "":
            print(line)
        elif color == "blue":
            print(f"{bcolors.BLUE}{line}{bcolors.ENDC}")
        elif color == "cyan":
            print(f"{bcolors.CYAN}{line}{bcolors.ENDC}")
        elif color == "green":
            print(f"{bcolors.GREEN}{line}{bcolors.ENDC}")
        elif color == "red":
            print(f"{bcolors.RED}{line}{bcolors.ENDC}")

    def title(text):
        Message.bold(f" "*int(sizeline/2) + text + " "*int(sizeline/2))

    def show_examples():
        Message.line()
        Message.title("Exemples")
        Message.line()

        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

        Message.blue(text)
        Message.cyan(text)
        Message.green(text)
        Message.warning(text)
        Message.fail(text)
        Message.bold(text)
        Message.underline(text)
