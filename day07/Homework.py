class Calculator:
    count = 0

    def info(self):
        print('나는 계산기 입니다.')
        print(self)

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        print(f'{a} + {b} 는 {a + b}입니다.')

    @classmethod
    def history(cls):
        print(f'총 {cls.count}번 계산 했습니다.')    
        print(cls)

calc = Calculator()

calc.info()
calc.add(1,1)
calc.history()


