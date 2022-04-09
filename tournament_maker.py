import csv
import json

def sign_up(dict):
    input_name = input('Participant Name: ')
    input_slot = input('Desired starting slot #[1-' + str(len(dict)) + ']: ')
    illegal_entry = True
    while illegal_entry is True:
        if not input_slot.isnumeric():
            print("Do not enter non-numeric values for tournament slots.")
            input_slot = input('Desired starting slot #[1-' + str(len(dict)) + ']: ')
            continue
        elif round(int(input_slot)) <= len(dict) and round(int(input_slot)) >= 1:
            for key in dict:
                if input_name == dict[key]:
                    print('This participant is already in tournament slot ' + dict[key])
                    input_name = input('Participant Name: ')
                    continue
                else:
                    illegal_entry = False
        else:
            print('slot value is out of range for this tournament.')
            input_slot = input('Desired starting slot #[1-' + str(len(dict)) + ']: ')
            continue
    #dict[int(input_slot)] = input_name
    dict.update({input_slot:input_name})
    return dict



def tourn_maker():
    exit = False
    dict = {}
    input_menu_is_legal = False
    input_participants_num = int(input('Welcome to Tournaments R US\n\nEnter the number of participants: '))
    print('There are ' + str(input_participants_num) + ' participant slots ready for sign-ups.')
    for participants in range(input_participants_num):
        dict[str(participants+1)] = None
    while exit == False:
        #while not input_menu_is_legal:
        input_menu = input('Participant Menu\n\n1. Sign Up\n2. Cancel Sign Up\n3. View Participants\n4. Save Changes\n5. Exit\nEnter the number for the Menu you want to use (1-5): ')
        back = False
        if input_menu not in ['1','2','3','4','5']:
            print('\nplease only use a number from 1 to 5 when navigating the menus')
            continue
        elif input_menu == '1':
            adding_roster = True
            while adding_roster:
                dict = sign_up(dict)
                input_adding_more = input('Would you like to add more? (yes/no): ')
                if input_adding_more.lower() == 'yes':
                    adding_roster = True
                else:
                    adding_roster = False
                    break
            continue
        elif input_menu == '2':
            input_legal = False
            while not input_legal:
                input_cancellation_slot = input('Participant Cancellation\n\nStarting slot #[1-' + str(len(dict)) + ']: ')
                if input_cancellation_slot.isnumeric() and int(input_cancellation_slot) > 0 and int(input_cancellation_slot) <= len(dict):
                    break
                else:
                    print('must choose a slot in range')
                    input_legal = False
            input_legal = False
            while not input_legal:
                input_cancellation_name = input('Input Participant Name or escape by entering \"back\": ')
                if input_cancellation_name == dict[str(input_cancellation_slot)]:
                    dict[(input_cancellation_slot)] = None
                    input_legal = True
                elif input_cancellation_name.lower() == 'back':
                    back = True
                    break
                else:
                    print(input_cancellation_name + ' is not in that starting slot.')
                    continue
            if back:
                continue
            else:
                print('Sucess:\n' + input_cancellation_name + ' has been cancelled from slot #' + input_cancellation_slot + '.')
                continue
        elif input_menu == '3':
            input_legal = False
            while not input_legal:
                input_view = input('View Participants\n\nStarting Slot: Participant\n')
                if not input_view.isnumeric():
                    print('that is not a slot number')
                    continue
                elif int(input_view) > len(dict):
                    print('that slot doesn\'t exist')
                    continue
                else:
                    input_legal = True
            input_legal2 = False
            while not input_legal2:
                upper_end = int(input_view) + 5
                lower_end = int(input_view) - 5
                if upper_end > len(dict):
                    upper_end = len(dict)
                    input_legal2 = True
                elif lower_end < 1:
                    lower_end = 1
                    input_legal2 = True
                else:
                    input_legal2 = True
            key_list = []
            diff_end = upper_end - lower_end
            for num in range(0,diff_end+1):
                key_list.append(num + lower_end)
            for key in key_list:
                dict.items
                print(str(key) + " : " + str(dict[str(key)]))
            continue
        elif input_menu == '4':
            input_legal3 = False
            while not input_legal3:
                input_save = input('Save Changes\n\nSave your changes to CSV? [y/n]')
                if input_save.lower() == 'yes' or input_save.lower() == 'y':
                    with open('tournament.csv', 'w') as csvfile:
                        with open('tournament.csv', 'w') as csvfile:
                            for key in dict.keys():
                                csvfile.write("%s,%s\n"%(key,dict[key]))
                    print('your tournament has been saved!')
                    break
                elif input_save.lower() == 'no' or input_save.lower() == 'n':
                    break
                else:
                    print('use \'yes\' or \'no\'')
                    continue
            continue
        elif input_menu == '5':
            input_leave = input('Exit\n\nAny unsaved changes will be lost.\nAre you sure you want to exit? [y/n]')
            if input_leave.lower() == 'y' or input_leave.lower() == 'yes':
                exit = True
                break
            else:
                continue
    print('Goodbye!')


tourn_maker()

#with open('tournament.csv', 'w') as csvfile:
  #  writer = csv.DictWriter(csvfile, fieldnames=['slot','name'])
 #   writer.writeheader()
#    writer.writerows(str(dict.items())

#with open('tournament.csv', 'w') as csvfile:
    #for key in dict.keys():
        #csvfile.write("%s,%s\n"%(key,dict[key]))
