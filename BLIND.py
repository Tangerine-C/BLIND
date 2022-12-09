# Description:This project was made by Matthew J. Martinez in part of a
# Integration Project of the COP 1500 course of Florida Gulf Coast University.
# Blind is a text-based game where you are a rover operator controlling a rover
# to safety back to it's ship before it is destroyed or runs out of power.
# NOTE: This version will mainly be a main menu and opening secion test code
# (and a test mini-game).
# CITATIONS -    -   -   -   -   -   -   -   -  -   -   -   -   -   -   -   -
# Assistance for code from ThinkWithPython2 (PDF)
# https://www.geeksforgeeks.org/isupper-islower-upper-python-applications/ (
# FOR EXPLANATION OF TOPIC) https://www.geeksforgeeks.org/sleep-in-python/
# (FOR EXPLANATION OF TOPIC) https://appdividend.com/2022/07/14/how-to-stop
# -python-script-from-execution/# :~:text=To%20stop%20a%20python%20script,
# terminate%20Python%20script%20executi on%20programmatically. Above for
# exit() (Which closes, or kills, python's running code immediately)
# https://stackoverflow.com/questions/4099422/printing-slowly-simulate
# -typing The above was used in the def print_ and was not using the main
# topic but the responses to the topic to create a emulated human typing
# text then edited it to work with non-random variables (fixed). The
# following links helped explain sys.stdout, sys.stdout.write() and
# sys.stdout.flush() in better detail.
# https://www.geeksforgeeks.org/python-sys-stdout-flush/#:~:text=because
# %20call ing%20sys.-,stdout.,of%20the%20Python%20runtime%20environment.
# https://www.geeksforgeeks.org/sys-stdout-write-in-python/#:~:text=to%20the
# %20 screen.-,sys.,Unlike%20print%2C%20sys.
import time, sys, random


def calculating():
    """
    A Purely Visual Loading Sequence.
    """
    calc = 1
    for x in range(17):
        if calc == 8:
            calc = 1
            if calc == 1:
                spin = "[ | ]"
            elif calc == 2:
                spin = "[ / ]"
            elif calc == 3:
                spin = "[ — ]"
            elif calc == 4:
                spin = "[ \ ]"
            elif calc == 5:
                spin = "[ | ]"
            elif calc == 6:
                spin = "[ / ]"
            elif calc == 7:
                spin = "[ — ]"
            elif calc == 8:
                spin = "[ \ ]"
        else:
            if calc == 1:
                spin = "[ | ]"
            elif calc == 2:
                spin = "[ / ]"
            elif calc == 3:
                spin = "[ — ]"
            elif calc == 4:
                spin = "[ \ ]"
            elif calc == 5:
                spin = "[ | ]"
            elif calc == 6:
                spin = "[ / ]"
            elif calc == 7:
                spin = "[ — ]"
            elif calc == 8:
                spin = "[ \ ]"
        print('\r' + spin, end="")
        calc += 1
        time.sleep(0.25)
    print("\r" + "[Load Complete]")
    print("")


def human_(phrase):
    """
    Human is a printing program that attempts to replicate the typing
    patters of a normal human. Contrasting its partner Compute.
    :param phrase:This is anything that you want the program to print.
    """
    # printed. SOURCE: MODIFIED OFF BILL GROSS of stackoverflow.com
    # discussion linked in citations.
    for anything in phrase:  # This essentially states that for every
        # anything (STRING) found in phrase (or between the parenthesis) it
        # will use the following code
        sys.stdout.write(anything)  # This states that for every letter it
        # will write (similar to print) it out but does not create a new
        # line  for sub-sequential sys.stdout.write()s. (BUFFERED)
        sys.stdout.flush()  # Every letter that would usually be left in the
        # 'buffer' it will be 'flushed' into the terminal (or outputed)
        # consecutively instead of all at once.
        time.sleep(random.random() * 10.0 / TYPING_SPEED)  # Use of random
        # in action. Time between each letter will be randomized along to
        # create a psudo-human typing algoritm.
    print('')  # This moves to next line after the completion of the phrase
    # within the function. (print_, think_f,think_sf, and think_s all work
    # under similar principles.)


def compute_f(phrase):
    """
    Compute is a printing program that attempts to replicate the perfect typing
    patters of a computer. Prefix Variant (_f) Fast, denoting the
    0.0125 delay. This is usually the one used in all dialog.
    :param phrase:
        This is anything that you want the program to print.
    """
    for anything in phrase:
        sys.stdout.write(anything)
        sys.stdout.flush()
        time.sleep(.0125)
    print('')


def compute_sf(phrase):  # _sf denotes Super Fast. Faster of comp_f.
    """
    Compute is a printing program that attempts to replicate the perfect typing
    patters of a computer. Prefix Variant (_sf) Super Fast, denoting the
    0.000125 delay 100x faster than _f.
    :param phrase:
        This is anything that you want the program to print.
    """
    for anything in phrase:
        sys.stdout.write(anything)
        sys.stdout.flush()
        time.sleep(.000125)
    print('')


def comp_s(phrase):
    """
    Compute is a printing program that attempts to replicate the perfect typing
    patters of a computer. Prefix Variant (_s) Slow, denoting the
    0.25 delay.
    :param phrase:
        This is anything that you want the program to print.
    """
    for anything in phrase:
        sys.stdout.write(anything)
        sys.stdout.flush()
        time.sleep(.25)
    print('')


def check_1():  # Part of the Game introduction (part 1). Essentially goes
    """
    Similar to Calculating though used once. Purely Visual.
    """
    system = 1
    while system < 94:
        print('\r%' + str(system), end="")
        system += 1
        time.sleep(random.uniform(0.000125, 0.02))
    compute_f(' [PROBLEM DETECTED]')
    compute_f('\nSYSTEM ERROR: CAMERA SYSTEMS OBTAINING INSUFFICIENT VOLTAGE')
    time.sleep(2)
    compute_f('EVALUATING DAMAGE...')
    time.sleep(3)


def check_2():
    """
    Similar to Calculating though used once. Purely Visual.
    """
    evaluate = 1
    while evaluate < 101:  # Its not 100 because of < does not allow it to
        # get to 100 but using 101 stops at 100 instead of 99 I
        # alternatively  could use "while evaluate <= 100".
        print('\r%' + str(evaluate), end='')
        evaluate += 1
        time.sleep(random.uniform(0.000125, 0.02))
    compute_f(' [COMPLETE]')
    compute_f(
        '\nSEVERED CONNECTION TO VISUALS; CAUSE LOW VOLTAGE, MISSING POWER '
        'CORD.  VERDICT: WE ARE BLIND...')
    time.sleep(.5)


def diagnostics():
    """
    Holds calls to the visual functions, partly redundant, but it's fine.
    """
    compute_f('CHECKING MAIN SYSTEMS...')
    time.sleep(3)
    print("")
    check_1()
    time.sleep(1)
    print("")
    check_2()


def logo_ini():  # The first appearence of the title logo (slow)
    """
    A function for the first viewing of the logo of the game which slowly
    appears on screen. It is replaced with a faster version when returning
    from other areas of the menu. (unless from a game over)
    """
    compute_sf(
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
        '░')  # Use of Alt codes to generate computer pre-assigned graphics.
    compute_sf(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓░░░░░░▓▓▓▓▓▓▓░░▓▓▓▓▓░░░░░▓▓▓░░▓▓▓▓▓▓▓▓▓░░░░░░░'
        '░')  # Alt codes used are Alt + 176 and Alt + 179 respectively.
    compute_sf(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓▓▓▓░░░░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░')  # To those wanting to use these hold down the Alt key and type
    #  the numbers then release alt
    compute_sf(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░▓▓▓░░░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░')  # Number Pad is required, make sure to have Num Lock on.
    compute_sf(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░▓▓▓░░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░')
    compute_sf(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░░▓▓▓░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░')
    compute_sf(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░░░▓▓▓▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░')
    compute_sf(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓░░▓▓▓▓▓▓▓░░▓▓▓░░░░░▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓░░░░░░░'
        '░')
    compute_sf(
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
        '░')


def logo_comp():  # Completion of the game will show a star
    """
    When a completion of the game is noticed the menu will reflect that by
    showing a star next to the words 'BLIND'.
    """
    compute_sf(
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
        '░░░░▓▓░░░░░░░░░')  # Use of Alt codes to generate computer
    # pre-assigned graphics.
    compute_sf(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓░░░░░░▓▓▓▓▓▓▓░░▓▓▓▓▓░░░░░▓▓▓░░▓▓▓▓▓▓▓▓▓░░░░░░░░'
        '░░░▓▓▓▓░░░░░░░░')  # Alt codes used are Alt + 176 and Alt + 179
    # respectively.
    compute_sf(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓▓▓▓░░░░▓▓▓░░▓▓▓░░░░░▓▓▓░░'
        '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░')  # To those wanting to use these hold down
    # the Alt key and type the numbers then
    # release alt
    compute_sf(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░▓▓▓░░░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░▓▓'
        '▓▓▓▓▓▓▓▓▓▓▓▓░░░')  # Number Pad is required, make sure to have Num
    # Lock on.
    compute_sf(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░▓▓▓░░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░░'
        '▓▓▓▓▓▓▓▓▓▓░░░░░')
    compute_sf(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░░▓▓▓░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░░'
        '░▓▓▓▓▓▓▓▓░░░░░░')
    compute_sf(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░░░▓▓▓▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░▓▓▓▓▓▓▓▓▓▓░░░░░')
    compute_sf(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓░░▓▓▓▓▓▓▓░░▓▓▓░░░░░▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓░░░░░░░▓'
        '▓▓▓▓░░▓▓▓▓▓░░░░')
    compute_sf(
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓'
        '▓░░░░░░░░▓▓▓░░░')


def logo_comp_re():  # Completion of the game will show a star
    """
    When a completion of the game is noticed the menu will reflect that by
    showing a star next to the words 'BLIND'. Faster version.
    """
    print(
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
        '░░░░▓▓░░░░░░░░░')  # Use of Alt codes to generate computer
    # pre-assigned graphics.
    time.sleep(.0125)
    print(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓░░░░░░▓▓▓▓▓▓▓░░▓▓▓▓▓░░░░░▓▓▓░░▓▓▓▓▓▓▓▓▓░░░░░░░░'
        '░░░▓▓▓▓░░░░░░░░')  # Alt codes used are Alt + 176 and Alt + 179
    # respectively.
    time.sleep(.0125)
    print(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓▓▓▓░░░░▓▓▓░░▓▓▓░░░░░▓▓▓░░'
        '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░')  # To those wanting to use these hold down
    # the Alt key and type the numbers then
    # release alt
    time.sleep(.0125)
    print(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░▓▓▓░░░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░▓▓'
        '▓▓▓▓▓▓▓▓▓▓▓▓░░░')  # Number Pad is required, make sure to have Num
    # Lock on.
    time.sleep(.0125)
    print(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░▓▓▓░░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░░'
        '▓▓▓▓▓▓▓▓▓▓░░░░░')
    time.sleep(.0125)
    print(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░░▓▓▓░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░░'
        '░▓▓▓▓▓▓▓▓░░░░░░')
    time.sleep(.0125)
    print(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░░░▓▓▓▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░▓▓▓▓▓▓▓▓▓▓░░░░░')
    time.sleep(.0125)
    print(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓░░▓▓▓▓▓▓▓░░▓▓▓░░░░░▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓░░░░░░░▓'
        '▓▓▓▓░░▓▓▓▓▓░░░░')
    time.sleep(.0125)
    print(
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓'
        '▓░░░░░░░░▓▓▓░░░')


def logo_re():  # The other appearences of the title logo (fast)
    """
    The faster version of logo_ini I would bore the players to death if
    they had to see this intro every time they left a sub-menu.
    """
    print(
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
        '░')
    time.sleep(.0125)
    print(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓░░░░░░▓▓▓▓▓▓▓░░▓▓▓▓▓░░░░░▓▓▓░░▓▓▓▓▓▓▓▓▓░░░░░░░'
        '░')
    time.sleep(.0125)
    print(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓▓▓▓░░░░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░')
    time.sleep(.0125)
    print(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░▓▓▓░░░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░')
    time.sleep(.0125)
    print(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░▓▓▓░░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░')
    time.sleep(.0125)
    print(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░░▓▓▓░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░')
    time.sleep(.0125)
    print(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░░░▓▓▓▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░')
    time.sleep(.0125)
    print(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓░░▓▓▓▓▓▓▓░░▓▓▓░░░░░▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓░░░░░░░'
        '░')
    time.sleep(.0125)
    print(
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
        '░')


def main_menu1(wins):  # Main menu for game
    """
    This is the first
    :param wins:
    """
    if int(wins) == 0:
        logo_ini()
    elif int(wins) >= 1:
        logo_comp()
    print(' ')
    print(' ')
    print('Type start, To begin')  # Not Done
    time.sleep(.25)
    print('Type ?, For Explanation')  # Not Done
    time.sleep(.25)
    print('Type credit, For Credits')  # Probably needs more for a Credits
    # (plural)
    time.sleep(.25)
    print('Type end, To Quit')  # Works :)
    time.sleep(.25)
    print('Type test, for python math test.')
    while True:  # This is the Directory for the main menu, input tell the
        # code where you want to go.
        state = str.lower(input())
        if state == 'start':
            start(wins)
        elif state == '?':
            explain_menu(wins)
        elif state == 'credit':
            credit(wins)
        elif state == 'end':
            end()
        elif state == 'test':
            test(wins)
        elif state == '0/0':  # For Reference causes Memory Error will not
            # show  in later versions, but I will keep because it's funny.
            print("?" * 100 ** 9)
        else:
            print('')
            human_('That is not a choice Operator ' + str.capitalize(
                operator) + ".")


def main_menu2(wins):  # The only difference between this and the menu
    # above is
    # that it loads the logo faster using loge_re(use) instead of  logo_ini(
    # tial)
    if int(wins) == 0:
        logo_re()
    elif int(wins) >= 1:
        logo_comp_re()
    print(' ')
    print(' ')
    print('Type start, To begin')  # Not Done
    time.sleep(.25)
    print('Type ?, For Explaination')  # Not Done
    time.sleep(.25)
    print(
        'Type credit, For Credits')  # Probably needs more for a Credits
    # (plural)
    time.sleep(.25)
    print('Type end, To Quit')  # Works :)
    time.sleep(.25)
    print('Type test, for python math test')  # Remove Later
    while True:
        state = str.lower(input())
        if state == 'start':
            start(wins)
        elif state == '?':
            explain_menu(wins)
        elif state == 'credit':
            credit(wins)
        elif state == 'end':
            end()
        elif state == 'test':
            test(wins)
        elif state == '0/0':  # For Reference causes Memory Error will not show
            # in later versions but I will keep because its funny.
            print("?" * 100 ** 9)
        else:
            print('')
            human_('That is not a choice ' + str.capitalize(operator) + ".")


def test(wins):
    print('')
    print('')
    human_('Hello Operator ' + str.capitalize(
        operator) + " let us, Mission Control, test your python math skills.")
    # CONCATENATION, makes different values (str) come together* in one -
    human_('What is 125 + 75?')  # -print statement. *It concatenates
    while True:
        question1 = int(
            input())  # Addition Explaination in the literal statement if you
        # get it wrong.
        if question1 == 200:
            print('')
            human_('Good, Next one.')
            time.sleep(1)
            break
        else:
            print('')
            human_(
                'Nope, Try again. Remember addition is the sum of two values.')
    human_(
        'What is 125 - 75?')  # Subtraction Explaination in the literal
    # statement if you get it wrong.
    while True:
        question2 = int(input())
        if question2 == 50:
            print('')
            human_('Good, Next one.')
            time.sleep(1)
            break
        else:
            print('')
            human_(
                'Nope, Try again. Remember subtraction is the sum of the'
                'difference between two values.')
    human_(
        'What is 100 * 4?')  # Multiplication Explaination in the literal
    # statement if you get it wrong.
    while True:
        question3 = float(input())
        if question3 == 400:
            print('')
            human_('Good, Next one.')
            time.sleep(1)
            break
        else:
            print('')
            human_(
                'Nope, Try again. Remember multiplication is the iterations'
                ' of a number used and the sum of those iterations.')
    human_(
        'What is 125 / 25?')  # Division Explaination in the literal
    # statement  if you get it wrong.
    while True:
        question4 = int(input())
        if question4 == 5:
            print('')
            human_('Good, Next one.')
            time.sleep(1)
            break
        else:
            print('')
            human_(
                'Nope, Try again. Remember division is how many times the '
                'value of another number can fit into the dividend'
                '(The number being divided).')
    human_(
        'What is 5 ** 3?')  # Exponent Explaination in the literal statement
    #  if you get it wrong.
    while True:
        question5 = int(input())
        if question5 == 125:
            print('')
            human_('Good, Next one.')
            time.sleep(1)
            break
        else:
            print('')
            human_(
                'Nope, Try again. Remember that "**" makes the value following'
                ' it an exponent for the initial value.')
    human_(
        'What is 10 // 3?')  # Floor Division Explaination in the literal
    # statement if you get it wrong.
    while True:
        question6 = int(input())
        if question6 == 1:
            print('')
            human_('Good, Next one.')
            time.sleep(1)
            break
        else:
            print('')
            human_(
                'Nope, Try again. Remember that "//" is not normal division,'
                ' it is floor division which is used to calculate a remainder'
                ' left over after division.')
    human_(
        'What is 10 % 3?')  # Modulus Explaination in the literal statement
    # if you get it wrong.
    while True:
        question7 = int(input())
        if question7 == 3:
            print('')
            break
        else:
            print('')
            human_(
                'Nope, Try again. Remember that "%" is modulus which finds how'
                ' many times a value can fit into another leaving out '
                'remainders and decimals.')
    human_('Good job operator, you seem to know your stuff.')
    comp_s('EXAMINATION OVER')
    print('GOOD JOB!', 'GOOD JOB!', 'GOOD JOB!',
          sep=' ')  # sep= changes what , is defined as (or it's behavior)
    # what I did essentially just made comma the same though as it just made
    # comma space.
    back(wins)


def end():
    print(' ')
    print(' ')
    comp_s('GOING INTO REST MODE...\n GOODNIGHT, ' + str.upper(operator))
    time.sleep(1)
    exit()


def credit(wins):
    print(' ')
    print(' ')
    compute_f('Credits')
    time.sleep(2)
    compute_f(
        'Blind is made by Matthew J. Martinez, Undergraduate (at time of'
        ' creation) at Florida Gulf Coast University.')
    back(wins)


def back(wins):
    time.sleep(2)
    print(' ')
    compute_f('Return? (y/n)')
    while True:
        state = str.lower(input())
        if state == 'y':
            print(' ')
            print(' ')
            main_menu2(wins)
        if state == 'n':
            comp_s('Okay...')
            comp_s('.')
            time.sleep(2)
            comp_s('..')
            time.sleep(2)
            comp_s('...')
            time.sleep(1)
            print(' ')
            compute_f('Now do you want to return? (y/n)')


def start(wins):
    print(' ')
    print(' ')
    game_main(wins)


def explain_menu(wins):  # Explains concepts about the game (this is accessed
    """
    This is a proper explanation on the content within the game. Accessed
    through the main menu.
    :param wins: How many times the player has completed the game, needs to
    be passed through to allow the menu and game_main to receive the
    information
    """
    # through menu). REVISIONS PROBABLE
    print(' ')
    print(' ')
    human_('This is Mission Control.')
    human_('You are instructed to bring back a T.E.R.R.A rover from')
    human_('PSR J1719-14 C, a comet on the far end of the Serpens Cauda'
           ' constellation')
    human_("as the carbon based crystal on the comet's surface are required"
           " for research.")
    human_('Shortly after landing, the rover was ejected pre-maturely and '
           'needs to return to the craft')
    human_('before the rover runs out of power. The comet is more stable than'
           ' it was 700 years')
    human_('ago so it should not be as bad to navigate.')
    human_('Our signal is still shoddy so I may take a while for commands to '
           'go through about an hour or so.')
    human_('The onboard AI will assist with translating commands, but will '
           'enforce any regulations we have placed over your commands')
    print(' ')
    human_('The rover is able to move and has features to assist in its '
           'retrieval.')
    human_('Solar power is available at times due to the rapid nature of the'
           ' planet.')
    human_('The command charge can recover some power.')
    human_('Charging can only be used once every four hours (*read: turns) '
           'due to the high amounts of heat.')
    human_('Emanating from the panels potentially damaging rover components.')
    human_('The command forward allows movement ahead.')
    human_('The command turn left/right allow rotation.')
    human_('Parts of the rover can be damaged. Do not allow this to occur.')
    human_('Damaged parts make certain actions more difficult, like losing '
           'maximum energy storage.')
    human_("Events may occur during your time on the planet, they may better "
           "your way back or may hamper it, be mindful of that fact.")
    human_('This is the end of the explanation.')
    back(wins)


def explain_game():  # Explains concepts about the game (this is accessed
    """
    This is a proper explanation on the content within the game. Accessed
    through game_main.
    """
    # through the game start if you did not read it and want to view).
    # REVISIONS PROBABLE
    print(' ')
    print(' ')
    human_('As you should know, this is Mission Control.')
    human_('You are instructed to bring back a T.E.R.R.A rover from')
    human_('PSR J1719-14 C, a comet on the far end of the Serpens Cauda'
           ' constellation')
    human_("as the carbon based crystal on the comet's surface are required"
           " for research.")
    human_('Shortly after landing, the rover was ejected pre-maturely and '
           'needs to return to the craft')
    human_('before the rover runs out of power. The comet is more stable than'
           ' it was 700 years')
    human_('ago so it should not be as bad to navigate.')
    human_('Our signal is still shoddy so I may take a while for commands to '
           'go through about an hour or so.')
    human_('The onboard AI will assist with translating commands, but will '
           'enforce any regulations we have placed over your commands')
    print(' ')
    human_('The rover is able to move and has features to assist in its '
           'retrieval.')
    human_('Solar power is available at times due to the rapid nature of the'
           ' planet.')
    human_('The command charge can recover some power.')
    human_('Charging can only be used once every four hours (*read: turns) '
           'due to the high amounts of heat.')
    human_('Emanating from the panels potentially damaging rover components.')
    human_('The command forward allows movement ahead.')
    human_('The command turn left/right allow rotation.')
    human_('Parts of the rover can be damaged. Do not allow this to occur.')
    human_('Damaged parts make certain actions more difficult, like losing '
           'maximum energy storage.')
    human_("Events may occur during your time on the planet, they may better "
           "your way back or may hamper it, be mindful of that fact.")
    human_('This is the end of the explanation.')
    print(' ')
    human_('Do you understand? (y/n)')
    understanding = True
    while understanding:
        understand = input()
        if understand == str.lower('y'):
            understanding = False  # Ironically
        if understand == str.lower('n'):
            print('')
            human_('Then read it again.')


def location_Rover_ini(location):  # Gives the Rover its initial location. Does
    """
    This is the first location you start. This is separate from the other
    code that denotes location and presents you with an event (location_Rover)
   1   2   3   4   5       On the left is what I will call the 'array' in
   6   7   8   9   10      which is the principle movement system of the
   11  12  13  14  15      game  and how I will be able
   16  17  18  19  20      principle movement system of the game and how  I
   20  22  23  24  25      will be able to create and simplifiy the code
  for  this segment so it will not be completely redundently inefficent by
  using  a movement system such as moving "Down" or  foward looking from A1
  (1) to B1 (6) it will add 5 to the a 'location' value and going from  A1 (
  1)  to A2 (2) it will simply add 1. When going to values above this still
  may be foward, it will subtract values of 1 when going left and 5 when
  going up the array. The definitions below are going to be all called by a
  long if/elif statement. .Rotations will be tracked with a number of 1
  through 4. 1 being North, 2 East, 3 South, and 4 West as shown by the compass
            N              on the left.
            1
        W4     2E
            3
            S

    :param location:
    """
    # not
    # need to track rotation as you will just be there and not being moving
    # into it.
    if location == 1:
        compute_f('WE ARE IN THE A1 BOUNDARY LINE, FURTHER MOVEMENT NORTH '
                  'AND WEST IS PROHIBITED')
    elif location == 2:
        compute_f('WE ARE IN THE A2 AREA, FURTHER MOVEMENT NORTH IS '
                  'PROHIBITED')
    elif location == 3:
        compute_f('WE ARE IN THE A3 AREA, FURTHER MOVEMENT NORTH IS '
                  'PROHIBITED')
    elif location == 4:
        compute_f('WE ARE IN THE A4 AREA, FURTHER MOVEMENT NORTH IS '
                  'PROHIBITED')
    elif location == 5:
        compute_f('WE ARE IN THE A5 BOUNDARY LINE, FURTHER MOVEMENT NORTH'
                  'AND EAST IS PROHIBITED')
    elif location == 6:
        compute_f('WE ARE IN THE B1 BOUNDARY LINE, FURTHER MOVEMENT WEST IS '
                  'PROHIBITED')
    elif location == 7:
        compute_f('WE ARE IN THE B2 AREA, FREE MOVEMENT IS AVAILABLE')
    elif location == 8:
        compute_f('WE ARE IN THE B3 AREA, FREE MOVEMENT IS AVAILABLE')
    elif location == 9:
        compute_f('WE ARE IN THE B4 AREA, FREE MOVEMENT IS AVAILABLE')
    elif location == 10:
        compute_f('WE ARE IN THE B5 BOUNDARY LINE, FURTHER MOVEMENT EAST IS '
                  'PROHIBITED')
    elif location == 11:
        compute_f('WE ARE IN THE C1 BOUNDARY LINE, FURTHER MOVEMENT WEST IS '
                  'PROHIBITED')
    elif location == 12:
        compute_f('WE ARE IN THE C2 AREA, FREE MOVEMENT IS AVAILABLE')
    elif location == 13:
        compute_f('WE ARE IN THE C3 AREA, FREE MOVEMENT IS AVAILABLE')
    elif location == 14:
        compute_f('WE ARE IN THE C4 AREA, FREE MOVEMENT IS AVAILABLE')
    elif location == 15:
        compute_f('WE ARE IN THE C5 BOUNDARY LINE, FURTHER MOVEMENT EAST IS '
                  'PROHIBITED')
    elif location == 16:
        compute_f('WE ARE IN THE D1 BOUNDARY LINE, FURTHER MOVEMENT WEST IS '
                  'PROHIBITED')
    elif location == 17:
        compute_f('WE ARE IN THE D2 AREA, FREE MOVEMENT IS AVAILABLE')
    elif location == 18:
        compute_f('WE ARE IN THE D3 AREA, FREE MOVEMENT IS AVAILABLE')
    elif location == 19:
        compute_f('WE ARE IN THE D4 AREA, FREE MOVEMENT IS AVAILABLE')
    elif location == 20:
        compute_f('WE ARE IN THE D5 BOUNDARY LINE, FURTHER MOVEMENT EAST IS '
                  'PROHIBITED')
    elif location == 21:
        compute_f('WE ARE IN THE E1 BOUNDARY LINE, FURTHER MOVEMENT SOUTH '
                  'AND WEST IS PROHIBITED')
    elif location == 22:
        compute_f('WE ARE IN THE E2 AREA, FURTHER MOVEMENT SOUTH IS '
                  'PROHIBITED')
    elif location == 23:
        compute_f('WE ARE IN THE E3 AREA, FURTHER MOVEMENT SOUTH IS '
                  'PROHIBITED')
    elif location == 24:
        compute_f('WE ARE IN THE E4 AREA, FURTHER MOVEMENT SOUTH IS '
                  'PROHIBITED')
    elif location == 25:
        compute_f('WE ARE IN THE E5 AREA, FURTHER MOVEMENT SOUTH AND EAST IS '
                  'PROHIBITED')


# -----------------AREA CODES--------------------------------------------------
def a1(values):  # EDGE NORTH WEST
    compute_f(
        "WE ARE IN THE A1 BOUNDARY LINE. FURTHER MOVEMENT NORTH OR WEST IS "
        "PROHIBITED.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) \
            == values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def a2(values):  # EDGE
    compute_f("WE ARE IN THE A2 BOUNDARY LINE. FURTHER MOVEMENT NORTH IS "
              "PROHIBITED.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) \
            == values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def a3(values):  # EDGE NORTH
    compute_f("WE ARE IN THE A3 BOUNDARY LINE. FURTHER MOVEMENT NORTH IS "
              "PROHIBITED.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def a4(values):  # EDGE
    compute_f("WE ARE IN THE A4 BOUNDARY LINE. FURTHER MOVEMENT NORTH IS "
              "PROHIBITED.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def a5(values):  # EDGE NORTH EAST
    compute_f("WE ARE IN THE A5 BOUNDARY LINE. FURTHER MOVEMENT NORTH OR EAST "
              "IS PROHIBITED.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def b1(values):  # EDGE
    compute_f("WE ARE IN THE B1 BOUNDARY LINE. FURTHER MOVEMENT WEST IS "
              "PROHIBITED.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def b2(values):  # INNER EDGE
    compute_f("WE ARE IN THE B2 AREA, FREE MOVEMENT AVAILABLE.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def b3(values):  # INNER EDGE
    compute_f("WE ARE IN THE B3 AREA, FREE MOVEMENT AVAILABLE.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def b4(values):  # INNER EDGE
    compute_f("WE ARE IN THE B4 AREA, FREE MOVEMENT AVAILABLE.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def b5(values):  # EDGE
    compute_f("WE ARE IN THE B5 BOUNDARY LINE, FURTHER MOVEMENT EAST IS "
              "PROHIBITED.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def c1(values):  # EDGE WEST
    compute_f("WE ARE IN THE C1 BOUNDARY LINE, FURTHER MOVEMENT WEST IS "
              "PROHIBITED.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def c2(values):  # INNER EDGE
    compute_f("WE ARE IN THE C2 AREA, FREE MOVEMENT AVAILABLE.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def c3(values):  # CENTER
    compute_f("WE ARE IN THE C3 AREA, FREE MOVEMENT AVAILABLE.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def c4(values):  # INNER EDGE
    compute_f("WE ARE IN THE C4 AREA, FREE MOVEMENT AVAILABLE.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def c5(values):  # EDGE EAST
    compute_f("WE ARE IN THE C5 BOUNDARY LINE, FURTHER MOVEMENT EAST IS "
              "PROHIBITED.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def d1(values):  # EDGE
    compute_f("WE ARE IN THE D1 BOUNDARY LINE, FURTHER MOVEMENT WEST IS "
              "PROHIBITED.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def d2(values):  # INNER EDGE
    compute_f("WE ARE IN THE D2 AREA, FREE MOVEMENT AVAILABLE.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def d3(values):  # INNER EDGE
    compute_f("WE ARE IN THE D3 AREA, FREE MOVEMENT AVAILABLE.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def d4(values):  # INNER EDGE
    compute_f("WE ARE IN THE D4 AREA, FREE MOVEMENT AVAILABLE.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def d5(values):  # EDGE
    compute_f("WE ARE IN THE D5 BOUNDARY LINE, FURTHER MOVEMENT EAST IS "
              "PROHIBITED.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def e1(values):  # EDGE SOUTH WEST
    compute_f("WE ARE IN THE E1 BOUNDARY LINE, FURTHER MOVEMENT WEST IS "
              "PROHIBITED.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def e2(values):  # EDGE
    compute_f("WE ARE IN THE E2 AREA, FREE MOVEMENT AVAILABLE.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def e3(values):  # EDGE SOUTH
    compute_f("WE ARE IN THE E3 AREA, FREE MOVEMENT AVAILABLE.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def e4(values):  # EDGE
    compute_f("WE ARE IN THE E4 AREA, FREE MOVEMENT AVAILABLE.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def e5(values):  # EDGE SOUTH EAST
    compute_f("WE ARE IN THE E5 BOUNDARY LINE, FURTHER MOVEMENT EAST IS "
              "PROHIBITED.")
    if not values[4] == values[5]:
        compute_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (values[4] + 5 or values[4] + 1 or values[4] - 1 or values[4] - 5) == \
            values[5]:
        compute_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    values = event_trigger(values)
    return values


def game_over(values):
    calculating()
    human_(
        "Connection with the rover has been lost. All reconnection attempts"
        " have failed.")
    human_(
        "This mission is a failure. Report to the staging room for"
        " debriefing.")
    print('')
    wins = values[14]
    print('')
    main_menu1(wins)


def value_Check(completions):
    """
    This generates the initial set of values that are needed for the game to
    run.
    :param completions: This parameter brings the save data of completions
    into the main code (not really necessary but helps).
    :return: Sends the code to the designation stats then that is sent to
    game(values)
    """
    turns = 0
    rotation = random.randrange(1, 5, 1)
    charge = 10  # Essentially the health stat for the rover once this hits
    # zero its is game over.(There is only a few other non battery game overs.)
    fate_Rover = 0  # Fate is a stat that will determine if you instanly
    # recieve a game over from a Major Event. It is calculated within the
    # events. (1 - 100)
    fate_Number_Rover = random.randrange(1, 100, 1)
    # This is the number that will cause fate to cause a game over to occur, it
    # will be random every game start.)
    while fate_Rover == fate_Number_Rover:
        fate_Number_Rover = random.randrange(1, 100, 1)
    fate_Ship = 0
    fate_Number_Ship = random.randrange(1, 100, 1)
    while fate_Ship == fate_Number_Ship:
        fate_Number_Ship = random.randrange(1, 100, 1)
    battery = 20  # Battery is what the maximum amount of energy that can be
    # held at a time, can be reduced through events, you can not gain more.
    local_Rover = random.randrange(1, 26, 1)  # This is to generate a random
    # value between 1 and 25 to allow a random spawn for the rover(you)
    local_Ship = random.randrange(1, 26, 1)  # This is to generate a random
    # value between 1 and 25 to allow a random spawn for the ship(objective)
    while local_Rover == local_Ship or local_Rover == local_Ship - 1 or \
            local_Rover == local_Ship + 1 or local_Rover == local_Ship + 5 \
            or local_Rover == local_Ship - 5:
        local_Ship = random.randrange(1, 26, 1)  # This makes sure that the
        # rover and the ship do not spawn(or have the same value) on each
        # other (or near) ending the game instantly/quickly.
    rotation_charge = 0
    event_number = 0
    ini = 1
    charge_cooldown = 4  # This is the cool down for the rover's charge ability
    wins = completions
    values = [turns, rotation, charge, battery, local_Rover, local_Ship,
              fate_Rover, fate_Number_Rover, fate_Ship, fate_Number_Ship,
              rotation_charge, event_number, ini, charge_cooldown, wins]
    return values


TYPING_SPEED = 120  # Required for human_(phrase)'s random time algorithm.


# Not a problem as a global never used for anything else


def game_main(completions):
    intro = True
    while intro:
        intro_play = str.lower(input("Play Intro? [RECOMMENDED] (Y/N)"))
        if intro_play == "y" or intro_play == "yes":
            human_('Welcome Operator ' + str.capitalize(operator) + ' We will '
                                                                    'proceed to the mission phase.')
            human_(
                'We assume you have been debriefed on the mission. You have '
                'right?')
            explain = True
            while explain:
                knowledge = input('(y/n)')
                if knowledge == str.lower('y'):
                    explain = False
                elif knowledge == str.lower('n'):
                    explain_game()  # IT EXISTS IN REAL CODE
                    explain = False
                else:
                    human_("That is not y or n operator!")
            print('')
            print('')
            human_('We will now relay information on the rover to you.')
            human_('Patching...')
            calculating()
            time.sleep(1)
            compute_f('HELLO OPERATOR')
            time.sleep(1)
            compute_f('CURRENT TEMPERATURE IS 300 DEGREES CELCIUS.')
            time.sleep(1)
            compute_f('CURRENT PHYSICAL STATE... FINE.')
            time.sleep(1)
            compute_f(
                'CURRENT SYSTEMS ARE 93% OPERATIONAL. VISUAL OPTICS ARE NOT '
                'FUNCTIONING. AUTO-PILOT MODULES ARE UNRESPONSIVE.')
            time.sleep(1)
            compute_f(
                'WE WILL HAVE TO RELY ON SURFACE SCAN EQUIPMENT TO VISUALIZE OUR '
                'LOCATION AND I WILL RELY ON YOUR CONTROL.')
            calculating()
            compute_f('I WILL BE IN YOUR CARE OPERATOR, PLEASE KEEP ME WELL.')
            print('')
            print('')
            time.sleep(1)
            human_('Mission Control here, we have given you manual control.')
            human_('From here on out it will be just you and your rover.')
            human_(
                'The rover should automatically relay locational information to you '
                'with every movement.')
        elif intro_play == "n" or intro_play == "no":
            intro = False
        else:
            print("That's not 'yes' or 'no' operator")
    human_("If you forget commands 'help' will relay control information.")
    human_('Good luck Operator.')
    print('')
    print('')
    stats = value_Check(completions)
    game(stats)


def repair_1():
    """
    Purely Visual
    """
    evaluate = 1
    while evaluate < 101:  # Its not 100 because of < does not allow it to
        # get to 100 but using 101 stops at 100 instead of 99 I
        # alternatively  could use "while evaluate <= 100".
        print('\r%' + str(evaluate), end='')
        evaluate += 1
        time.sleep(random.uniform(0.000125, 0.02))
    compute_f('[POWER SYSTEMS RESTORED]')
    time.sleep(.5)
    compute_f('\nTHE ENERGY SPIKE CAUSED HEAVY ENERGY LOSS WITHIN OUR '
              'BATTERY.')
    time.sleep(.5)


# --------------EVENTS---------------------------------------------------------
def event_trigger(event):  # This set of code generates a value and presents a
    """
    function event_trigger: This grants the player a random event based
    off a generated value. This could hurt or help the player.
    :param event: Event is still the list of data that game_main generated.
    But event_trigger primarily uses [11] from that list or event_value,
    along with some others.
    :return: Information on the event that just occurred. Specifically the
    value tied to that event.
    """
    # situation based off the random value generated (within a range)
    event[11] = random.randrange(0, 101, 1)
    if event[11] >= 0 and event[11] <= 10:
        compute_f("RADIATION DECREASE: THE SKY IS EMPTY.")
        time.sleep(1)
        print("CHARGE EFFICIENCY: " + "[?]", end="")
        for x in range(30):
            efficiency = random.uniform(40.999, 60.999, )
            print("\rCHARGE EFFICIENCY: %" + str(format(efficiency, ".2f")),
                  end="")
            time.sleep(0.1)

        compute_f("\nNOTHING MORE TO REPORT.")

    elif event[11] >= 11 and event[11] <= 13:
        compute_f("LARGE UNKNOWN ENERGY SPIKE, NO COUNTER MEASURES PREPARED")
        time.sleep(.5)
        compute_f("POW9r inSTaBIlITY D-23cTED")
        print("r" * 20)
        compute_f("rESe7ING Br3AKER")
        time.sleep(.5)
        repair_1()
        event[2] += -5
    elif event[11] == 14 or event[11] == 16:
        compute_f("SPIKE IN AVAILABLE SUNLIGHT DETECTED. OUR SOLAR CHARGING "
                  "WILL BE MORE EFFECTIVE.")
        compute_f("WE DODGED A SOLAR FLARE")
    elif event[11] == 15:  # MAJOR EVENT: SOLAR FLARE | The rarer harsher
        # events, can end the game by itself.
        compute_f(
            '[WARNING] MAJOR SPIKE IN AVAILABLE SUNLIGHT DETECTED.'
            ' TEMPERATURES RISING TO UNSUITABLE LEVELS')
        compute_f('INTERNAL TEMPERATURE OVER 78 DEGREES CELSIUS.')
        compute_f('OVERRIDING OPERATOR CONTROL. DISABLING ALL SYSTEMS NON-'
                  'ESSENTIAL'
                  ' TO SURVIVAL AND REROUTING ALL POWER TO COOLING SYSTEMS.')
        compute_f('DISABLING CONNECTION')
        human_(
            'We have lost connection with the rover, we are pulling up'
            ' satellite imagery to see the situation.')
        human_("It doesn't look good...")
        compute_sf(
            '▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░░░░░░░▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░░░░░░▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░░░░░░▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░░░░░▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░░░░░▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓░░░▓▓▓░▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓░░▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓'
            '▓▓▓▓▓▓▓▓░▓▓▓▓▓░░▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓'
            '▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓'
            '▓▓░▓▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░'
            '▓▓▓░▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓░▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓'
            '░▓▓▓▓░▓▓▓░▓▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓░▓▓▓░▓▓░▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓░▓▓'
            '▓░▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓░▓▓▓░▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓░▓▓░▓'
            '▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓'
            '▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓░▓▓'
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓'
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓'
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓'
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        compute_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓'
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        time.sleep(2)
        human_(
            "The sun is in very close proximity to the comet. There will be a"
            " large spike in temperatures.")
        human_(
            "The rover is sturdier then most but it's systems still have a"
            " sensitive melting point, specifically the battery.")
        human_("We will keep checking for connection to the rover, standby.")
        calculating()
        sun_spot = random.randrange(-3, -10, -1)
        event[2] += sun_spot
        sun_spot_damage = random.randrange(-1, -5, -1)
        event[3] += sun_spot_damage
        event[6] = random.randrange(1, 100, 1)
        if event[6] == 42:
            event[2] = 0  # GAME OVER
        else:
            compute_f("CONNECTION REESTABLISHED")
            compute_f("REVIEWING DAMAGE")
            if sun_spot <= -6 and sun_spot >= -10:
                compute_f(
                    'HIGH ENERGY USAGE REQUIRED FOR OPTIMAL COOLING WE HAVE'
                    ' LOST A LARGE AMOUNT OF ENERGY.')
            elif sun_spot <= -3 and sun_spot >= -5:
                compute_f('OPTIMAL ENERGY USAGE REQUIRED FOR COOLING.')
                time.sleep(1)
                comp_s('WE GOT LUCKY...')
            if sun_spot_damage >= -5 and sun_spot_damage <= -3:
                compute_f('SUBSTANTIAL DAMAGE RECEIVED TO POWER CORE')
                compute_f('CURRENTLY IRREPARABLE, OUR ENERGY STORAGE WILL BE'
                          ' MODERATELY REDUCED TO AVOID FURTHER DAMAGE.')
            if sun_spot_damage >= -2 and sun_spot_damage <= -1:
                compute_f('MINOR DAMAGE RECEIVED TO POWER CORE')
                compute_f('CURRENTLY IRREPARABLE, OUR ENERGY STORAGE WILL BE'
                          ' SLIGHTLY REDUCED TO AVOID FURTHER DAMAGE.')
            event[13] += random.randrange(0,-6,-2)
    elif event[11] == 26:  # MAJOR EVENT: METEOR SHOWER
        compute_f(
            "[WARNING] THE COMET IS RAPIDLY APPROACHING SOLAR SYSTEM'S"
            " ASTROID BELT")
        compute_f("STELLAR MASS RAPIDLY ENTERING COMET")
        compute_f("IMPACTS PROBABLE. AREAS MAY RECEIVE DAMAGE.")
        compute_f("BRACING...")
        calculating()
        event[6] = random.randrange(1, 100, 1)
        if event[6] == event[8]:
            event[2] = 0  # GAME OVER
        else:
            compute_f("ROVER MAIN UNIT WAS UNAFFECTED BY METEOR IMPACTS.")
            compute_f("AREAS AROUND THE MISSION AREA HAVE BEEN AFFECTED HOW"
                      "EVER.")
            compute_f("CHECKING FOR SHIP SIGNAL.")
            event[8] = random.randrange(1, 100, 1)
        if event[8] == event[9]:
            event[2] = 0
        else:
            compute_f("SIGNAL RESPONSE RECEIVED.")
            compute_f("OUR CRAFT IS STILL OPERATIONAL.")
            compute_f("LET US MOVE ON WITH THE MISSION.")
    if event[11] >= 27 and event[11] <= 100:
        compute_f("RADIATION INCREASE: THE SUN IS IN FULL VIEW")
        print("CHARGE EFFICIENCY: " + "[?]", end="")
        for x in range(30):
            efficiency = random.uniform(90.999, 110.999, )
            print("\rCHARGE EFFICIENCY: %" + str(format(efficiency, ".2f")),
                  end="")
            time.sleep(0.1)
        compute_f("\nNOTHING MORE TO REPORT.")
    return event  # Allows the value of event to be tracked by game()


def direction_check(rotation):
    """
    This tells the user where the rover is looking also is used in the
    direction you move when you go foward.
    :param rotation: Need tell the direction your are facing (direction =
    rotation)
    :return: returns direction to allow game() to say the direction your facing
    """
    if rotation == 1:
        direction = "NORTH"
        return direction
    elif rotation == 2:
        direction = "EAST"
        return direction
    elif rotation == 3:
        direction = "SOUTH"
        return direction
    elif rotation == 4:
        direction = "WEST"
        return direction


def game(values):  # movement to other locations after. (ALSO ESSENTIALLY THE
    """
    This is the main game code, a lot happens here.
    :param values: Read Below (List)
    """
    # MAIN GAME CODE)
    # -----------LIST GUIDE----------------------------------------------------
    # The variables under values[x] are not constants.
    # TURNS = values[0], ROTATION = values[1], CHARGE = values[2],
    # BATTERY = values[3], LOCAL_ROVER = values[4], LOCAL_SHIP = values[5],
    # FATE_ROVER = values[6], FATE_NUMBER_ROVER = values[7],
    # FATE_SHIP = values[8], FATE_NUMBER_SHIP = values[9],
    # ROTATION_CHARGE = values[10], EVENT_NUMBER = values[11] INI = values[12]
    # CHARGE_COOLDOWN = values[13], WINS = values[14]
    # REMEMBER LISTS START WITH 0!
    # -----------REMEMBER------------------------------------------------------
    # LIST WILL HAVE TO BE BROUGHT THROUGH EVERY CALL THAT LEAVES THE
    # 'ORIGINAL' game(values) behind (Think stacks), if this is not done
    # values will not stick, and will cause errors. Return is only required
    # if the value needs to return a value, if it just displays prints
    # nothing is needed.
    # I AM SORRY FOR HOW HARD IT IS TO FOLLOW DUE TO THE USE OF LISTS :(
    # ------------GAME---------------------------------------------------------
    # SHOWS TYPE ERROR: NONE-TYPE WHEN RECALLED
    while values[4] != values[5]:
        if values[13] < 4:
            values[13] += 1
        if values[12] == 1:  # Calls initial location
            location_Rover_ini(values[4])
            print(values[5])
            values[12] += -1
        if values[2] <= 0:  # If charge is less than (somehow) or equal to 0
            # the game will be over.
            game_over(values)
        print("")
        direction = direction_check(values[1])
        values[0] += 1  # Code generates a Turn counter to show how long the
        # run has been.
        print("Turn " + str(values[0]))
        print("")
        if values[2] <= 5 and values[2] >= 1:
            compute_f("[WARNING] NEARING INSUFFICIENT POWER. PLEASE CHARGE "
                      "SOON.")
        else:
            compute_f("POWER LEVELS NOMINAL.")
        compute_f("REMAINING POWER: " + str(values[2]) + "/" + str(values[3]))
        compute_f("WE ARE FACING: " + direction + ".")
        print("")
        if values[13] == 4:
            compute_f("SOLAR PANELS PRIMED. CHARGE IS AVAILABLE.")
        elif values[13] < 0:
            compute_f("SOLAR PANELS DANGEROUSLY HOT. EMERGENCY HEAT SINK IN "
                      "PROGRESS")
        else:
            compute_f("SOLAR PANELS OVERHEATED. COOLING STILL IN PROGRESS.")
        play = True
        while play:
            action = str.lower(input("\nWHAT NOW OPERATOR?"))
            # CHARGE-----------------------------------------------------------
            if action == "charge":  # Charge is what keeps you alive, this does
                # not take a charge to use.
                if values[13] == 4:
                    if not values[2] + 2 >= values[3]:  # The Rover has a
                        # max power
                        if values[11] > 0 and values[11] < 11:
                            values[2] += 1
                            values[13] = 1
                            game(values)
                        if values[11] == 14 or values[11] == 16:
                            values[2] += 4
                            values[13] = 1
                            game(values)  # Ends Turn.
                        elif values[11] >= 27:
                            values[2] += 2
                            values[13] = 1
                            game(values)
                        else:
                            values[2] += 2
                            values[13] = 1
                            game(values)  # Ends Turn. Does not continue code as
                            # it only charges the rover and does not move.
                    else:  # When charge goes over max power or battery (values[
                        # 3]) if forces the values to be the same as battery
                        # total (or its capacity).
                        values[2] = values[3]
                        game(values)  # Wastes a turn.
                else:
                    compute_f("COOLING STILL IN PROGRESS. USING SOLAR PANELS "
                              "NOW COULD DAMAGE SYSTEMS")
                    compute_f("OVERRIDE WARNING?")
                    warning = True
                    while warning:
                        override = str.lower(input("\r[YES/NO]"))
                        if override == 'yes':
                            compute_f("OVERRIDE SUCCESSFUL")
                            if not values[2] + 2 >= values[3]:   # The Rover
                                # has a max power
                                if values[11] == 14 or values[11] == 16:
                                    values[2] += 4
                                    values[3] += random.randrange(-1, -3, -1)
                                    values[13] = 1
                                    game(values)  # Ends Turn.

                                else:
                                    values[2] += 2
                                    values[3] += random.randrange(-1, -3, -1)
                                    values[13] = 1
                                    game(values)
                            else:
                                values[2] = values[3]
                                values[13] = 1
                                game(values)  # Wastes a turn.
                        elif override == 'no':
                            compute_f("OVERRIDE CANCELLED")
                            time.sleep(2)
                            compute_f("WHAT NOW OPERATOR?")




            # ROTATION - Again rotations do not initially take charge it only
            # does if you turn twice.
            elif action == "turn right":
                if values[1] + 1 == 5:
                    values[1] = 1
                    values[10] += 1
                    direction = direction_check(values[1])
                    if values[10] == 2:
                        values[2] += - 1
                        compute_f(
                            "REMAINING POWER: " + str(values[2]) + "/" + str(
                                values[3]))
                        values[10] = 0
                    compute_f("WE ARE NOW FACING: " + direction + ".")
                else:
                    values[1] += 1
                    values[10] += 1
                    direction = direction_check(values[1])
                    if values[10] == 2:
                        values[2] += - 1
                        compute_f(
                            "REMAINING POWER: " + str(values[2]) + "/" + str(
                                values[3]))
                        values[10] = 0
                    compute_f("WE ARE NOW FACING: " + direction + ".")
            elif action == "turn left":
                if values[1] - 1 == 0:
                    values[1] = 4
                    values[10] += 1
                    direction = direction_check(values[1])
                    if values[10] == 2:
                        values[2] += - 1
                        compute_f(
                            "REMAINING POWER: " + str(values[2]) + "/" + str(
                                values[3]))
                        values[10] = 0
                    compute_f("WE ARE NOW FACING: " + direction + ".")
                else:
                    values[1] += - 1
                    values[10] += 1
                    direction = direction_check(values[1])
                    if values[10] == 2:
                        values[2] += - 1
                        compute_f(
                            "REMAINING POWER: " + str(values[2]) + "/" + str(
                                values[3]))
                        values[10] = 0
                    compute_f("WE ARE NOW FACING: " + direction + ".")
            # FORWARD MOVEMENTS - Movements always take chage unless it is
            # caused  by a random event (Which is not implemented yet.)

            elif action == "forward" and values[1] == 2:  # All of the
                # following
                # codes use the forward command but check the 'rover'
                # rotation to give you the correct movements based on
                # alignment. Going East
                if values[4] + 1 == 26 or values[4] + 1 == 6 or values[4] == \
                        11 or values[4] + 1 == 16 or values[4] + 1 == 21:  # To
                    # understand why I have many stops for this is so that you
                    # cannot end up on the left of the array from the  right
                    compute_f("THAT IS NOT POSSIBLE OPERATOR, WE WILL BE "
                              "LEAVING THE MISSION AREA.")
                    time.sleep(1)
                    compute_f("OVERRIDING COMMAND. GIVE ME ANOTHER.")
                else:
                    values[4] += 1
                    values[2] += - 1
                    play = False
            elif action == "forward" and values[1] == 4:  # Going West
                if values[4] - 1 == 0 or values[4] - 1 == 5 or values[4] - 1 \
                        == 10 or values[4] - 1 == 15 or values[4] - 1 == 20:
                    compute_f(
                        "THAT IS NOT POSSIBLE OPERATOR, WE WILL BE LEAVING"
                        " THE MISSION AREA.")
                    time.sleep(1)
                    compute_f("OVERRIDING COMMAND. GIVE ME ANOTHER.")
                else:
                    values[4] += - 1
                    values[2] += - 1
                    play = False
            elif action == "forward" and values[1] == 3:
                if values[4] + 5 >= 26:  # This does not need as many
                    # situations since it cannot go left or right, i only need
                    # to stop it from going down too far.
                    compute_f(
                        "THAT IS NOT POSSIBLE OPERATOR, WE WILL BE LEAVING "
                        "THE "
                        "MISSION AREA.")
                    time.sleep(1)
                    compute_f("OVERRIDING COMMAND. GIVE ME ANOTHER.")
                else:
                    values[4] += 5
                    values[2] += - 1
                    play = False
            elif action == "forward" and values[1] == 1:
                if values[4] - 5 <= 1:
                    compute_f("THAT IS NOT POSSIBLE OPERATOR, WE WILL BE "
                              "LEAVING THE MISSION AREA.")
                    time.sleep(1)
                    compute_f("OVERRIDING COMMAND. GIVE ME ANOTHER.")
                else:
                    values[4] += - 5
                    values[2] += - 1
                    play = False
            elif action == "help":
                compute_f(
                    'AVAILABLE OPERATIONS: \n 1. FORWARD \n 2. CHARGE \n '
                    '3. TURN (Left/Right) \n 4. WHERE (Location)')
            elif action == "where":
                print("")
                location_Rover_ini(values[4])

            else:
                compute_f('THAT IS NOT A VALID OPTION OPERATOR.')

        if values[4] == 1:  # Calls locations (SHOULD RETURN THE LIST UPDATED
            # WITH THE EVENT VALUE (VALUES[11])) CURRENTLY RETURNS NONE
            stats = a1(values)
            game(stats)
        elif values[4] == 2:
            stats = a2(values)
            game(stats)
        elif values[4] == 3:
            stats = a3(values)
            game(stats)
        elif values[4] == 4:
            stats = a4(values)
            game(stats)
        elif values[4] == 5:
            stats = a5(values)
            game(stats)
        elif values[4] == 6:
            stats = b1(values)
            game(stats)
        elif values[4] == 7:
            stats = b2(values)
            game(stats)
        elif values[4] == 8:
            stats = b3(values)
            game(stats)
        elif values[4] == 9:
            stats = b4(values)
            game(stats)
        elif values[4] == 10:
            stats = b5(values)
            game(stats)
        elif values[4] == 11:
            stats = c1(values)
            game(stats)
        elif values[4] == 12:
            stats = c2(values)
            game(stats)
        elif values[4] == 13:
            stats = c3(values)
            game(stats)
        elif values[4] == 14:
            stats = c4(values)
            game(stats)
        elif values[4] == 15:
            stats = c5(values)
            game(stats)
        elif values[4] == 16:
            stats = d1(values)
            game(stats)
        elif values[4] == 17:
            stats = d2(values)
            game(stats)
        elif values[4] == 18:
            stats = d3(values)
            game(stats)
        elif values[4] == 19:
            stats = d4(values)
            game(stats)
        elif values[4] == 20:
            stats = d5(values)
            game(stats)
        elif values[4] == 21:
            stats = e1(values)
            game(stats)
        elif values[4] == 22:
            stats = e2(values)
            game(stats)
        elif values[4] == 23:
            stats = e3(values)
            game(stats)
        elif values[4] == 24:
            stats = e4(values)
            game(stats)
        elif values[4] == 25:
            stats = e5(values)
            game(stats)

    while values[4] == values[5]:  # This marks the game completion. No
        # definition. (As there is only one way to win)
        compute_f("OPERATOR WE HAVE ARRIVED TO THE SHIP. THANK YOU, "
                  "OPERATOR...")
        time.sleep(2)
        comp_s(str.upper(operator) + ", I WILL SEE YOU BACK ON EARTH")
        calculating()  # DONT LISTEN TO THE ERROR IT IS THERE
        human_("Mission complete. We have confirmed the arrival and  "
               "reattachment of the Rover.")
        human_("Good job Operator.")
        with open("save.txt", "r") as save:
            info = save.readlines()  # Takes out information from save
            print('NAME DEFINED. SAVING...')
            info[0] = "1\n"  # \n is required for multi line saves!
            info[1] = str.lower(operator + "\n")
            info[2] = '1\n'
            wins = info[0]
        with open("save.txt", 'w') as save:
            save.writelines(info)  # Updates the file
            time.sleep(2)
        main_menu2(wins)  # DON'T LISTEN TO THE ERROR IT IS THERE IN THE
        # ORIGINAL CODE

    # ADD A RANDOM DIALOG DEFINITION FOR ALL THE LOCATIONS
    #
    #
    # IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT
    # MOVE THE DEFINITION BEHIND THEIR CALL OR THEY WILL NOT WORK AS INTENDED
    #
    #

with open("save.txt", "r") as save:
    info = save.read().splitlines()
    played = info[2]
    if int(info[2]) == 1:
        print("WELL COME BACK " + str.upper(info[1]) + ".")
        operator = str.upper(info[1])
        completion = info[0]
        save.close()
        print("")
        calculating()
        time.sleep(1)
        compute_f('RUNNING SYSTEMS DIAGNOSTICS. PLEASE WAIT...')
        time.sleep(2)
        diagnostics()  # Hops up to the diagnostics definition
        main_menu1(completion)  # Hops up to the main menu definition
    elif int(info[2]) == 0:
        print('W', end='')  # All these print statements are shortened to the
        # function comp_(fast [f],super fast [sf],and slow [s]) and human_.
        time.sleep(.0125)  # Refer to human_ (First couple lines) for more
        # information on the general creation of the code and its functions.
        print('E', end='')
        time.sleep(.0125)
        print('L', end='')
        time.sleep(.0125)
        print('C', end='')
        time.sleep(.0125)
        print('O', end='')
        time.sleep(.0125)
        print('M', end='')
        time.sleep(.0125)
        print('E', end='')
        time.sleep(.0125)
        print(' ', end='')
        time.sleep(.0125)
        print('O', end='')
        time.sleep(.0125)
        print('P', end='')
        time.sleep(.0125)
        print('E', end='')
        time.sleep(.0125)
        print('R', end='')
        time.sleep(.0125)
        print('A', end='')
        time.sleep(.0125)
        print('T', end='')
        time.sleep(.0125)
        print('O', end='')
        time.sleep(.0125)
        print('R')
        time.sleep(.0125)
        time.sleep(1)
        compute_f('DEFINE NAME OF OPERATOR: ')
        operator = input()
        with open("save.txt", "r") as save:
            info = save.readlines()  # Takes out information from save
            print('NAME DEFINED. SAVING...')
            info[0] = "0\n"  # \n is required for multi line saves!
            info[1] = str.lower(operator + "\n")
            info[2] = '1\n'
            completion = info[0]
        with open("save.txt", 'w') as save:
            save.writelines(info)  # Updates the file
            time.sleep(2)
        print("")
        calculating()  # Hops up to the calculating definition
        compute_f('HELLO ' + str.upper(operator) + '.')
        time.sleep(1)
        compute_f('RUNNING SYSTEMS DIAGNOSTICS. PLEASE WAIT...')
        time.sleep(2)
        diagnostics()  # Hops up to the diagnostics definition
        main_menu1(completion)  # Hops up to the main menu definition