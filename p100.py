class ATM:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def checkbalence(self,amount):
        print('your balence is ',amount)
    def widraw(self,a,w):
        newamount=a-w
        print('you have witdrawn'+str(w)+' your remaining balence is '+str(newamount))

def main():
    cardnumber=input('insert your card number')
    pin=input('inset your pin')
    a=50000
    newUser=ATM(cardnumber,pin)
    print('choose you activity')
    print('1: balence inqurie 2: witdraw')
    activity=int(input('enter you activity number'))
    if (activity==1):
        newUser.checkbalence(a)
    elif (activity==2):
        amount=int(input('enter the amount'))
        newUser.widraw(a,amount)
    else:
        print('enter a valid number')
if __name__=='__main__':
    main()