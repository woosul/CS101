# 1부터 입력되는 숫자까지의 합을 구하는 모듈로 입력되는 값은 양의 정수
def calculate_sum(n) :
    if n <= 0:
        return 0
    else:
        return (n * (n + 1)) // 2

# calculate_sum()함수를 테스트하는 코드
def test_calculate_sum() :
    assert calculate_sum(10) == 55
    assert calculate_sum(100) == 5050
    assert calculate_sum(1000) == 500500
    print("테스트 통과!")

# calculate_sum()함수에 외부입력값을 전달하고 그 결과를 출력하는 코드
def main():
    n = int(input("숫자를 입력하세요 : "))
    print(calculate_sum(n))

if __name__ == "__main__" :
    test_calculate_sum()
    main()


    

    
    
