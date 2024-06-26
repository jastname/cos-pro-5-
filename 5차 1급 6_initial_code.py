import time
start = time.time()
def solution(s1, s2, p, q):
    def trans(s,p):
        base = ''
        while s > 0:
            s, mod = divmod(s ,p)
            base += str(mod)
        return base[::-1]
 
    def add(a,b,p):
        i, j = int(a,p), int(b,p)
        return trans(i + j,q)

    answer = add(trans(int(s1,p),q), trans(int(s2,p),q), q)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "112001"
s2 = "12010"
p = 3
q = 8
ret = solution(s1, s2, p, q)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
print(time.time()-start)