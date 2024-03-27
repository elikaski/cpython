Playing Around With Python
=============================================
This is a fork of the official `CPython project <https://github.com/python/cpython>`_.



Collatz Branch
---------------

Introducing a brand new Bytecode instruction - UNARY_COLLATZ

Which can be compiled to using the $ operator

.. image:: https://github.com/elikaski/cpython/blob/collatz/images/dis.PNG
   :alt: Example Bytecode



It calculates the Collatz function of a number


.. image:: https://github.com/elikaski/cpython/blob/collatz/images/collatz_function.PNG
   :alt: Collatz Function



Any class can implement the __collatz__ magic method


.. image:: https://github.com/elikaski/cpython/blob/collatz/images/example.PNG
   :alt: ChatGPT




How to run
^^^^^^^^^^

In order to run the interpreter simply run python.exe.

If copied elsewhere, it requires to have python313.dll and the Lib directory in the same directory as python.exe.

To make changes and compile, refer to the original `CPython project <https://github.com/python/cpython>`_.
