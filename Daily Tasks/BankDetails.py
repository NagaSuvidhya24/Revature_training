from typing import final


class BankDetail:
    def __init__(self,custid,cname,bal):
        self.custid= custid
        self.cname= cname
        self.bal= bal

    @final
    def welcome_message(self):
        print('Welcome to SBI ')

    def display_details(self):
        print(f'{self.custid} - {self.cname} - {self.bal}')
