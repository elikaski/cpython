import dis
# works on both Python 3.7 and 3.11
def patch_function(func, old_instruction, new_instruction):
    import sys
    from ctypes import memmove
    assert len(old_instruction) == len(new_instruction)
    code = func.__code__
    if sys.version_info >= (3, 11):
        new_bytecode = code._co_code_adaptive.replace(old_instruction, new_instruction)
        # find offset to _co_code_adaptive
        size = 0x100
        code_object_bytes = b"\x00" * size
        memmove(code_object_bytes, id(code), size)
        co_code_adaptive_offset = code_object_bytes.index(code._co_code_adaptive)
        memmove(id(code) + co_code_adaptive_offset, new_bytecode, len(new_bytecode))
    if sys.version_info >= (3, 0):
        new_bytecode = code.co_code.replace(old_instruction, new_instruction)
        memmove(code.co_code, new_bytecode, len(new_bytecode))
    else:
        raise Exception("unsupported python version for patching function (for now...)")

OP_ADD = b"\x00"
OP_SUB = b"\x0A"

def foo(x):
    return x + 1

# replace ADD with SUB
# making foo become "return x - 1"

old_instruction = dis.opmap["BINARY_OP"].to_bytes() + OP_ADD
new_instruction = dis.opmap["BINARY_OP"].to_bytes() + OP_SUB
print("before: foo(5) =", foo(5))
patch_function(foo, old_instruction, new_instruction)
print("after : foo(5) =", foo(5))
