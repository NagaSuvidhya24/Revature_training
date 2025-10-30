from BankDetails import BankDetail

class CreditCards(BankDetail):
    def __init__(self, custid, cname, bal,creditcardscore,status):
        super().__init__(custid, cname,bal)
        self.creditcardscore=creditcardscore
        self.status=status

    def welcome_message(self):
        print(f'Welcome to SBI,{self.cname}')

    def display_cc_details(self):
        print(f'{self.creditcardscore} - {self.status}')