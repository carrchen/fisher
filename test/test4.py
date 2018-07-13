from werkzeug.local import LocalStack


s = LocalStack()
s.push(1)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)


s.push(1)
s.push(2)
# 栈 先进后出
print(s.top)
print(s.top)
print(s.pop())
print(s.top)
