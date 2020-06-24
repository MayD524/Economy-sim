import random

sellers_list = []
buyers_list = []
buyers = {}
sellers = {}

## Sellers
## id: [value, bar]


def check_even(num):
    num = int(num)
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



recent_ids = []

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
    sale = False
    for i in range(1, len(buyers_list)):
        if i % 2 != 0:
        
            for x in range(2, len(sellers_list)):
                if x %2 == 0:
                    cseller = choose_seller(x, i)
                    is_comp = cseller.is_compatable()
                    if is_comp:
                        sale = start_transaction(i, x)
                    else:
                        x+1
                        if x not in range(len(sellers_list)):
                            continue
                            
                    if sale and buyers[x]['bought'] == False and sellers[i]['sold'] == False:
                        buyers[x]['bought'] = True
                        sellers[i]['sold'] = True
                        print(f"{i} sold to {x}")
                    else:
                        x + 1
                        if x not in range(len(sellers_list)):
                            continue
                else:
                    continue
        else:
            continue

def main_loop():


    def start_person(sid, value, bar):
        mk = make_person(sid, value, bar)
        mk.make_the_person()

    for sid in range(1, 1000):

        if sid not in recent_ids:
            recent_ids.append(sid)

        else:
            continue

        value = random.randint(1, 100)
        bar = random.randint(1, value)
        start_person(sid, value, bar)
    make_transactions()


if __name__ == "__main__":
    ## Program Start ##
    main_loop()
    
    
    
