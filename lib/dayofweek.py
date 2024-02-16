class Mornings:

    def __init__(self, day_of_week):
        self.day_of_week = day_of_week
        self.morning_routine()
    
    def morning_routine(self):
        print('4:30 a.m.')
        print('wake up')
        print('work out')
        print('shower')
        print('brush teeth')
        print('get dressed')
        print('let dog out')
        print('feed dog')
        print('drink coffee')
        print('pack kids lunch')
        print('wake kid up')
        print('make kid breakfast')
        print('drink coffee')
        print('walk kid to school bus')
        print('walk dog')
        print('make breakfast')
        print('eat breakfast')
        print('start my day')

class Friday(Mornings):

    def __init__(self, day_of_week):
        super().__init__(day_of_week)
        
    def morning_routine(self):
        super().morning_routine()
        print('b/c its Friday, make more coffee')
        print('drink coffee')
        self.caffeinated = True

friday = Friday('Today')






