#로또 번호를 랜덤으로 뽑아주는 프로그램을 짜시오


import random


numbers = range(1,46)
#마치 [1,2,3,....,45] 과 비슷하다.
lotto = random.sample(numbers,6)
print(sorted(lotto))
