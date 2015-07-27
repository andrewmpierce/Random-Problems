class Coffee:
    def __init__(self):
        self.pound_cost = 10.50

    def order_cost(self, how_many):
        order_cost = ((self.pound_cost +.86) * how_many) + 1.50
        print ("Your order will cost $%r" %order_cost)

coffee = Coffee()
coffee.order_cost(5)
