# Problem Description
# -----------------------

'https://www.hackerrank.com/challenges/bon-appetit/problem'


def bonappetite(bill):
    k = int(input('Enter item not wanted by Anna: '))
    orig_bill = []
    orig_bill.extend(bill)

    try:
        if k == bill.index(bill[k]):
            response = input('Anna! U OK?(y/n): ')
            while response is not 'n' or 'y':
                response = input('Anna! U OK?(y/n): ')
                if response is 'n':
                    bill.pop(bill.index(bill[k]))
                    anna_amt = (sum(bill)) / 2
                    bryan_amt = sum(orig_bill) - anna_amt
                    return f"""Amount to be paid by Anna: {anna_amt}
                            \nAmount to be paid by Bryan: {bryan_amt}"""
                elif response is 'y':
                    payable_amt = (sum(bill)) / 2
                    anna_refund = bill[k] / 2
                    print(f"Amount to be paid y both: {payable_amt}")
                    return f'Amount to be refunded to Anna:{anna_refund}'

    except Exception as err:
        return err.args
    finally:
        print('Welcome !')


bill = [30, 45, 50, 20, 32]
print(bonappetite(bill))
