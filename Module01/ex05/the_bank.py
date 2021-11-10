class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
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
        members = [attr for attr in dir(account)
                   if not callable(getattr(account, attr))
                   and not attr.startswith("__")]
        res = [False, False, False, False]
        if len(members) % 2 == 1:
            res[0] = True
        if any(attr.startswith('b') for attr in members):
            res[1] = True
        if not any(attr.startswith('zip') or attr.startswith('addr')
                   for attr in members):
            res[2] = True
        if 'name' and 'id' and 'value' not in members:
            res[3] = True
        return res

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
        if any(self.is_corrupted(origin)) or any(self.is_corrupted(dest)):
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
        corruption = self.is_corrupted(account)
        attr = a.__dict__
        if not any(corruption):
            return True
        if corruption[1]:
            for key in attr.keys():
                if key.startswith('b'):
                    attr[key[1:]] = attr.pop(key)
        if corruption[2]:
            print("Missing information:\n\tClient {0}\n".format(attr))
            to_add = input("Would you like to complete \'zip\' or \'addr\'? ")
            attr[to_add] = input("Enter {0}: ".format(to_add))
        if corruption[3]:
            if 'name' not in attr.keys():
                print("Missing information:\n\tClient {0}\n".format(attr))
                attr['name'] = input("Enter name {0}".format(to_add))
            if 'id' not in attr.keys():
                attr['id'] = len(self.account)
            if 'value' not in attr.keys():
                attr['value'] = 0
        if self.is_corrupted(account)[0]:
            if 'other' not in attr.keys():
                attr['other'] = "nothing"
            else:
                attr['misc'] = "nothing"
        return any(self.is_corrupted(account))
