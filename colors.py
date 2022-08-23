from styles import Styles


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

    def print_color(color, text):
        if color == "":
            print(text)
        elif color == Colors.BLUE:
            print(f"{Colors.BLUE}{text}{Styles.ENDC}")
        elif color == Colors.CYAN:
            print(f"{Colors.CYAN}{text}{Styles.ENDC}")
        elif color == Colors.GREEN:
            print(f"{Colors.GREEN}{text}{Styles.ENDC}")
        elif color == Colors.RED:
            print(f"{Colors.RED}{text}{Styles.ENDC}")
        elif color == Colors.YELLOW:
            print(f"{Colors.YELLOW}{text}{Styles.ENDC}")
