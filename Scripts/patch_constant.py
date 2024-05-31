def patch_function_constant(func, old_value, new_value):
    from ctypes import memmove
    consts = index = func.__code__.co_consts
    index = consts.index(old_value)
    memmove(id(consts) + 0x18 + index * 8, id(new_value).to_bytes(8, "little"), 8)

def foo(a, b):
    return 2 * a + b

# replace constant 2 with constant 3
# making foo become "return 3 * a + b"

print("before: foo(1, 2) =", foo(1, 2))
patch_function_constant(foo, 2, 3)
print("after: foo(1, 2) =", foo(1, 2))
