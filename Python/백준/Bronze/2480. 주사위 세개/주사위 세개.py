num1,num2,num3 = map(int,input().split())


#모두 같은 숫자일 경우
if (num1+num2+num3) / 3 == num1 :
    money = 10000 + num1*1000
    print(f"{money}")
   #두개의 숫자만 같을 경우
elif num1 == num3 or num1 == num2:
    money = 1000 + num1 *100
    print(f"{money}")
elif num1 == num2 or num2 == num3:
    money = 1000 + num2 *100
    print(f"{money}")
elif num1 == num3 or num3 == num2:
    money = 1000 + num3 *100
    print(f"{money}") 
else: #모두가 다른 숫자일 경우
    if num1 > num2 and num1 > num3:
        money = num1 * 100
        print(f"{money}")
    elif num2 > num3 and num2 > num1:
        money = num2 * 100
        print(f"{money}")
    else:
        money = num3 * 100
        print(f"{money}")
        
    