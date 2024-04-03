#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(number, target):
    answer = 0
    if number < target:
        while not number == target:
            if number > target:
                number = number - 1
                answer = answer + 1
                continue
            number1 = number + 1
            abs1 = abs(target - number1)
            number2 = number * 2
            abs2 = abs(target - number2)
            if abs1 > abs2:
                answer = answer + 1
                number = number2
            elif abs1 < abs2:
                answer = answer + 1
                number = number1
    
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
number1 = 5
target1 = 9
ret1 = solution(number1, target1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 3
target2 = 11
ret2 = solution(number2, target2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")