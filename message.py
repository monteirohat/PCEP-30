from styles import Styles
from colors import Colors
from emoticons import Emoticons


sizeline = 60
sizeline2 = 62

class Message:

    def blue(text):
        print(f"{Colors.BLUE}{text}{Styles.ENDC}")

    def cyan(text):
        print(f"{Colors.CYAN}{text}{Styles.ENDC}")

    def green(text):
        print(f"{Colors.GREEN}{text}{Styles.ENDC}")

    def warning(text):
        print(f"{Colors.YELLOW}{text}{Styles.ENDC}")

    def fail(text):
        print(f"{Colors.RED}{text}{Styles.ENDC}")

    def bold(text):
        print(f"{Styles.BOLD}{text}{Styles.ENDC}")

    def underline(text):
        print(f"{Styles.UNDERLINE}{text}{Styles.ENDC}")

    def line(color=""):
        line = "\u2500"*sizeline2
        Colors.print_color(color, line)

    def line_dotted(color=""):
        line = "\u2212"*sizeline2
        Colors.print_color(color, line)

    def line_equal(color=""):
        line = "="*sizeline2
        Colors.print_color(color, line)

    def line_asterisk(color=""):
        line = "*"*sizeline2
        Colors.print_color(color, line)
    
    def line_arrows(color=""):
        line = "<"*int((sizeline2/2)-2) + " FIM " + ">"*int((sizeline2/2)-3)
        Colors.print_color(color, line)


    def title(text, bar = True):
        if bar == True:
            Message.bold(f"|" + " "*((int(sizeline/2)-int(len(text)/2))-1) +
                     text + " "*((int(sizeline/2)-int(len(text)/2))-1) + "|")
        else:
            Message.bold(f" "*((int(sizeline/2)-int(len(text)/2))-1) +
                     text + " "*((int(sizeline/2)-int(len(text)/2))-1))

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

    # -------------------------------------
    # Display Emoticons by UNICODE
    # -------------------------------------

    def help_emoticons():
        Message.line()
        Message.title("{} Help - Emoticons".format(Message.thinking_face()))
        Message.line()

        print('{} - grinning face \n'.format(Message.grinning_face()))
        print('{} - grinning face with big eyes \n'.format(Message.grinning_face_with_big_eyes()))
        print('{} - grinning face with smiling eyes \n'.format(
            Message.grinning_face_with_smiling_eyes()))
        print('{} - beaming face with smiling eyes \n'.format(Message.beaming_face_with_smiling_eyes()))
        print('{} - grinning squinting face \n'.format(Message.grinning_squinting_face()))
        print('{} - grinning face with sweat \n'.format(Message.grinning_face_with_sweat()))
        print('{} - rolling on the floor laughing \n'.format(Message.rolling_on_the_floor_laughing()))
        print('{} - face with tears of joy \n'.format(Message.face_with_tears_of_joy()))
        print('{} - slightly smiling face \n'.format(Message.slightly_smiling_face()))
        print('{} - upside-down face \n'.format(Message.upside_down_face()))
        print('{} - winking face \n'.format(Message.winking_face()))
        print('{} - smiling face with smiling eyes \n'.format(Message.smiling_face_with_smiling_eyes()))
        print('{} - smiling face with halo \n'.format(Message.smiling_face_with_halo()))
        print('{} - smiling face with 3 hearts \n'.format(Message.smiling_face_with_3_hearts()))
        print('{} - smiling face with heart-eyes \n'.format(Message.smiling_face_with_heart_eyes()))
        print('{} - star-struck \n'.format(Message.star_struck()))
        print('{} - face blowing a kiss \n'.format(Message.face_blowing_a_kiss()))
        print('{} - kissing face \n'.format(Message.kissing_face()))
        print('{} - smiling face \n'.format(Message.smiling_face()))
        print('{} - kissing face with closed eyes \n'.format(Message.kissing_face_with_closed_eyes()))
        print('{} - kissing face with smiling eyes \n'.format(Message.kissing_face_with_smiling_eyes()))
        print('{} - face savoring food \n'.format(Message.face_savoring_food()))
        print('{} - face with tongue \n'.format(Message.face_with_tongue()))
        print('{} - winking face with tongue \n'.format(Message.winking_face_with_tongue()))
        print('{} - zany face \n'.format(Message.zany_face()))
        print('{} - squinting face with tongue \n'.format(Message.squinting_face_with_tongue()))
        print('{} - money-mouth face \n'.format(Message.money_mouth_face()))
        print('{} - hugging face \n'.format(Message.hugging_face()))
        print(
            '{} - face with hand over mouth \n'.format(Message.face_with_hand_over_mouth()))
        print('{} - shushing face \n'.format(Message.shushing_face()))
        print('{} - thinking face \n'.format(Message.thinking_face()))
        print('{} - zipper-mouth face \n'.format(Message.zipper_mouth_face()))
        print('{} - face with raised eyebrow \n'.format(Message.face_with_raised_eyebrow()))
        print('{} - neutral face \n'.format(Message.neutral_face()))
        print('{} - expressionless face \n'.format(Message.expressionless_face()))
        print('{} - face without mouth \n'.format(Message.face_without_mouth()))
        print('{} - smirking face \n'.format(Message.smirking_face()))
        print('{} - unamused face \n'.format(Message.unamused_face()))
        print('{} - face with rolling eyes \n'.format(Message.face_with_rolling_eyes()))
        print('{} - grimacing face \n'.format(Message.grimacing_face()))
        print('{} - lying face \n'.format(Message.lying_face()))
        print('{} - relieved face \n'.format(Message.relieved_face()))
        print('{} - pensive face \n'.format(Message.pensive_face()))
        print('{} - sleepy face \n'.format(Message.sleepy_face()))
        print('{} - drooling face \n'.format(Message.drooling_face()))
        print('{} - sleeping face \n'.format(Message.sleepy_face()))
        print('{} - face with medical mask \n'.format(Message.face_with_medical_mask()))
        print('{} - face with thermometer \n'.format(Message.face_with_thermometer()))
        print('{} - face with head-bandage \n'.format(Message.face_with_head_bandage()))
        print('{} - nauseated face \n'.format(Message.nauseated_face()))

        Message.line_dotted()


    def grinning_face():
        return Emoticons.GRINNING_FACE

    def grinning_face_with_big_eyes():
        return Emoticons.GRINNING_FACE_WITH_BIG_EYES

    def grinning_face_with_smiling_eyes():
        return Emoticons.GRINNING_FACE_WITH_SMILING_EYES

    def beaming_face_with_smiling_eyes():
        return Emoticons.BEAMING_FACE_WITH_SMILING_EYES

    def grinning_squinting_face():
        return Emoticons.GRINNING_SQUINTING_FACE

    def grinning_face_with_sweat():
        return Emoticons.GRINNING_FACE_WITH_SWEAT

    def rolling_on_the_floor_laughing():
        return Emoticons.ROLLING_ON_THE_FLOOR_LAUGHING

    def face_with_tears_of_joy():
        return Emoticons.FACE_WITH_TEARS_OF_JOY

    def slightly_smiling_face():
        return Emoticons.SLIGHTLY_SMILING_FACE

    def upside_down_face():
        return Emoticons.UPSIDE_DOWN_FACE

    def winking_face():
        return Emoticons.GRINNING_FACE_WITH_SWEAT

    def smiling_face_with_smiling_eyes():
        return Emoticons.SMILING_FACE_WITH_SMILING_EYES

    def smiling_face_with_halo():
        return Emoticons.SMILING_FACE_WITH_HALO

    def smiling_face_with_3_hearts():
        return Emoticons.SMILING_FACE_WITH_3_HEARTS

    def smiling_face_with_heart_eyes():
        return Emoticons.SMILING_FACE_WITH_HEART_EYES

    def star_struck():
        return Emoticons.STAR_STRUCK

    def face_blowing_a_kiss():
        return Emoticons.FACE_BLOWING_A_KISS

    def kissing_face():
        return Emoticons.KISSING_FACE

    def smiling_face():
        return Emoticons.SMILING_FACE

    def kissing_face_with_closed_eyes():
        return Emoticons.KISSING_FACE_WITH_CLOSED_EYES

    def kissing_face_with_smiling_eyes():
        return Emoticons.KISSING_FACE_WITH_SMILING_EYES

    def face_savoring_food():
        return Emoticons.FACE_SAVORING_FOOD

    def face_with_tongue():
        return Emoticons.FACE_WITH_TONGUE

    def winking_face_with_tongue():
        return Emoticons.WINKING_FACE_WITH_TONGUE

    def zany_face():
        return Emoticons.ZANY_FACE

    def squinting_face_with_tongue():
        return Emoticons.SQUINTING_FACE_WITH_TONGUE

    def money_mouth_face():
        return Emoticons.MONEY_MOUTH_FACE

    def hugging_face():
        return Emoticons.HUGGING_FACE

    def face_with_hand_over_mouth():
        return Emoticons.FACE_WITH_HAND_OVER_MOUTH

    def shushing_face():
        return Emoticons.SHUSHING_FACE

    def thinking_face():
        return Emoticons.THINKING_FACE

    def zipper_mouth_face():
        return Emoticons.ZIPPER_MOUTH_FACE

    def face_with_raised_eyebrow():
        return Emoticons.FACE_WITH_RAISED_EYEBROW

    def neutral_face():
        return Emoticons.NEUTRAL_FACE

    def expressionless_face():
        return Emoticons.EXPRESSIONLESS_FACE

    def face_without_mouth():
        return Emoticons.FACE_WITHOUT_MOUTH

    def smirking_face():
        return Emoticons.SMIRKING_FACE

    def unamused_face():
        return Emoticons.UNAMUSED_FACE

    def face_with_rolling_eyes():
        return Emoticons.FACE_WITH_ROLLING_EYES

    def grimacing_face():
        return Emoticons.GRIMACING_FACE

    def lying_face():
        return Emoticons.LYING_FACE

    def relieved_face():
        return Emoticons.RELIEVED_FACE

    def pensive_face():
        return Emoticons.PENSIVE_FACE

    def sleepy_face():
        return Emoticons.SLEEPING_FACE

    def drooling_face():
        return Emoticons.DROOLING_FACE

    def sleeping_face():
        return Emoticons.SLEEPING_FACE

    def face_with_medical_mask():
        return Emoticons.FACE_WITH_MEDICAL_MASK

    def face_with_thermometer():
        return Emoticons.FACE_WITH_THERMOMETER

    def face_with_head_bandage():
        return Emoticons.FACE_WITH_HEAD_BANDAGE

    def nauseated_face():
        return Emoticons.NAUSEATED_FACE
