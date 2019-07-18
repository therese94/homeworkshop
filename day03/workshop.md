# Workshop_day03



## 1번 문제

> 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요.

```python
def palindrome(word):
    for i in range(int(len(word)/2)):
        if word[i] != word[-1-i]:   #하나라도 다른게 있으면 False 반환
            return False
        else:
            return True

print(palindrome('abcdedcba'))
print(palindrome('abcdedcb'))
```

(1번 문제 실행화면)

![](img/workshop_01.png)

------------------------------------------------------------------------------------------------------------



```python
##다른답               #reversed 함수 사용

def palindrome(word):
	return True if list(word) == list(reversed(word)) else False
```

```python
##다른답 2             #슬라이싱 사용

def palindrome(word):
return word == word[::-1]
```

