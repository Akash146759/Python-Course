
def bill(bill_amount, tip_perc):
    total_amt = bill_amount*(1 + 0.01*tip_perc)
    total_amt = round(total_amt,2)
    print('Please pay : ', total_amt)

amount = int(input('enter bill amount : '))
tip_perc = int(input('enter tip percentage amount : '))



bill(amount, tip_perc)

bill(1200,20)



