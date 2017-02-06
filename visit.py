import commons

def run():
	inp = input('请输入您访问页面的url：').strip()
	modules, func = inp.split('/')
	obj = __import__(modules)
	if hasattr(obj, func):
		func = getattr(obj, func)
		func()
	else:
		print('404')


if __name__ == '__main__':
	run()

