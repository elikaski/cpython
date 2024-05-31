import dis
def foo(x):
    return x + 1

def find_offset_to_adaptive_bytecode(code_object):
    # copy entire code object into bytes variable
    size = 0x100
    code_object_bytes = b"\x00" * size
    memmove(code_object_bytes, id(code_object), size)
    # search _co_code_adaptive index in the bytes variable
    return code_object_bytes.index(code_object._co_code_adaptive)

# replace ADD with SUBTRACT
# making foo become "return x - 1"

dis.dis(foo, adaptive=True)
print("foo(5) =", foo(5))
OP_ADD = b"\x00"
OP_SUB = b"\x0A"
old_instruction = dis.opmap["BINARY_OP"].to_bytes() + OP_ADD
new_instruction = dis.opmap["BINARY_OP"].to_bytes() + OP_SUB
bytecode = foo.__code__._co_code_adaptive
new_bytecode = bytecode.replace(old_instruction, new_instruction)
print("before :", bytecode)
print("after :", new_bytecode)
from ctypes import memmove
assert len(bytecode) == len(new_bytecode)
offset = find_offset_to_adaptive_bytecode(foo.__code__)
memmove(id(foo.__code__) + offset, new_bytecode, len(bytecode))
print("new _co_code_adaptive:", foo.__code__._co_code_adaptive)
dis.dis(foo, adaptive=True)
print("foo(5) =", foo(5))
