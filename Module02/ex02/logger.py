import time
from random import randint
import os
import functools

firstRun = True


def log_entry(user, fct_name, exec_time):
    if exec_time < 1:
        unit = "ms"
        exec_time /= 1000
    else:
        unit = "s"
    return "({0})Running: {1:18} [ exec-time = {2:.3f} {3} ]\n".format(
                user,
                fct_name.replace("_", " ").title(),
                exec_time,
                unit)


def write_log(function_name, time, firstRun=False, usr=os.environ.get('USER')):
    opt = 'a'
    if firstRun:
        opt = 'w'
        firstRun = False
    logfile = open("machine.log", opt)
    logfile.write(log_entry(usr, function_name, time))
    logfile.close()
    return firstRun


def log(func):
    def wrapper(*args, **kwargs):
        ts = time.perf_counter()
        res = func(*args, **kwargs)
        te = time.perf_counter()
        global firstRun
        firstRun = write_log(func.__name__, te - ts, firstRun)
        return res
    return wrapper


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    
    machine.make_coffee()
    machine.add_water(70)
