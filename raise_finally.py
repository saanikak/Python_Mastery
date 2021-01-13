#Google python's built in exceptions
#User defined exception

class Accident(Exception):

    def __init__(self, msg):
        self.message = msg

    def print_exception(self):
        print("User defined exception", self.message)


try:
    raise Accident('crash between 2 cars')
except Accident as e:
    e.print_exception()
finally:
    print('cleans up the code...finally')


# try:
#     raise MemoryError('Memory Exception in try block')
# except Exception as e:
#     print(e)

