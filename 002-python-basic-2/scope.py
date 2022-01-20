# Scope - what variables do I have access to?
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

_name = 'charles'
print(_name)

num = int(5)
print(num)
x = "hello"[0]
print(x)
