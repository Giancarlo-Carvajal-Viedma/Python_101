# try
# except
# else
# finally
# raise
# assert
# custom exceptions

class ToLowNumberValueError(Exception):
    msg: str

    def __init__(self, msg):
        self.msg = msg


def do_somethin(a):
    res = int(a)
    if res <2:
        raise ToLowNumberValueError("The number is to low")
    return res


try:
    print("Trying")
    assert 2==2
    print(do_somethin(1))

except AssertionError:
    print("AssertionError")
except ValueError:
    print("ValueError")
except SyntaxError as e:
    print("Syntaxerror", e.msg)
except ToLowNumberValueError as e:
    print(e.msg)
except:
    print("Catch em all")
else:
    print("OK")
finally:
    print("I will always be with you")

do_somethin(1)