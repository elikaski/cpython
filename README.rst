Playing Around With Python
=============================================
This is a fork of the official `CPython project <https://github.com/python/cpython>`_.



Self Modifying Code Branch
--------------------------

Some Python scripts that show self-modifying code


.. image:: https://github.com/elikaski/cpython/blob/self_modifying_code/images/code_patch_instruction.PNG
   :alt: ADD to SUB

A code that replaces the ADD instruction with a SUB instruction


.. image:: https://github.com/elikaski/cpython/blob/self_modifying_code/images/code_patch_instruction_result.PNG
   :alt: ADD to SUB result

Result of running this script




.. image:: https://github.com/elikaski/cpython/blob/self_modifying_code/images/code_patch_constant.PNG
   :alt: 2 to 3

A code that replaces the constant 2 used in the function with the constant 3


.. image:: https://github.com/elikaski/cpython/blob/self_modifying_code/images/code_patch_constant_result.PNG
   :alt: 2 to 3 result

Result of running this script




More Examples
^^^^^^^^^^^^^

This branch contains the following scripts:


- Patch instruction (Python 3.7)
- Patch instruction (Python 3.11)
- Patch constant
- Replace constant with variable
- Patch instruction arg (python 3.11)
- Patch instruction arg (python 3.7 + 3.11)

