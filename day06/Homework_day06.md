# Homework_day06



## 1번 문제

> Python은 객체 지향 프로그래밍 언어입니다. Python에서 기본적으로 정의되어
> 있는 클래스 5가지만 작성하시오.

str  /  list  /  dict  /  int /  float



## 2번 문제

> 다음 매직 메서드의 역할을 간단하게 작성하시오.
> • __init__
> • __del__
> • __str__
> • __repr__

1. init : 생성자는 인스턴스 객체가 생성될 때 호출되는 함수
2. del : 소멸자는 객체가 소멸되는 과정에서 호출되는 함수
3. str : __str__ 함수의 리턴값은 print안에 넣은 경우 나옴
4. repr : __repr__함수의 리턴값은 그냥 호출시 나옴



## 3번 문제

> 아래 코드의 ‘.sort()’와 같이 문자열, 리스트, 딕셔너리 등을 조작할 때
> 사용하였던 것들은 클래스에 정의된 메서드들이었다. 이처럼 문자열, 리스트,
> 딕셔너리 등을 조작하는 메서드 3가지를 그 역할과 함께 작성하시오.
>
> ```python
> numbers = [5, 1, 2]
> numbers.sort()
> print(numbers)  #[1, 2, 5]
> ```

```python
numbers = [5, 1, 2]
numbers.reverse()
print(numbers)

# 결과 : [2, 1, 5]
# reverse() 메소드는 리스트 순서를 바꿔준다
```

```python
numbers = [5, 1, 2]
numbers.append(3)
print(numbers)

# 결과 : [5, 1, 2, 3]
# append() 메소드는 요소를 추가해준다
```

```python
numbers = [5, 1, 2]
numbers.pop()
print(numbers)

# 결과 : [5, 1]
# pop() 메소드는 요소를 빼내준다
```

