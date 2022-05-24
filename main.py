import random
import string
from time import sleep
from termcolor import colored
import datetime

def func():
    chance=random.randint(0,10000)
    amount_gen=random.random()
    time = datetime.datetime.now()
    r_string = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(30)])

    f = open("bitlog.txt", "a")

    if chance == 1:
        print(colored(r_string, 'blue'), colored(str(amount_gen) + "BTC", 'green'))
        print(colored(str(amount_gen) + "BTC added to bitlog wallet", 'yellow'))
        f.write (("%s:%s:%s %s/%s/%s | +%sBTC\n" % (time.hour, time.minute, time.second,time.day, time.month, time.year, str(amount_gen))))
        f.close()
 
    else:
        print(colored(r_string, 'blue'), colored("0.00BTC", 'red'))

    sleep(0.01)

while (True):
    func()
