class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        #if hasattr(self, 'value'):
        #    self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []
    
    def add(self, account):
        self.account.append(account)

    def find_account(self, account):
        for a in self.account:
            if a.name == account or a.id == account:
                return a
        return None

    def is_corrupted(self, a):
        account = self.find_account(a)
        members = [attr for attr in dir(account) if not callable(getattr(account, attr)) and not attr.startswith("__")]
        if len(members) % 2 and any(attr.startswith('b') for attr in members) and \
            not any(attr.startswith('zip') or attr.startswith('addr') for attr in account.__dict__.values()) or \
             'name' and 'id' and 'value' not in members:
            return True
        return False

    def get_value(self, account):
        find = self.find_account(account)
        if not find:
            raise ValueError("Cannot identify account")
        else:
            return find.value    

    def check_object(self, account):
        if not isinstance(account, int) and not isinstance(account, str):
            return False
        if not self.find_account(account):
            return False
        return True

    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest: int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        if not self.check_object(origin) or not self.check_object(dest):
            return False
        if self.is_corrupted(origin) or self.is_corrupted(dest):
            return False
        if amount < 0 or self.get_value(origin) - amount < 0:
            return False
        return True
        
    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return True if success, False if an error occured
        """
        a = self.find_account(account)
        pass
