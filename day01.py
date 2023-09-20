num = 100
print('안녕: ', num)

li = [100, '안녕', 1.123]
print (li)
li.append("그래")
print(li)
print(li[0])

dic = {"키":"값"}
print(dic)
print(dic["키"])


# 들여쓰기 확인 잘하기
if num > 100:
    print(100, '보다 크다');
elif num <= 100:
    print('100과 같거나 작다');
    print('100과 같거나 작다');
    print('100과 같거나 작다');
    print('100과 같거나 작다');

for i in range(1, 10, 2):
    print(i)

# forEach
# for(자료형 s : Array)
# 개행없이 작성하고 싶으면 end="" 사용
li = [100, 200, 300]
for i in li:
    print(i, end="aaa") 

def test(n):
    print(n, 'test호출')
    return "리턴값"

result = test("안녕");
print(result)
    
