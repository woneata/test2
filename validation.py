def account_number_validation(account_number):
    # check if account_number is not empty
    # if account_number is 6 digits
    # if the account_number is an integer
    if account_number:

        try:
            int(account_number)

            if len(str(account_number)) == 6:

                return True
        except ValueError:
            print('Invalid account number. Account number should be an integer')
            return False

        else:
            print('Account number must be 6 digits')
            return False

    else:
        print('Account number is a required field')
        return False
