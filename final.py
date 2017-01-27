# Quiz app for bc-14-justinmacharia Quiz app
# Author: Justin Macharia
# Version: 1.0

# library to help work with and search directories
import os

# library to help time  how long the quiz should take
import time

# library to help color our tables and output
from colorclass import Color, Windows

# library to help print out tabular data
from terminaltables import SingleTable

# library to help create and load json files(our quizzes)
import json



# current path for the file we are working on:
current_path = os.path.dirname(os.path.abspath(__file__))

# function to help display the main menu.


def show_menu():
    # set table color elements for Menu item to green
    table = [[Color('{autogreen}Menu Item{/autogreen}'), 'Description'],
             [Color('{autogreen} 1{/autogreen}'), 'See Categories of quizzes available'],
             [Color('{autogreen} 2{/autogreen}'), 'Import quiz from firebase']
             ]
    table_instance = SingleTable(table)
    table_instance.inner_heading_row_border = False
    print(table_instance.table)
    print("")
    print("")

# function to display the various quiz categories


def show_quiz_categories():
    print("")
    print("             QUIZ CATEGORIES  ")
    print("")

    # set quiz category table items to color yellow
    table = [[Color('{autoyellow}Quiz Category{/autoyellow}'), 'Description'],
             [Color('{autoyellow}1{/autoyellow}'), 'Open ended questions'],
             [Color('{autoyellow}2{/autoyellow}'), 'Closed questions']
             ]
    table_instance = SingleTable(table)
    table_instance.inner_heading_row_border = False
    # print table
    print(table_instance.table)
    print("")
    print("")


# function to show list of open ended questions
def show_list_of_open_ended_questions():
    file_count = 0

    # check to see if the path to questions exists
    if os.path.exists(current_path) == True:

        # print out names of files that end with .json in the quizzes folder
            print("          Number of quizzes          Quiz names                         ")
            for my_files in os.listdir(current_path + '/Open quizzes/'):
                if my_files.endswith('.json') == True:
                    file_count += 1
                    file_names = my_files.strip('.json')

                    print("          %d                       %s             " % (file_count, file_names))
                    print("")
                    print("")
                else:
                    my_shell()
# show list of closed questions
def show_list_of_closed_questions():
    file_count = 0

    # check to see if the path to questions exists
    if os.path.exists(current_path) == True:

        # print out names of files that end with .json in the quizzes folder
            print("          Number of quizzes          Quiz names                         ")
            for my_files in os.listdir(current_path + '/Closed quizzes/'):
                if my_files.endswith('.json') == True:
                    file_count += 1
                    file_names = my_files.strip('.json')

                    print("          %d                       %s             " % (file_count, file_names))
                    print("")
                    print("")
                else:
                    my_shell()


# function to check quiz availability and take closed quiz

def check_quiz_availability_and_take_closed_quiz(quiz_selector_input):
    quiz_list = []

    # check to see if the quiz exists
    if os.path.exists(current_path) == True:

            for my_files in os.listdir(current_path + '/Closed quizzes/'):
                if my_files.endswith('.json') == True:
                    quiz_list.append(my_files)

                    # Get the initials of the file that will allow us to print that particular quiz
                    for each_file in quiz_list:
                        my_checker = each_file[-8:-6]
                        if my_checker == quiz_selector_input:
                            print("The quiz is available")
                            print("")

                            # prompt the user to see if they would like to take the test or not
                            my_input = input("Would you like to do it? Press Y if yes and N if not: ").upper()

                            # check for valid input
                            while my_input not in ['Y', 'N']:
                                print("Invalid input! Reply with Y or N")
                                print("")
                                print("")
                                my_input = input("Would you like to do it? Press Y if yes and N if not: ")
                                print("")
                                print("")

                            # if yes then print out the quiz a question at a time
                            if my_input == 'Y':
                                for file_checker in os.listdir(current_path + '/Closed quizzes/'):
                                    if file_checker == each_file:
                                        print(file_checker)

                                        # load the json into out program
                                        with open(current_path + '/Closed quizzes/' + file_checker) as json_data:
                                            print("")
                                            print("")
                                            print("-" * 20)
                                            print(" Loading questions :")
                                            print("")
                                            print("")
                                            time.sleep(0.5)  # delay loading by 0.5 seconds
                                            d = json.load(json_data)

                                            correct_count = 0
                                            tracker = 0
                                            temp = 0
                                            duration = 60
                                            while tracker <= len(d):
                                                loop_count = 0

                                                # start timing

                                                start_time = int(time.time())

                                                # set duration of my quiz to 60 seconds
                                                duration = 10 * len(d)

                                                # print out each question one at a time
                                                for quiz in d:
                                                    for key in d[quiz]:
                                                        for question in key:
                                                            loop_count += 1
                                                            duration = 60

                                                            # print question
                                                            print(question)
                                                            print("")
                                                            print('A. ', key[question][0]['A'])
                                                            print('B. ', key[question][1]['B'])
                                                            print('C. ', key[question][2]['C'])
                                                            print('D. ', key[question][3]['D'])

                                                            # prompt for an answer

                                                            ans = input("     Your answer(Answer with A,B,C or D): ").upper()
                                                            print("")
                                                            timed = int(time.time()) - start_time

                                                            # if the duration ends, break
                                                            if timed > duration:
                                                                print('-' * 20)
                                                                print("YOUR TIME IS UP")
                                                                print('-' * 20)
                                                                break

                                                            # check to see if the answer is correct

                                                            if ans == 'A':
                                                                checker = key[question][0]['is_answer']
                                                                if checker == True:
                                                                    correct_count +=  1

                                                            elif ans == 'B':
                                                                checker = key[question][1]['is_answer']
                                                                if checker == True:
                                                                    correct_count +=  1
                                                            elif ans == 'C':
                                                                checker = key[question][2]['is_answer']
                                                                if checker == True:
                                                                    correct_count +=  1
                                                            elif ans == 'D':
                                                                checker = key[question][3]['is_answer']
                                                                if checker == True:
                                                                    correct_count +=  1
                                                            else:
                                                                print("Invalid input")

                                                    # break out of the while loop if the time is up
                                                    elapsed_time = timed
                                                    if elapsed_time > duration:
                                                        print('-' * 20)
                                                        print("YOUR TIME IS UP")
                                                        print('-' * 20)
                                                        break
                                                    tracker = loop_count
                                                    tracker += 1

                                            # Calculate results and show  answers and scores  in percentage
                                            total = len(key)
                                            result = (correct_count / total) * 100

                                            # print out message depending on scores
                                            if result >= 80 or correct_count >= 4:
                                                print("")
                                                print(" Excellent! ")
                                                print('You have %d out of %d questions  correct!' % (correct_count, len(key)))
                                                print('Your have scored %d %%' % result)

                                            elif result >= 60 or correct_count >= 3:
                                                print("")
                                                print(" Good work! ")
                                                print('You have %d out of %d questions  correct!' % (correct_count, len(key)))
                                                print('Your have scored %d %%' % result)

                                            elif result >= 40 or correct_count >= 2:
                                                print("")
                                                print(" Average! Work harder ")
                                                print('You have %d out of %d questions  correct!' % (correct_count, len(key)))
                                                print('Your have scored %d %%' % result)

                                            elif result >= 20 or correct_count >= 1:
                                                print("")
                                                print(" Level up in this test subject! ")
                                                print('You have %d out of %d questions  correct!' % (correct_count, len(key)))
                                                print('Your have scored %d %%' % result)

                                            elif result >= 0 or correct_count >= 0:
                                                print("")
                                                print(" You've Failed! ")
                                                print('You have %d out of %d questions  correct!' % (correct_count, len(key)))
                                                print('Your have scored %d %%' % result)
                            if my_input == 'N':
                                my_shell()



def check_quiz_availability_and_take_open_quiz(quiz_selector_input):
    quiz_list = []

    # check to see if the quiz exists
    if os.path.exists(current_path) == True:

            for my_files in os.listdir(current_path + '/Open quizzes/'):
                if my_files.endswith('.json') == True:
                    quiz_list.append(my_files)

                    # Get the initials of the file that will allow us to print that particular quiz
                    for each_file in quiz_list:
                        my_checker = each_file[-8:-6]
                        if my_checker == quiz_selector_input:
                            print("The quiz is available")
                            print("")

                            # prompt the user to see if they would like to take the test or not
                            my_input = input("Would you like to do it? Press Y if yes and N if not: ").upper()

                            # check for valid input
                            while my_input not in ['Y', 'N']:
                                print("Invalid input! Reply with Y or N")
                                print("")
                                print("")
                                my_input = input("Would you like to do it? Press Y if yes and N if not: ")
                                print("")
                                print("")

                            # if yes then print out the quiz a question at a time
                            if my_input == 'Y':
                                for file_checker in os.listdir(current_path + '/Open quizzes/'):
                                    if file_checker == each_file:
                                        print(file_checker)

                                        # load the json into out program
                                        with open(current_path + '/Open quizzes/' + file_checker) as json_data:
                                            print("")
                                            print("")
                                            print("-" * 20)
                                            print(" Loading questions :")
                                            print("")
                                            print("")
                                            time.sleep(0.5)  # delay loading by 0.5 seconds
                                            d = json.load(json_data)

                                            correct_count = 0
                                            tracker = 0
                                            duration = 60
                                            while tracker <= len(d):
                                                loop_count = 0

                                                # start timing
                                                start_time = int(time.time())

                                                # set duration of my quiz to 60 seconds
                                                duration = 10 * len(d)

                                                # print out each question one at a time
                                                for key in d.keys():
                                                    loop_count += 1
                                                    duration = 60

                                                    # print question
                                                    print(key)
                                                    print("")

                                                    # prompt for an answer

                                                    ans = input("     Your answer: ").lower()
                                                    print("")
                                                    timed = int(time.time()) - start_time

                                                    # if the duration ends, break
                                                    if timed > duration:
                                                        print('-' * 20)
                                                        print("YOUR TIME IS UP")
                                                        print('-' * 20)
                                                        break

                                                    # check to see if the answer is correct

                                                    if ans == str(d[key]):
                                                        print("")
                                                        print("")
                                                        print("Correct!")
                                                        correct_count = correct_count + 1

                                                    else:
                                                        print("")
                                                        print("")
                                                        print("Incorrect answer!")

                                                # break out of the while loop if the time is up
                                                elapsed_time = timed
                                                if elapsed_time > duration:
                                                        print('-' * 20)
                                                        print("YOUR TIME IS UP")
                                                        print('-' * 20)
                                                        break
                                                tracker = loop_count
                                                tracker += 1

                                            # Calculate results and show  answers and scores  in percentage
                                            total = len(d)
                                            result = (correct_count / total) * 100

                                            # print out message depending on scores
                                            if result >= 80 or correct_count >= 4:
                                                print("")
                                                print(" Excellent! ")
                                                print('You have %d out of %d questions  correct!' % (correct_count, len(d)))
                                                print('Your have scored %d %%' % result)

                                            elif result >= 60 or correct_count >= 3:
                                                print("")
                                                print(" Good work! ")
                                                print('You have %d out of %d questions  correct!' % (correct_count, len(d)))
                                                print('Your have scored %d %%' % result)

                                            elif result >= 40 or correct_count >= 2:
                                                print("")
                                                print(" Average! Work harder ")
                                                print('You have %d out of %d questions  correct!' % (correct_count, len(d)))
                                                print('Your have scored %d %%' % result)

                                            elif result >= 20 or correct_count >= 1:
                                                print("")
                                                print(" Level up in this test subject! ")
                                                print('You have %d out of %d questions  correct!' % (correct_count, len(d)))
                                                print('Your have scored %d %%' % result)

                                            elif result >= 0 or correct_count >= 0:
                                                print("")
                                                print(" You've Failed! ")
                                                print('You have %d out of %d questions  correct!' % (correct_count, len(d)))
                                                print('Your have scored %d %%' % result)
                            if my_input == 'N':
                                my_shell()

# function to help the user interact with the console app at a high level


def my_shell():
    while True:
        Windows.enable()  # enable windows colors so we can use color in terminal tables

        # Introductory message
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("                           [QUIZZES]                ")
        print("")
        print("")
        print("")
        print("        How much do you know about what you think you know?           ")
        print("")
        print("")
        print("")
        menu_input = input("                    Enter M to view menu:    ").upper()
        print("  ")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")

        # check menu input for correctness
        while menu_input != 'M':
            print("              ALERT! Please enter valid input to continue")
            print("")
            print("")
            menu_input = input("                    Enter M to view menu:    \n").upper()
            print("")
            print("")
        if menu_input == 'M':
            show_menu()

        # prompt for menu items input
        menu_item_input = input(" Select a menu item to proceed: ")

        while menu_item_input not in [1, 2, '1', '2']:
            print(" Invalid input! Please enter a menu Item Number")
            print("")
            print("")
            menu_item_input = input("Select a menu item to proceed: ")
            print("")
            print("")

        # if menu item input is valid then call the show quiz categories function
        if menu_item_input in [1, 2, '1', '2']:
            if menu_item_input in [1, 2, '1', '2']:
                show_quiz_categories()

        # prompt for quiz category input
        quiz_category_input = input("Enter a quiz category to view quizzes in it: ")
        while quiz_category_input not in [1, 2, '1', '2']:
            print("Invalid input! Please enter a quiz category number")
            print("")
            print("")
            quiz_category_input = input("Select a quiz category number: ")
            print("")
            print("")

        # if input is valid call the show list of open ended or option based questions function
        if quiz_category_input in [1, 2, '1', '2']:
            if quiz_category_input in [1, '1']:
                show_list_of_open_ended_questions()
            elif quiz_category_input in [2, '2']:
                show_list_of_closed_questions()

        # prompt for quiz selector input
        quiz_selector_input = input("Enter the initials in brackets of the quiz you would like to do: ")

        while len(quiz_selector_input) != 2:
            print("Problem loading quiz...")
            print("")
            print("Please select another quiz or enter correct initials")
            print("")
            quiz_selector_input = input("Enter the initials in brackets of the quiz you would like to do: ")
            print("")
            print("")

        # allow the user to take the quiz if it is available
        if isinstance(quiz_selector_input, str):
            if quiz_category_input in [1, '1']:
                check_quiz_availability_and_take_open_quiz(quiz_selector_input)
            elif quiz_category_input in [2, '2']:
                check_quiz_availability_and_take_closed_quiz(quiz_selector_input)


if __name__ == "__main__":
    my_shell()
