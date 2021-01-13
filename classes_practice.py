class Human(object):
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == 'tennis player':
            print(self.name + " plays tennis!")
        elif self.occupation == 'actor':
            print(self.name + ' stars in movies!')

    def says(self):
        print(self.name + ' says hello to you!')

if __name__ == '__main__':

    tom = Human('tom cruise', 'actor')
    tom.do_work()
    tom.says()

    print()
    roger = Human('roger federer', 'tennis player')
    roger.do_work()
    roger.says()
