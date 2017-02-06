#参数组合顺序 必选参数、可选参数、可变参数、命名关键字参数、关键字参数
def func(a, b = 0, *args, c, **kw):
	print(a, b, args, c, kw)


#对于任意函数都可以被调用
def func(*args, **kw)