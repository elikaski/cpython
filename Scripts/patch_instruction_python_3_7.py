import dis
def foo(x):
    return x + 1

# replace ADD with SUBTRACT
# making foo become "return x - 1"

dis.dis(foo)
print("foo(5) =", foo(5))
bytecode = foo.__code__.co_code
old_instruction = dis.opmap["BINARY_ADD"].to_bytes(1, "little")
new_instruction = dis.opmap["BINARY_SUBTRACT"].to_bytes(1, "little")
new_bytecode = bytecode.replace(old_instruction, new_instruction)
print("before:", bytecode)
print("after :", new_bytecode)
from ctypes import memmove
assert len(bytecode) == len(new_bytecode)
memmove(bytecode, new_bytecode, len(bytecode))
dis.dis(foo)
print("foo(5) =", foo(5))
