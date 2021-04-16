'''
简单装饰器:
    实现装饰后函数的功能是如果x和y相乘为负数，则返回0
'''

def check_result(func):
    '''hahah'''
    def wrapper(*args, **kwargs):
        '''this is wrapper'''
        result = func(*args, **kwargs)

        if result < 0:
            return 0
        else:
            return result
    return wrapper



def foo(x, y):
    '''this is foo'''
    return x * y
print((check_result(foo)(10,2)))

# 装饰过程拆解
# wrapper = check_result(foo)
# foo = wrapper