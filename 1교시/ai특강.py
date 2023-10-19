# -*- coding: utf-8 -*-
"""AI특강

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xMHqA6-fGDS_47gjJ3-2iu0QvPJ3Bcur
"""

##1교시
import random

# 숫자 랜덤으로 선택
number = random.randint(1, 100)

# 사용자로부터 숫자 입력 받기
guess = int(input("1부터 100 사이의 숫자를 맞춰보세요: "))

# 추측한 숫자와 실제 숫자를 비교하면서 반복
while guess != number:
    if guess < number:
        print("좀 더 큰 수를 입력하세요.")
    else:
        print("좀 더 작은 수를 입력하세요.")
    guess = int(input("다시 시도해보세요: "))

# 정답 메시지 출력
print("정답입니다! 숫자 {}를 맞췄습니다.".format(number))