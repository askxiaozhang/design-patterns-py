from typing import Union, List

import os
import numpy as np

import abc  # Abstract Base Class


class IModel(metaclass=abc.ABCMeta):  # 定义一个抽象类 #IUser 是一种命名约定，通常表示 "Interface for User"（用户接口）。在软件工程中，这种命名惯例经常用于表示一个接口，而不是具体的实现类
    # __metaclass__ = abc.ABCMeta # __metaclass__ 的方式是 Python 2 中的语法，而在 Python 3 中，它已经被废弃，不再推荐使用
    '''
    具体来说，__metaclass__ = abc.ABCMeta
    的作用是将
    IUser
    类指定为抽象基类，并使用
    ABCMeta
    作为其元类。
    这样一来，IUser
    就成为一个抽象类，而不能被直接实例化。子类必须提供抽象方法的实现，否则会在实例化时引发
    TypeError。
    这是一种在设计中强制规定接口实现的机制，以确保派生类符合指定的接口约定。
    '''

    @staticmethod
    def read_image(self, image_path: str) -> np.ndarray:
        pass

    @abc.abstractmethod
    def process(self, image: Union[str, np.ndarray]) -> np.ndarray:
        raise NotImplementedError

    @abc.abstractmethod
    def process_batch(self, images: List[Union[str, np.ndarray]]) -> List[np.ndarray]:
        raise NotImplementedError

class TestModel(IModel):
    def __init__(self):
        pass

    def process(self, image: Union[str, np.ndarray]) -> np.ndarray:
        print("process")

    def process_batch(self, images: List[Union[str, np.ndarray]]) -> List[np.ndarray]:
        print("process_batch")

    @staticmethod
    def read_image(self, image_path: str) -> np.ndarray:
        print("read_image")



'''访问权限
访问权限（public、private、protected）主要通过命名约定来体现，而不是通过关键字直接指定。
Python并没有像其他一些编程语言（如Java、C++）那样提供严格的访问控制修饰符。

1 Public（公有）：公有成员可以在任何地方被访问。
# 在类的方法或属性前不加任何修饰符，即默认为公有。
class MyClass:
    def public_method(self):
        print("This is a public method.")

    public_attribute = "This is a public attribute."

2 Private（私有）：私有成员只能在类内部被访问，不能在类外部被访问。
# 用双下划线（__）表示私有成员。
class MyClass:
    def __private_method(self):
        print("This is a private method.")

    __private_attribute = "This is a private attribute."

3 Protected（受保护）：受保护成员可以在类内部和子类中被访问，不能在类外部被访问。
# 用单下划线（_）表示受保护成员。
class MyClass:
    def _protected_method(self):
        print("This is a protected method.")

    _protected_attribute = "This is a protected attribute."
'''

if __name__ == "__main__":
    #test = IModel() # 会报错 抽象类无法被实例化
    test2 = TestModel()