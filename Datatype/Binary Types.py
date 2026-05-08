#Binary Types: bytes, bytearray, memoryview
#bytes
x=b"Hello World"
print(x)
print(type(x))
#bytearray
y= bytearray(5)
print(y)
print(type(y)) 
#memoryview
z = memoryview(bytes(5))
print(z)
print(type(z)) 

#or
x = bytes("Hello World", "utf-8")
print(x)
print(type(x))
y = bytearray("Hello World", "utf-8")
print(y)
print(type(y))
z = memoryview(bytes("Hello World", "utf-8"))
print(z)
print(type(z))
