def makeBold(fn):
    print("BBBBB" * 5)

    def wrapped():
        print("bbbbb" * 5)
        return "<b>" + fn() + "</b>"

    return wrapped


def makeItalic(fn):
    print("IIIII" * 5)

    def wrapped():
        print("iiiiii" * 5)
        return "<i>" + fn() + "</i>"

    return wrapped


# 2.装饰器的使用，直接@加上函数名的形式，放到需要装饰的函数头上即可。
@makeBold  # 效果等同于test_Bold=makeBold(test_Bold)，装饰器放在一个函数上，相当于将这个函数当成参数传递给装饰函数
def test_Bold():
    print("test_Bold" * 5)
    return "this is the test_Bold"


@makeItalic  # 效果等同于test_Italic=makeItalic(test_Italic)，装饰器放在一个函数上，相当于将这个函数当成参数传递给装饰函数
def test_Italic():
    print("test_Itali" * 5)
    return "this is the test_Italic"
