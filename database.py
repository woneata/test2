# create record
# update record
# read record
# delete
# CRUD

# find user

def create(account_number, user_details):
    completion_state = False
    try:

        f = open("data/user_record/" + str(account_number) + ".txt", "x")

    except FileExistsError:
        print("User already exists")
        # delete the already created file, and print out error, then return false
        return completion_state

    else:
        f.write(str(user_details));

    finally:
        f.close();
    return completion_state
    # create a file - account_number.txt
    # add the user details to the file
    # return true
    # if saving to file file fails, then delete created file


def read(user_account_number):
    print('read user record')
    # find user with account number
    # fetch content of the file


def update(user_account_number):
    print('update user record')
    # find user with account number
    # fetch the contents of the file
    # update the contents of the file
    # save the file
    # return true


def delete(user_account_number):
    print('delete user record')
    # find user with account number
    # delete the user record (file)
    # return true


def find(user_account_number):
    print('find user')
    # find user record in the data folder

