# The variable type is only for purpose of typing — Support for type hints
# Python doesn't enforce the variable type so it will go ahead and execute it and throw exception if necessary

class TestClass1():
    def __init__(self):
        self._data = 1;
    pass

class TestClass2():
    def __init__(self):
        self._data = 2;

    def value2(self):
        return self._data

    pass

class TestClass3():
    def value():
        return 1;

    pass


def doit(inputs, enabled):
    """Do something with those inputs

    Args:
        inputs (Union[str, List[str]]):  input names
        enabled (Dict[str, bool]):  mapping of input names to
            enabled status

    Returns:
        Iterable[str]: enabled inputs
    """
    pass

def afunction(a:TestClass1, b:TestClass2)->TestClass3:
    return a._data + b.value2();

def testPython3():
    a = TestClass1();
    b = TestClass2();
    print(afunction(a, b));
    print (afunction (b, a));
    doit(None, None)