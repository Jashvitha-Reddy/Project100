class Atm(object):
    def __init__(self,cardnumber,pinumber,transationamount):
        self.cardnumber=cardnumber
        self.pinumber=pinumber
        self.transationamount=transationamount

    def CashWithdrawl(self):
        print("cash with drawled")
    def BalanceAmount(self,bank_balance):
        print("remaining amount")

ICIC = Atm(520,5521,1000)
ICIC.CashWithdrawl()
