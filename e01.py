# pip install pandas => cmd창에서 설치해주기

import pandas
# DataFrame : 2차원 배열
df = pandas.read_csv("1.pandas.csv")
print(df)


import pandas as pd

df = pd.read_csv("1.pandas.csv")
print(df)

# Series : 1차원 배열
# [ ] Series 형식으로 가져온다
print( df['name'] )
print( df.age )

# 여러개의 값을 가져오고자 하는 경우[[ ]]
# [[ ]] DataFrame 형식으로 가져온다
print( df[['name']])
print( df[['name', 'age']])

# 인덱싱 : 인덱스의 범위를 지정한다
print( df[1:3] )    # 1~2까지의 데이터
print( df[ :3] )     # 처음부터 ~2까지의 데이터
print( df[1: ] )     # 1~ 끝까지의 데이터

# loc : DF.loc[ index조건식, 컬럼 조건식 ]
print( df.loc[1:3 , 'name'] )   # 1~3까지의 name 데이터
print( df.loc[1:3 , ['name', 'score'] ] ) # 1~3까지의 name, score 데이터
print( df.loc[ :  , 'name' : 'grade'] ) #name ~ grade의 모든 데이터
print( df.loc[1:3, ] ) # 1~3까지의 모든 데이터

print( df['grade'] == 'A')  # True인지 False인지 출력
print( df[ df['grade'] == 'A' ])    #True에 대한 정보만 출력
