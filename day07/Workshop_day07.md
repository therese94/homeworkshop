# Workshop_day06



## 1번 문제

> 아래와 같은 Animal 클래스가 있을 때, 해당 클래스를 상속 받아 아래 보기와 같이
> 동작하는 Dog 클래스와 Bird 클래스를 작성하시오.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):
    def walk(self):
        super().walk()

    def run(self):
        print(f'{self.name}! 달린다!')

class Bird(Animal):
    def walk(self):
        super().walk()

    def eat(self):
        print(f'{self.name}! 먹는다!')

    def fly(self):
        print(f'{self.name}! 푸드덕!')

dog = Dog('바둑이')
bird = Bird('구구')

dog.walk()
dog.run()

bird.walk()
bird.eat()
bird.fly()
```



