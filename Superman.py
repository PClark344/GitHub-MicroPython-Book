import utime

user_name = 'Charlie Corli'
superman_user_name = 'Clark Kent'

while user_name != superman_user_name:
    user_name = input('What is your name? ')
    if user_name == 'Paul Clark':
        print('Close but no cigar')
    else:
        if user_name != superman_user_name:
            print('You are not Superman')
print('You are Superman!!')
utime.sleep(1)
print('Now stop lounging around and save the world again.')
