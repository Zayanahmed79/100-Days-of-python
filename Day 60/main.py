class MyClass:
    def __init__(self, value):
        self._value = value
    def show(self):
        print(f"The value is: {self._value}")
    @property
    def ten_value(self):
        return self._value* 10
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10

    
obj = MyClass(10)
obj.ten_value = 13
print(obj.ten_value)
obj.show()

