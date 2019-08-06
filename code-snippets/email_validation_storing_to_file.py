import re


def email_validate():
    with open('emails.txt', 'r') as file:
        new = file.readlines()
        for each in new:
            # print(each, end='')
            regex = re.fullmatch(r'^[a-zA-Z]\w+@(gmail|hotmail|yahoo)\.com', each[:-1])
            if regex is None:
                print(f"{each} is invalid mail")
                with open('invalid_mail.txt', 'a') as file1:
                    file1.write(each)

            else:
                print(f'{each} is valid')
                with open('valid_mail.txt', 'a') as file1:
                    file1.write(each)


    # if pattern is None:
    #     with open('')


email_validate()
