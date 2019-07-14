"""
Utils.py
-----------

Validation functions
"""

def yes_no_option_check(message=''):
    valid_yes = ['Yes','yes','Y','y']
    valid_no = ['No','no','N','n']
    option = None

    while option not in valid_yes or valid_no:
        option = input(message)
        if option in valid_yes:
            return True
        elif option in valid_no:
            return False
        else:
            print('Please enter yes or no')


def check_response_status(response):
    """Checks the response status code and prints """
    if response.status_code is 200:
        print('\n[+] Request Successful (' + (str(response.status_code)) + ')')
        return True
    else:
        print('[-] Request Unsuccessful - ' + (str(response.status_code)))
        return False

