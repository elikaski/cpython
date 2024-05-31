import dis
def foo(a, b):
    return 2 * a + b

def find_offset_to_adaptive_bytecode(code_object):
    # copy entire code object into bytes variable
    size = 0x100
    code_object_bytes = b"\x00" * size
    memmove(code_object_bytes, id(code_object), size)
    # search _co_code_adaptive index in the bytes variable
    return code_object_bytes.index(code_object._co_code_adaptive)

# replace LOAD_FAST 0 with LOAD_FAST 1
# making foo become "return 2 * b + b"

print("before: foo(1, 2) =", foo(1, 2))
old_instruction = dis.opmap["LOAD_FAST"].to_bytes() + b"\x00" # index of a
new_instruction = dis.opmap["LOAD_FAST"].to_bytes() + b"\x01" # index of b
new_bytecode = foo.__code__._co_code_adaptive.replace(old_instruction, new_instruction)
from ctypes import memmove
offset = find_offset_to_adaptive_bytecode(foo.__code__)
memmove(id(foo.__code__) + offset, new_bytecode, len(new_bytecode))
print("after: foo(1, 2) =", foo(1, 2))
