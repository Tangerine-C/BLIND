# Info (PLEASE USE FULLSCREEN WHEN VIEWING THIS CODE)
# This project was made by Matthew J. Martinez in part of a Integration Project
# of the COP 1500 course of Florida Gulf Coast University.
# Blind is a text-based game where you are a rover operator controlling a rover
# to safety back to it's ship before it is destroyed or runs out of power.
# NOTE: This version will mainly be a main menu and opening secion test code
# (and a test mini game).
# Append: There would be more color to the prints but sadly ANSI Escape Code is
# not supported any longer by the current versions of python past 3.6
# CITATIONS -    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
# Assistance for code from
# ThinkWithPython2 (PDF)
# https://www.geeksforgeeks.org/isupper-islower-upper-python-applications/
# (FOR EXPLAINATION OF TOPIC)
# https://www.geeksforgeeks.org/sleep-in-python/
# (FOR EXPLAINATION OF TOPIC)
# https://appdividend.com/2022/07/14/how-to-stop-python-script-from-execution/#
# :~:text=To%20stop%20a%20python%20script,terminate%20Python%20script%20executi
# on%20programmatically.
# Above for exit() (Which closes, or kills, python's running code immediately)
# https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
# The above was used in the def print_ and was not using the main topic but the
# responses to the topic to create a emulated human typing text then edited it
# to work with non random variables (fixed). The following links helped explain
# sys.stdout, sys.stdout.write() and sys.stdout.flush() in better detail.
# https://www.geeksforgeeks.org/python-sys-stdout-flush/#:~:text=because%20call
# ing%20sys.-,stdout.,of%20the%20Python%20runtime%20environment.
# https://www.geeksforgeeks.org/sys-stdout-write-in-python/#:~:text=to%20the%20
# screen.-,sys.,Unlike%20print%2C%20sys.

# IMPORTS -  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
import time, sys, \
    random  # SYS denotes tweaks done to the python algorithm. Time allows time
# .sleep to work and allows pauses in the algorithm. Random allow random values
# to be allocated.


# DEFINITIONS (MOST)   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
# def value_Check():  # Initialization for the values below done at the start of
#     # the code for the game.
#     rotation = random.randrange(1, 5, 1)
#     charge = 10  # Essentially the health stat for the rover once this hits
#     # zero its is game over.(There is only a few other non battery game overs.)
#     fate_Rover = 0  #Fate is a stat that will determine if you instanly
#     # recieve a game over from a Major Event. It is calculated within the
#     # events. (1 - 100)
#     fate_Number1 = random.randrange(1, 100,1)
#     #This is the number that will cause fate to cause a game over to occur, it
#     #will be random every game start.)
#     while fate_Rover == fate_Number1:
#         fate_Number1 = random.randrange(1, 100, 1)
#     fate_Ship = 0
#     fate_Number2 = randome.randrange(1, 100, 1)
#     while fate_Ship == fate_Number2:
#         fate_Number2 = random.randrange(1, 100, 1)
#     battery = 20  # Battery is what the maximum amount of energy that can be
#     # held at a time, can be reduced through events, you can not gain more.
#     local_Rover = random.randrange(1, 26, 1)  # This is to generate a random
#     # value between 1 and 25 to allow a random spawn for the rover(you)
#     local_Ship = random.randrange(1, 26, 1)  # This is to generate a random
#     # value between 1 and 25 to allow a random spawn for the ship(objective)
#     while local_Rover == local_Ship or local_Rover == local_Ship - 1 or \
#           local_Rover == local_Ship + 1 or local_Rover == local_Ship + 5 \
#           or local_Rover == local_Ship - 5:
#         local_Ship = random.randrange(1, 26, 1)  # This makes sure that the
#         # rover and the ship do not spawn(or have the same value) on each
#         # other (or near) ending the game instantly/quickly.
#     ini_Values = [fate_Rover,fate_Number1,fate_Ship,fate_Number2,
#                   local_Rover,local_Ship]
#   return ini_Values

typing_speed = 120  # Required for human_(phrase)'s random time algorithm.
#Not a problem as a global never used for anything else


def human_(phrase):  # This simulates human typing in code when ever text is
    # printed. SOURCE: MODIFIED OFF BILL GROSS of stackoverflow.com
    # disscussion linked in citations.
    for anything in phrase:  # This essentially states that for every
        # anything (STRING) found in phrase (or between the parenthesis) it
        # will use the following code
        sys.stdout.write(anything)  # This states that for every letter it
        # will write (similar to print) it out but does not create a new
        # line  for sub-sequential sys.stdout.write()s. (BUFFERED)
        sys.stdout.flush()  # Every letter that would usually be left in the
        # 'buffer' it will be 'flushed' into the terminal (or outputed)
        # consecutively instead of all at once.
        time.sleep(random.random() * 10.0 / typing_speed)  # Use of random
        # in action. Time between each letter will be randomized along to
        # create a psudo-human typing algoritm.
    print('')  # This moves to next line after the completion of the phrase
    # within the function. (print_, think_f,think_sf, and think_s all work
    # under similar principles.)


def comp_f(phrase):  # This simulates computer [shortened to comp] (i.e. fast,
                  # perfect) typing and is a non-random variant of human_.
    for anything in phrase:
        sys.stdout.write(anything)
        sys.stdout.flush()
        time.sleep(.0125)
    print('')


def comp_sf(phrase):  # _sf denotes Super Fast. Faster of comp_f.
    for anything in phrase:
        sys.stdout.write(anything)
        sys.stdout.flush()
        time.sleep(.00125)
    print('')


def comp_s(phrase):  # _s denotes Slow. Slower variant of comp_f.
    for anything in phrase:
        sys.stdout.write(anything)
        sys.stdout.flush()
        time.sleep(.25)
    print('')


def calculating():  # Just a viusal device nothing more.
    comp_f('.')
    time.sleep(0.75)
    comp_f('..')
    time.sleep(0.75)
    comp_f('...')
    time.sleep(0.75)


def check_1():  # Part of the Game introduction (part 1). Essentially goes
    # from 1% to 93% then stops.
    system = 1
    while system < 94:
        print(str(system) + '%')
        system += 1
        time.sleep(0.0125)
    comp_f('SYSTEM ERROR: CAMERA SYSTEMS OBTAINING INSUFFICIENT VOLTAGE')
    time.sleep(2)
    comp_f('EVALUATING DAMAGE...')
    time.sleep(3)


def check_2():  # Part of Game introduction (Part 2) Essentially goes from
    # 1% to 100% then stops.
    evaluate = 1
    while evaluate < 101:  # Its not 100 because of < does not allow it to
        # get to 100 but using 101 stops at 100 instead of 99 I
        # alternatively  could use "while evaluate <= 100".
        print(str(evaluate) + '%')
        evaluate += 1
        time.sleep(0.0125)
    comp_f(
        'SEVERED CONNECTION TO VISUALS; CAUSE LOW VOLTAGE, MISSING POWER '
        'CORD.  VERDICT: WE ARE BLIND...')
    time.sleep(.5)


def diagnostics():
    comp_f('CHECKING MAIN SYSTEMS...')
    time.sleep(3)
    check_1()
    time.sleep(1)
    check_2()


def logo_ini():  # The first appearence of the title logo (slow)
    comp_sf(
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
        '░')  # Use of Alt codes to generate computer pre-assigned graphics.
    comp_sf(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓░░░░░░▓▓▓▓▓▓▓░░▓▓▓▓▓░░░░░▓▓▓░░▓▓▓▓▓▓▓▓▓░░░░░░░'
        '░')  # Alt codes used are Alt + 176 and Alt + 179 respectively.
    comp_sf(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓▓▓▓░░░░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░')  # To those wanting to use these hold down the Alt key and type
    #  the numbers then release alt
    comp_sf(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░▓▓▓░░░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░')  # Number Pad is required, make sure to have Num Lock on.
    comp_sf(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░▓▓▓░░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░')
    comp_sf(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░░▓▓▓░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░')
    comp_sf(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░░░▓▓▓▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░')
    comp_sf(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓░░▓▓▓▓▓▓▓░░▓▓▓░░░░░▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓░░░░░░░'
        '░')
    comp_sf(
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
        '░')


def logo_comp():  # Completion of the game will show a star
    comp_sf(
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
        '░░░░▓▓░░░░░░░░░')  # Use of Alt codes to generate computer
                            # pre-assigned graphics.
    comp_sf(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓░░░░░░▓▓▓▓▓▓▓░░▓▓▓▓▓░░░░░▓▓▓░░▓▓▓▓▓▓▓▓▓░░░░░░░░'
        '░░░▓▓▓▓░░░░░░░░')  # Alt codes used are Alt + 176 and Alt + 179
                           # respectively.
    comp_sf('░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓▓▓▓░░░░▓▓▓░░▓▓▓░░░░░▓▓▓░░'
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░')  # To those wanting to use these hold down
                                   # the Alt key and type the numbers then
                                   # release alt
    comp_sf(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░▓▓▓░░░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░▓▓'
        '▓▓▓▓▓▓▓▓▓▓▓▓░░░')  # Number Pad is required, make sure to have Num
                           # Lock on.
    comp_sf(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░▓▓▓░░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░░'
        '▓▓▓▓▓▓▓▓▓▓░░░░░')
    comp_sf(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░░▓▓▓░▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░░'
        '░▓▓▓▓▓▓▓▓░░░░░░')
    comp_sf(
        '░░░░░░▓▓▓░░░░░▓▓▓░░▓▓▓░░░░░░░░▓▓▓░░░░▓▓▓░░░░▓▓▓▓▓▓░░▓▓▓░░░░░▓▓▓░░░░░'
        '░▓▓▓▓▓▓▓▓▓▓░░░░░')
    comp_sf(
        '░░░░░░▓▓▓▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓░░▓▓▓▓▓▓▓░░▓▓▓░░░░░▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓░░░░░░░▓'
        '▓▓▓▓░░▓▓▓▓▓░░░░')
    comp_sf(
        '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓'
        '▓░░░░░░░░▓▓▓░░░')


def logo_re():  # The other appearences of the title logo (fast)
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


def main_menu1():  # Main menu for game
    if completion == 0:
        logo_ini()
    if completion == 1:
        logo_comp()
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
    print('Type test, for python math test.')
    while True:  # This is the Directory for the main menu, input tell the
        # code where you want to go.
        state = str.lower(input())
        if state == 'start':
            start()
        elif state == '?':
            explain_menu()
        elif state == 'credit':
            credit()
        elif state == 'end':
            end()
        elif state == 'test':
            test()
        elif state == '0/0':  # For Reference causes Memory Error will not
            # show  in later versions but I will keep because its funny.
            print("?" * 100 ** 9)
        else:
            print('')
            human_('That is not a choice Operator ' + str.capitalize(
                operator) + ".")


def main_menu2():  # The only difference between this and the menu above is
    # that it loads the logo faster using loge_re(use) instead of  logo_ini(
    # tial)
    logo_re()
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
            start()
        elif state == '?':
            explain_menu()
        elif state == 'credit':
            credit()
        elif state == 'end':
            end()
        elif state == 'test':
            test()
        elif state == '0/0':  # For Reference causes Memory Error will not show
            # in later versions but I will keep because its funny.
            print("?" * 100 ** 9)
        else:
            print('')
            human_('That is not a choice ' + str.capitalize(operator) + ".")


def test():
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
    back()


def end():
    print(' ')
    print(' ')
    comp_s('GOING INTO REST MODE...\n GOODNIGHT, ' + str.upper(operator))
    time.sleep(1)
    exit()


def credit():
    print(' ')
    print(' ')
    comp_f('Credits')
    time.sleep(2)
    comp_f(
        'Blind is made by Matthew J. Martinez, Undergraduate (at time of'
        ' creation) at Florida Gulf Coast University.')
    back()


def back():
    time.sleep(2)
    print(' ')
    comp_f('Return? (y/n)')
    while True:
        state = str.lower(input())
        if state == 'y':
            print(' ')
            print(' ')
            main_menu2()
        if state == 'n':
            comp_s('Okay...')
            comp_s('.')
            time.sleep(2)
            comp_s('..')
            time.sleep(2)
            comp_s('...')
            time.sleep(1)
            print(' ')
            comp_f('Now do you want to return? (y/n)')


def start():
    print(' ')
    print(' ')
    game_main()


def explain_menu():  # Explains concepts about the game (this is accessed
    # through menu). REVISIONS PROBABLE
    print(' ')
    print(' ')
    human_('This is Mission Control.')
    human_('You are instructed to bring back a T.E.R.R.A rover from')
    human_(
        'PSR J1719-14 C, a comet on the far end of the Serpens Cauda'
        ' constellation')
    human_(
        "as the carbon based crystal on the planet's surface are required"
        " for research.")
    human_(
        'Shortly after landing, the rover was ejected pre-maturely and needs'
        ' to return')
    human_(
        'before the rover runs out of power. The planet is more stable than'
        ' it was 700')
    human_('ago so it should not be as bad to navigate.')
    print(' ')
    human_(
        'The rover is able to move and has feature to assist in its retreval.')
    human_(
        'Solar power is available at times due to the rapid nature of the'
        ' planet.')
    human_('The command charge can recover some power.')
    human_('The command forward allows movement ahead.')
    human_('The command turn left/right allow rotation.')
    human_('Parts of the rover can be damaged. Do not allow this to occur.')
    human_(
        'Damaged parts make certain actions more difficult, like taking'
        ' more energy.')
    human_('This is the end of the explaination.')
    back()


def explain_game():  # Explains concepts about the game (this is accessed
    # through the game start if you did not read it and want to view).
    # REVISIONS PROBABLE
    print(' ')
    print(' ')
    human_('As you should know, this is Mission Control.')
    human_(
        "You are instructed to bring back a T.E.R.R.A rover as it's"
        " operator from")
    human_(
        'PSR J1719-14 C, a comet on the far end of the Serpens Cauda'
        ' constellation')
    human_(
        "as the carbon based crystal on the comet's surface are required"
        " for research.")
    human_(
        'Shortly after landing, the rover was ejected pre-maturely and needs'
        ' to return')
    human_(
        'before the rover runs out of power. The planet is more stable than'
        ' it was 700')
    human_('ago so it should not be as bad to navigate.')
    print(' ')
    human_(
        'The rover is able to move and has feature to assist in its retreval.')
    human_(
        'Solar power is available at times due to the rapid nature of the'
        ' comet.')
    human_('The command charge can recover some power.')
    human_('The command forward allows movement ahead.')
    human_('The command turn left/right allow rotation.')
    human_('Parts of the rover can be damaged. Do not allow this to occur.')
    human_(
        'Damaged parts make certain actions more difficult, like taking more'
        ' energy.')
    human_('This is the end of the explaination.')
    print(' ')
    human_('Do you understand? (y/n)')
    while True:
        understand = input()
        if understand == str.lower('y'):
            break
        if understand == str.lower('n'):
            print('')
            human_('Then read it again.')


def game_main():
    human_('Welcome Operator ' + str.capitalize(
        operator) + ' we will procede to the mission phase.')
    human_('We assume you have been debriefed on the mission. You have right?')
    knowledge = input('(y/n)')
    while True:
        if knowledge == str.lower('y'):
            break
        if knowledge == str.lower('n'):
            explain_game()
            break
    print('')
    print('')
    human_('We will now relay information on the rover to you.')
    human_('Patching...')
    calculating()
    comp_f('HELLO OPERATOR')
    time.sleep(1)
    comp_f('CURRENT TEMPERATURE IS 300 DEGREES CELCIUS.')
    time.sleep(1)
    comp_f('CURRENT PHYSICAL STATE... FINE.')
    time.sleep(1)
    comp_f(
        'CURRENT SYSTEMS ARE 93% OPERATIONAL. VISUAL OPTICS ARE NOT '
        'FUNCTIONING. AUTO-PILOT MODULES ARE UNRESPONSIVE.')
    time.sleep(1)
    comp_f(
        'WE WILL HAVE TO RELY ON SURFACE SCAN EQUIPMENT TO VISUALIZE OUR '
        'LOCATION AND I WILL RELY ON YOUR CONTROL.')
    calculating()
    comp_f('I WILL BE IN YOUR CARE OPERATOR, PLEASE KEEP ME WELL.')
    print('')
    print('')
    time.sleep(1)
    human_('Mission Control here, we have given you manual control.')
    human_('From here on out it will be just you and your rover.')
    human_(
        'Make sure to use a scan to know where your rover is initially to'
        ' know how to make your next move.')
    human_('Good luck Operator.')
    print('')
    print('')
    print('End of Code')
    print("The 'Game' part of the code still needs much work, so this is as "
          "far as the code will function fully without having errors")

def game_over():
    human_(
        "Connection with the rover has been lost. All reconnection attempts"
        " have failed.")
    human_(
        "This mission is a failure. Report to the staging room for"
        " debriefing.")
    print('')
    print('')
    menu_game1


def repair_1():  # Part of Game introduction (Part 2) Essentially goes from
    # 1% to 100% then stops.
    evaluate = 1
    while evaluate < 101:  # Its not 100 because of < does not allow it to
        # get to 100 but using 101 stops at 100 instead of 99 I
        # alternatively could use "while evaluate <= 100".
        print(str(evaluate) + '%')
        evaluate = evaluate + 1
        time.sleep(0.0125)
    comp_f('POWER SYSTEMS RESTORED.')
    comp_f('THE ENERGY SPIKE CAUSED HEAVY ENERGY LOSS WITHIN OUR BATTERY.')
    time.sleep(.5)


# AREA CODES (A1 - E5) This is for all areas in game and their discriptions  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
# This will probably be the longest sets of code in the entire code batch.
# A LOT of If Then statements most likely as it will have to track what can
# go  where from the neighboring areas.
# i.e. if you go foward facing south at A1 you will go to A2, east will lead
# to B1, North & West will waste power and return you to A1.
# It will probably be done at first with A1 to C3 (i.e 3 x 3) to test code
# then the additional spaces will be included.
# This section will be managed a range of 1 - 25 meaning every area will  be
# given a value.
#   1   2   3   4   5       On the left is what I will call the 'array' in
#   6   7   8   9   10      which is the principle movement system of the
#   11  12  13  14  15      game  and how I will be able
#   16  17  18  19  20      principle movement system of the game and how  I
#   20  22  23  24  25      will be able to create and simplifiy the code
# for  this segment so it will not be completely redundently inefficent by
# using  a movement system such as moving "Down" or  foward looking from A1
# (1) to B1 (6) it will add 5 to the a 'location' value and going from  A1 (
# 1)  to A2 (2) it will simply add 1. When going to values above this still
# may be foward, it will subtract values of 1 when going left and 5 when
# going up the array. The definitions below are going to be all called by a
# long if/elif statement. If this is not enough work for me this may be
# expanded  to a 10 x 10 array instead of a 5 x 5 array.Rotations will be
# tracked with a number of 1 through 4. 1 being North, 2 East, 3 South, and 4
#           N               West as shown by the compass on the left.
#           1
#       W4     2E
#           3
#           S
def location_Rover_ini():  # Gives the Rover its initial location. Does not
    # need to track rotation as you will just be there and not being moving
    # into it.
    if local_Rover == 1:
        A1()
    elif local_Rover == 2:
        A2()
    elif local_Rover == 3:
        A3()
    elif local_Rover == 4:
        A4()
    elif local_Rover == 5:
        A5()
    elif local_Rover == 6:
        B1()
    elif local_Rover == 7:
        B2()
    elif local_Rover == 8:
        B3()
    elif local_Rover == 9:
        B4()
    elif local_Rover == 10:
        B5()
    elif local_Rover == 11:
        C1()
    elif local_Rover == 12:
        C2()
    elif local_Rover == 13:
        C3()
    elif local_Rover == 14:
        C4()
    elif local_Rover == 15:
        C5()
    elif local_Rover == 16:
        D1()
    elif local_Rover == 17:
        D2()
    elif local_Rover == 18:
        D3()
    elif local_Rover == 19:
        D4()
    elif local_Rover == 20:
        D5()
    elif local_Rover == 21:
        E1()
    elif local_Rover == 22:
        E2()
    elif local_Rover == 23:
        E3()
    elif local_Rover == 24:
        E4()
    elif local_Rover == 25:
        E5()


# def location_Ship_ini():  # Gives the Ship its initial location. Does not
#     # need  to track rotation as you will just be there and not being moving
#     # into it. PROBABLY DO NOT NEED THIS CODE.
#     if local_Ship == 1:
#         A1()
#     elif local_Ship == 2:
#         A2()
#     elif local_Ship == 3:
#         A3()
#     elif local_Ship == 4:
#         A4()
#     elif local_Ship == 5:
#         A5()
#     elif local_Ship == 6:
#         B1()
#     elif local_Ship == 7:
#         B2()
#     elif local_Ship == 8:
#         B3()
#     elif local_Ship == 9:
#         B4()
#     elif local_Ship == 10:
#         B5()
#     elif local_Ship == 11:
#         C1()
#     elif local_Ship == 12:
#         C2()
#     elif local_Ship == 13:
#         C3()
#     elif local_Ship == 14:
#         C4()
#     elif local_Ship == 15:
#         C5()
#     elif local_Ship == 16:
#         D1()
#     elif local_Ship == 17:
#         D2()
#     elif local_Ship == 18:
#         D3()
#     elif local_Ship == 19:
#         D4()
#     elif local_Ship == 20:
#         D5()
#     elif local_Ship == 21:
#         E1()
#     elif local_Ship == 22:
#         E2()
#     elif local_Ship == 23:
#         E3()
#     elif local_Ship == 24:
#         E4()
#     elif local_Ship == 25:
#         E5()
#

def direction_check():
    if rotation == 1:  # This set of if/elif statements prepares the code to
        #  tell you the direction you are looking.
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


def game():  # movement to other locations after. (ALSO ESSENTIALLY THE
    # MAIN GAME CODE)
    if ini == 0: #generates your location data and the direction you are
        # facing along with general stats that will affect gameplay.
        rotation = random.randrange(1, 5, 1)
        charge = 10  # Essentially the health stat for the rover once this hits
        # zero its is game over.(There is only a few other non battery game
        # overs.)
        rot_charge = 0 #This value is when you lose a single charge after 2
        # rotation uses (just so you dont lose power extremely quickly).
        fate_Rover = 0  # Fate is a stat that will determine if you instantly
        # receive a game over from a Major Event. It is calculated within the
        # events. (1 - 100)
        fate_Number1 = random.randrange(1, 100, 1)
        # This is the number that will cause fate to cause a game over to
        # occur, it will be random every game start.
        fate_Ship = 0
        fate_Number2 = randome.randrange(1, 100, 1)
        battery = 20  # Battery is what the maximum amount of energy that can be
        # held at a time, can be reduced through events, you can not gain more.
        local_Rover = random.randrange(1, 26, 1)  # This is to generate a
        # random
        # value between 1 and 25 to allow a random spawn for the rover(you)
        local_Ship = random.randrange(1, 26, 1)  # This is to generate a random
        # value between 1 and 25 to allow a random spawn for the ship(objective)
        while local_Rover == local_Ship or local_Rover == local_Ship - 1 or \
            local_Rover == local_Ship + 1 or local_Rover == local_Ship + 5 \
            or local_Rover == local_Ship - 5:
            local_Ship = random.randrange(1, 26, 1)  # This makes sure that the
            # rover and the ship do not spawn(or have the same value) on each
            # other (or near) ending the game instantly/quickly.
        location_Rover_ini() #Gives starting location
        event_Value == 0
    #Game ---------------------------------------------------------------------
    while local_Rover != local_Ship:
        if charge <= 0:  # If charge is less than (somehow) or equal to 0
            # the game will be over.
            game_over()
        print("")
        direction_check()
        turn = 0
        turn += 1  # Code generates a Turn counter to show how long the run
        # has been.
        print("Turn " + str(turn))
        print("")
        if charge <= 5 and charge >= 1:
            comp_f("[WARNING] NEARING INSUFFICIENT POWER. PLEASE CHARGE SOON.")
        else:
            comp_f("POWER LEVELS NOMINAL.")
        comp_f("REMAINING POWER: " + str(charge) + "/" + str(battery))
        comp_f("WE ARE FACING: " + direction + ".")
        print("")
        print("")
        if rot_charge == 2:  # Every two rotations (or turn left or right
            # commands) will drain power.
            charge += -1
        action = str.lower(input("WHAT NOW OPERATOR?"))


        # CHARGE --------------------------------------------------------------
        if action == "charge":  # Charge is what keeps you alive, this does
            # not take a charge to use.
            if event == 14 or event == 16:
                charge += 4
            else:
                charge += 2
            if charge >= battery + 1:  # The Rover has a max power of 20
                # initially.
                charge == 20
                game() #Wastes a turn.
            else:
                game()


        # ROTATION - Again rotations do not initially take charge it only
        # does if you turn twice.
        if action == "turn right":
            if rotation + 1 == 5:
                rotation = 1
                rot_charge += 1
                direction_check()
                comp_f("WE ARE NOW FACING: " + direction + ".")
            else:
                rotation += 1
                rot_charge += 1
                direction_check()
                comp_f("WE ARE NOW FACING: " + direction + ".")
        if action == "turn left":
            if rotation - 1 == 0:
                rotation == 4
                rot_charge += 1
                direction_check()
                comp_f("WE ARE NOW FACING: " + direction + ".")
            else:
                rotation += - 1
                rot_charge += 1
                direction_check()
                comp_f("WE ARE NOW FACING: " + direction + ".")
        # FORWARD MOVEMENTS - Movements always take chage unless it is
        # caused  by a random event (Which is not implemented yet.)


        if action == "foward" and rotation == 2:  # All of the following
            # codes use the foward command but check the 'rover' rotation
            # to give you the correct movements based on alignment,
            if local_Rover + 1 == 26:
                comp_f(
                    "THAT IS NOT POSSIBLE OPERATOR, WE WILL BE LEAVING THE "
                    "MISSION AREA.")
                time.sleep(1)
                comp_f("OVERRIDDING COMMAND. GIVE ME ANOTHER.")
            else:
                local_Rover = local_Rover + 1
                power = power - 1
        if action == "foward" and rotation == 4:
            if local_Rover - 1 == 0:
                comp_f(
                    "THAT IS NOT POSSIBLE OPERATOR, WE WILL BE LEAVING THE "
                    "MISSION AREA.")
                time.sleep(1)
                comp_f("OVERRIDDING COMMAND. GIVE ME ANOTHER.")
            else:
                local_Rover = local_Rover - 1
                power = power - 1
        if action == "foward" and rotation == 3:
            if local_Rover + 5 >= 26:
                comp_f(
                    "THAT IS NOT POSSIBLE OPERATOR, WE WILL BE LEAVING THE "
                    "MISSION AREA.")
                time.sleep(1)
                comp_f("OVERRIDDING COMMAND. GIVE ME ANOTHER.")
            else:
                local_Rover = local_Rover + 5
                power = power - 1
        if action == "foward" and rotation == 1:
            if local_Rover - 5 <= 1:
                comp_f(
                    "THAT IS NOT POSSIBLE OPERATOR, WE WILL BE LEAVING THE "
                    "MISSION AREA.")
                time.sleep(1)
                comp_f("OVERRIDDING COMMAND. GIVE ME ANOTHER.")
            else:
                local_Rover = local_Rover - 5
                power = power - 1
    while local_Rover == local_Ship:  # This marks the game completion. No
        # definition. (As there is only one way to win)
        comp_f("OPERATOR WE HAVE ARRIVED TO THE SHIP. THANK YOU, OPERATOR...")
        time.sleep(2)
        comp_s(str.upper(operator) + ", I WILL SEE YOU BACK ON EARTH")
        calculating()
        human_(
            "Mission complete. We have confirmed the arrival and reattachment"
            " of the Rover.")
        human_("Good job Operator.")
        completion = open("save.txt", "w")
        wins = int(completion.readline())
        wins += 1
        completion.write(str(wins))
        completion.close()


        main_menu1
    if local_Rover == 1:  # LOWERCASE ALL OF THE DEFINITIONS/VARIABLES (CAUSE
        # OF RED ERRORS
        A1()
        game()
    elif local_Rover == 2:
        A2()
        game()
    elif local_Rover == 3:
        A3()
        game()
    elif local_Rover == 4:
        A4()
        game()
    elif local_Rover == 5:
        A5()
        game()
    elif local_Rover == 6:
        B1()
        game()
    elif local_Rover == 7:
        B2()
        game()
    elif local_Rover == 8:
        B3()
        game()
    elif local_Rover == 9:
        B4()
        game()
    elif local_Rover == 10:
        B5()
        game()
    elif local_Rover == 11:
        C1()
        game()
    elif local_Rover == 12:
        C2()
        game()
    elif local_Rover == 13:
        C3()
        game()
    elif local_Rover == 14:
        C4()
        game()
    elif local_Rover == 15:
        C5()
        game()
    elif local_Rover == 16:
        D1()
        game()
    elif local_Rover == 17:
        D2()
        game()
    elif local_Rover == 18:
        D3()
        game()
    elif local_Rover == 19:
        D4()
        game()
    elif local_Rover == 20:
        D5()
        game()
    elif local_Rover == 21:
        E1()
        game()
    elif local_Rover == 22:
        E2()
        game()
    elif local_Rover == 23:
        E3()
        game()
    elif local_Rover == 24:
        E4()
        game()
    elif local_Rover == 25:
        E5()
        game()


def event_trigger():  # This set of code generates a value and presents a
    # situation based off the random value generated (within a range).
    event = random.randrange(0, 26, 1)
    if event >= 0 and event <= 10:
        comp_f("NOTHING MORE TO REPORT.")
    elif event >= 11 and event <= 13:
        comp_f("LARGE UNKNOWN ENERGY SPIKE, NO COUNTER MEASURES PREPARED")
        comp_f("POW9r inSTaBIlITY D-23cTED")
        print("r"*20)
        comp_f("rESe7ING Br3AKER")
        repair_1()
        charge += -5
    elif event == 14 or event == 16:
        comp_f("SPIKE IN AVAILABLE SUNLIGHT DETECTED. OUR SOLAR CHARGING "
               "WILL BE MORE EFFECTIVE.")
        comp_f("WE DODGED A SOLAR FLARE")
    elif event == 15:  # MAJOR EVENT: SOLAR FLARE | The more rarer harsher
        # events, can end the game by itself.
        comp_f(
            '[WARNING] MAJOR SPIKE IN AVAILABLE SUNLIGHT DETECTED.'
            ' TEMPERATURES RISING TO UNSUITABLE LEVELS')
        comp_f('TEMPERTURE OVER 78 DEGREES CELCIUS.')
        comp_f('OVERRIDING OPERATOR CONTROL. DISABLING ALL SYSTEMS NON-'
               'ESSENTIAL'
            ' TO SURVIVAL AND REROUTING ALL POWER TO COOLING SYSTEMS.')
        comp_f('DISABLING CONNECTION')
        human_(
            'We have lost connection with the rover, we are pulling up'
            ' satellite imagery to see the situation.')
        human_("It doesn't look good...")
        comp_sf(
            '▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░░░░░░░▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░░░░░░▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░░░░░░▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░░░░░▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░░░░░▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '░░░▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓░░░▓▓▓░▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
            '▓▓▓▓▓▓▓░▓▓▓░░░▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓░░▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓'
            '▓▓▓▓▓▓▓▓░▓▓▓▓▓░░▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓'
            '▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓'
            '▓▓░▓▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░'
            '▓▓▓░▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓░▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓'
            '░▓▓▓▓░▓▓▓░▓▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓░▓▓▓░▓▓░▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓░▓▓'
            '▓░▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓░▓▓▓░▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓░▓▓░▓'
            '▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓'
            '▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓░▓▓'
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓'
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓'
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓'
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        comp_sf(
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓'
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
        time.sleep(2)
        human_(
            "The sun is in very close proximity to the comet. There will be a"
            " large spike in temperatures.")
        human_(
            "The rover is sturdier then most but it's systems still have a"
            " sensetive melting point, specifically the battery.")
        human_("We will keep checking for connection to the rover, standby.")
        calculating()
        sun_spot = random.randrange(-3, -10, -1)
        charge += sun_spot
        sun_spot_damage = random.randrange(-1, -5, -1)
        battery += sun_spot_damage
        fate_Rover = random.randrange(1, 100, 1)
        if fate_Rover == 42:
            charge == 0  # DEATH
        else:
            comp_f("CONNECTION REESTABLISHED")
            comp_f("REVIEWING DAMAGE")
            if sun_spot <= -6 and sun_spot >= -10:
                comp_(
                    'HIGH ENERGY USAGE REQUIRED FOR OPTIMAL COOLING WE HAVE'
                    ' LOST A LARGE AMOUNT OF ENERGY.')
            elif sun_spot <= -3 and sun_spot >= -5:
                comp_f('OPTIMAL ENEGERY USAGE REQUIRED FOR COOLING.')
                time.sleep(1)
                comp_s('WE GOT LUCKY...')
            if sun_spot_damage >= -5 and sun_spot_damage <= -3:
                comp_f('SUBSTANCIAL DAMAGE RECIEVED TO POWER CORE')
                comp_f(
                    'CURRENTLTY IRREPAIRABLE, OUR ENERGY STORAGE WILL BE'
                    ' MODERATELY REDUCED TO AVOID FURTHER DAMAGE.')
            if sun_spot_damage >= -2 and sun_spot_damage <= -1:
                comp_f('MINOR DAMAGE RECIEVED TO POWER CORE')
                comp_f(
                    'CURRENTLTY IRREPAIRABLE, OUR ENERGY STORAGE WILL BE'
                    ' SLIGHTLY REDUCED TO AVOID FURTHER DAMAGE.')
    elif event == 26:  # MAJOR EVENT: METOR SHOWER
        comp_f(
            "[WARNING] THE COMET IS RAPIDLY APPROACHING SOLAR SYSTEM'S"
            " ASTROID BELT")
        comp_f("STELLAR MASS RAPIDLY ENTERING COMET")
        comp_f("IMPACTS PROBABLE. AREAS MAY RECEIVE DAMAGE.")
        comp_f("BRACING...")
        calculating()
        fate_Rover = random.randrange(1, 100, 1)
        if fate == fate_number1:
            charge == 0  # DEATH
        else:
            comp_f("ROVER MAIN UNIT WAS UNAFFECTED BY METEOR IMPACTS.")
            comp_f("AREAS AROUND THE MISSION AREA HAVE BEEN AFFECTED HOW"
                   "EVER.")
            comp_f("CHECKING FOR SHIP SIGNAL.")
            fate_Rover = random.randrange(1, 100, 1)
        if fate == fate_number2:
            charge = 0
        else:
            comp_f("SIGNAL RESPONSE RECEIVED.")
            comp_f("OUR CRAFT IS STILL OPERATIONAL.")
            comp_f("LET US MOVE ON WITH THE MISSION.")
        return event #Allows the value of event to be tracked by movement()
# ADD A RANDOM DIALOG DEFINITION FOR ALL THE LOCATIONS
def A1():  # EDGE NORTH WEST
    comp_f(
        "WE ARE IN THE A1 BOUNDARY LINE. FURTHER MOVEMENT NORTH OR WEST IS "
        "PROHIBITED.")
    comp_f("SONAR SHOWS FLAT TERRAIN. LARGE SPIKE IN ALTITUDE FOUND "
           "SOUTHWARD POSSIBLE LARGE SCALE SONAR POSSIBLE FROM THOSE "
           "ALTITUDES.")
    if not local_Rover == local_Ship:
        comp_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (local_Rover + 5 or local_Rover + 1 or local_Rover - 1 or local_Rover \
            -5) == local_Ship:
        comp_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    event_Value = event_trigger()
    return event_Value

def A2():  # EDGE
    comp_f("WE ARE IN THE A2 BOUNDARY LINE. FURTHER MOVEMENT NORTH IS "
        "PROHIBITED.")
    comp_f("SONAR SHOWS FLAT TERRAIN WITH SLIGHT SHIFTS IN ELEVATION "
           "SOUTHEAST.")
    if not local_Rover == local_Ship:
        comp_f("THE SHIP IS NOT HERE. LET US MOVE ON.")
    if (local_Rover + 5 or local_Rover + 1 or local_Rover - 1 or local_Rover \
        - 5) == local_Ship:
        comp_f("THE SHIP SIGNAL IS STRONG, WE ARE CLOSE")
    event_Value = event_trigger()
    return event_Value


def A3():  # EDGE NORTH
    null


def A4():  # EDGE
    null


def A5():  # EDGE NORTH EAST
    null


def B1():  # EDGE
    null


def B2():  # INNER EDGE
    null


def B3():  # INNER EDGE
    null


def B4():  # INNER EDGE
    null


def B5():  # EDGE
    null


def C1():  # EDGE WEST
    null


def C2():  # INNER EDGE
    null


def C3():  # CENTER
    null


def C4():  # INNER EDGE
    null


def C5():  # EDGE EAST
    null


def D1():  # EDGE
    null


def D2():  # INNER EDGE
    null


def D3():  # INNER EDGE
    null


def D4():  # INNER EDGE
    null


def D5():  # EDGE
    null


def E1():  # EDGE SOUTH WEST
    null


def E2():  # EDGE
    null


def E3():  # EDGE SOUTH
    null


def E4():  # EDGE
    null


def E5():  # EDGE SOUTH EAST
    null


# ACTUAL START OF CODE   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
completion = 0
print('W',
      end='')  # All these print statements are shortened to the function comp_(fast [f],super fast [sf],and slow [s]) and human_.
time.sleep(
    .0125)  # Refer to human_ (First couple lines) for more information on the general creation of the code and its functions.
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
comp_f('DEFINE NAME OF OPERATOR: ')
operator = input()
calculating()  # Hops up to the calculating definition
comp_f('HELLO ' + str.upper(operator) + '.')
time.sleep(1)
comp_f('RUNNING SYSTEMS DIAGNOSTICS. PLEASE WAIT...')
time.sleep(2)
diagnostics()  # Hops up to the diagnostics definition
main_menu1()  # Hops up to the main menu definition
