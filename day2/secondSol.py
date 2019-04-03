import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False

sr = pd.Series()
def printMenu():
    print('제품수량관리')
    print('-'*10)
    print('1.입력','2.출력','3.검색','4.정렬(제품명기준)',
          '5.차트보기(바차트)','6.종료', sep='\n')
def inFn():
    while True :
        print('1.입력')
        p = input('제품명:')
        c = int(input('수량:'))
        sr[p] = c
        if (input('계속입력(y/n)') != 'y'):
            break

def outFn():
    print('2.출력')
    print('%10s%10s'%('제품명', '수량'))
    for n, s in sr.items():
        print('%10s%10d'%(n, s))

def searchFn():
    print('3.검색')
    s = input('검색제품명입력')
    print('%10s%10s'%('제품명', '수량'))
    print('%10s%10d'%(s, sr[s]) )

def sortFn():
    print('4.정렬결과출력')
    print('%10s%10s'%('제품명', '수량'))
    for n, s in sr.sort_index().items():
        print('%10s%10d'%(n, s))

def chartFn():
    print('5.차트출력')
    sr.plot(kind='bar')
    plt.show()

def errMenu():
    print('1~6번중 선택하세요')
    
d={1:inFn, 2:outFn, 3:searchFn, 4:sortFn, 5:chartFn,6:exit}
def mainFun():
    while True :
        printMenu()
        m = int(input('메뉴를 선택하세요'))
        d.get(m, errMenu)()

mainFun()
