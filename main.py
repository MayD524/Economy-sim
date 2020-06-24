import random, time

sellers_list = []
buyers_list = []
buyers = {}
sellers = {}

def check_even(num):
    if num %2 == 0:
        return True
    else:
        return False

class choose_seller:
    def __init__(self, buyer_id, seller_id):
        self.buyer_id = buyer_id
        self.seller_id = seller_id

    def is_compatable(self):
        self.sellers_bar = sellers[self.seller_id]['bar']
        self.sellers_value = sellers[self.seller_id]['value']
        self.buyers_value =  buyers[self.buyer_id]['value']

        if self.sellers_bar > self.buyers_value:
            return False
        elif self.sellers_bar < self.buyers_value and self.sellers_value <= self.buyers_value:
            return True

class make_person:

    def __init__(self, sid, value, bar):
        self.id = sid
        self.value = value
        self.bar = bar

    def add_person(self):

        if self.even == True:
            buyers[self.id] = {}
            buyers_list.append(self.id)
        else:
            sellers[self.id] = {}
            sellers_list.append(self.id)

    def make_the_person(self):
        self.even = check_even(self.id)
        self.add_person()

        if self.id in buyers_list:
            buyers[self.id]['value'] = self.value
            buyers[self.id]['bought'] = False

        elif self.id in sellers_list:
            sellers[self.id]['value'] = self.value
            sellers[self.id]['bar'] = self.bar
            sellers[self.id]['sold'] = False
        else:
            return

def start_transaction(seller_id, buyer_id):
    sale = False
    sellers_bar = sellers[seller_id]['bar']
    sellers_value = sellers[seller_id]['value']
    buyers_value =  buyers[buyer_id]['value']

    if buyers_value < sellers_value and buyers_value > sellers_bar:
        sale = True
    elif buyers_value < sellers_value and buyers_value < sellers_bar:
        sale = False
    elif buyers_value > sellers_value:
        sale = True
    return sale

def make_transactions():
    i = random.choice(list(buyers.keys()))
    x = random.choice(list(sellers.keys()))
    cseller = choose_seller(i, x)
    is_comp = cseller.is_compatable()
    if is_comp:
        sale = start_transaction(x, i)
    else:
        return
    
    if sale and buyers[i]['bought'] == False and sellers[x]['sold'] == False:
        buyers[i]['bought'] = True
        sellers[x]['sold'] = True
        print(f'{x} sold to {i}')
    
    else:
        return
    
    

def change_seller():
    for i in sellers.keys():
        if sellers[i]['sold'] == False:
            sellers[i]['value'] -= 10
            sellers[i]['bar'] -= 10
        elif sellers[i]['sold'] == True:
            sellers[i]['value'] += 10
            sellers[i]['bar'] += 10


def main(max_people):
    day = 0
    print(f'day {day}')
    while True:
        for i in range(1, max_people):
            make_transactions()
        time.sleep(10)
        day +=1
        print(f'day {day}')
        change_seller()

def start(max_people):
    for sid in range(1, max_people):
        def start_person(sid, value, bar):
            mk = make_person(sid, value, bar)
            mk.make_the_person()
        value = random.randint(1, 100)
        bar = random.randint(1, value)
        start_person(sid, value, bar)
    main(max_people)

if __name__ == "__main__":
    ## START ##
    max_people = 100
    start(max_people) 
    
