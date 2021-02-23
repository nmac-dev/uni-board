"""
Script to generate random users to be loaded to database.
To use: fill_user_data.py <number of users> <destination  file>
"""

import names, os, sys
if len(sys.argv) != 3:
    print('Include number of users to generate and output file as arguments!')
    exit()
file , num_users= sys.argv[2], int(sys.argv[1])

def create_user(first, last):
    user = [
        '{\n',
        '    \"model\": \"auth.user\",\n',
        '    \"pk\": 1,\n',
        '    \"fields\": {\n',
        '        \"password\": \"pbkdf2_sha256$216000$zWN0FuzR361j$FhccKCZlcquGXBi7kqC+BuQGnL1DSmMaOCjl6fWOdL0=\",\n',
        '        \"last_login\": \"2021-02-23T15:41:42.878Z\",\n',
        '        \"is_superuser\": false,\n',
        '        \"username\": \"' + first.lower() + '-' + last.lower() + '\",\n',
        '        \"first_name\": \"' + first +'\",\n',
        '        \"last_name\": \"' + last +'\",\n',
        '        \"email\": \"' + first.lower() + '.' + last.lower() + '@mail.com' + '\",\n',
        '        \"is_staff\": false,\n',
        '        \"is_active\": true,\n',
        '        \"date_joined\": \"2021-02-23T15:41:36.340Z\",\n',
        '        \"groups\": [],\n',
        '        \"user_permissions\": []\n',
        '    }\n',
        '},\n',
    ]
    return user

with open(file, 'w') as f:
    f.write('[\n')
    for i in range(num_users):
        lines = create_user(names.get_first_name(), names.get_last_name())
        for line in lines:
            f.write(line)
    f.seek(f.tell() - 2, os.SEEK_SET)
    f.truncate()
    f.write('\n]')