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


def foo(a, b):
    return 2 * a + b

# replace LOAD_FAST 0 with LOAD_FAST 1
# making foo become "return b * b + b"


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


def foo(a, b):
    return 2 * a + b

# replace LOAD_CONST 1 with LOAD_FAST 0
# making foo become "return a * a + b"

old_instruction = dis.opmap["LOAD_CONST"].to_bytes(1, byteorder="little") + b"\x01" # constant 2
new_instruction = dis.opmap["LOAD_FAST"].to_bytes(1, byteorder="little") + b"\x00" # variable a
print("before: foo(1, 2) =", foo(1, 2))
patch_function(foo, old_instruction, new_instruction)
print("after: foo(1, 2) =", foo(1, 2))
