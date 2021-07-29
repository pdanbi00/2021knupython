# for문 무작정 따라해보기
for i in range(1, 11): # 1부터 11까지 도는거 아니고 한개 적게 돌아서 10번 도는 듯
    if (i%2 == 0):
        print(i, "은/는 짝수입니다.")
    else:
        print(i, "은/는 홀수입니다.")

# for문의 구조
# for i in 범위:
#     반복할 명령어1
#     반복할 명령어2
# (주석 여러 문장 잡아서 할때는 그 부분 블럭 잡고 ctrl + /)

# for문 with list
mylist = ['해달이', '사스미', '메기']
for i in mylist:
    print(i)
print("반복 끝")

# print list with range
print(list(range(10))) # start 기본값은 0
print(list(range(1,11))) # step 기본값은 1
print(list(range(1,20,3)))
print(list(range(20,0,-3)))

# for문 with range
for i in range(1,11):
    print(i, end=" ")
print('반복 끝')