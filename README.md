# Example Python Project

Notes on how to setup modules and packages in Python.

## Python Modules

From the [docs](https://docs.python.org/3/tutorial/modules.html):


> A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended

Also of note

-  Within a module, the module’s name (as a string) is available as the value of the global variable `__name__`.
- When using `import`:
  - The directory from which the input script was run or the current directory if the interpreter is being run interactively
  - The list of directories contained in the [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH) environment variable, if it is set.
- Using `sys.path` from `import sys` shows where the intpreter is trying to resolve imports from  
- Using `sys.path.append` can add a new path to resolve an import from at runtime
- After a module has been imported, e.g. `import mod_a`, using `mod_a.__file__` returns the path of where the module was loaded from
- Using `dir()` will return a list of alphabetically sorted list of names in the current **local symbol table** - this can be useful for identifying what exactly has been added to the namespace by an `import` statement

### Examples of imports


Just using `import`:

```python
import mod_a

classA = mod_a.classA("Jean Baudrillard")
classA.sayHello() # Prints "Hi! My Name Is Jean Baudrillard!"
```

Using `from` and `import`:

```python
from mod_a import adder, composeAll, logger

listOfAdders = composeAll([
    adder(2),
    adder(4),
    adder(6),
    adder(8),
    logger()
])

listOfAdders(10) # Prints "30"
```

Using `from`, `import` and `as`:

```python
from mod_a import ClassA as MyClass

myClass = MyClass("Paul Gilbert")
myClass.sayHello() # Prints "Hi! My Name Paul Gilbert!"
```

Using `import` and `as`:

```python
import mod_b as fnLib

printAdder = lambda x : fnLib.composeAll([
    adder(x), logger()
])

add5 = printAdder(5)
add5(10); # Print 15
```

## Python Packages

From the [docs](https://docs.python.org/3/tutorial/modules.html#packages):

> Packages are a way of structuring Python’s module namespace by using “dotted module names

Also of note:

- When importing the package, Python searches through the directories on sys.path looking for the package subdirectory.
- The `__init__.py` files are required to make Python treat directories containing the file as packages.

## pip

From the [docs](https://pip.pypa.io/en/stable/reference/requirements-file-format/):

> Requirements files serve as a list of items to be installed by pip, when using pip install. Files that use this format are often called “pip requirements.txt files”, since requirements.txt is usually what these files are named (although, that is not a requirement).

Example _requirements.txt_ file:

```
numpy==1.21.2
scipy==1.7.3
matplotlib==3.4.3

```

To install:

```python
pip install -r requirements.txt
```

## References

- [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/)
- [Learn Python in X Minutes](https://learnxinyminutes.com/docs/python/)
- [The import system](https://docs.python.org/3/reference/import.html)
