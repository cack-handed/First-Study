import numpy

# 随机数
# maxNumber是随机数的最大值  
def randomNumber(maxNumber):
    #10是自行设置的，默认生成随机数的数量
    print(numpy.sort(numpy.random.rand(10)*maxNumber//1))

def shuiXianHua():
    '''
    水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）
    '''
    print(list(filter((lambda n : n==(n%10)**3+(n//10%10)**3+(n//100%10)**3),list(i for i in range(100,1000)))))
 
def primary(n):
    for i in range(2,n):
        if n/i==n//i:
            return False
    return True
    
if __name__=="__main__":    
    #randomNumber(100)

    #shuiXianHua()

    print(primary(55))


