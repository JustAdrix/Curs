'''
Context Manage = Un concept care ne permite sa gestionam accesul la diverse resurse prin apelarea automata a doua
functii la intrarea si iesirea din context
In python



with context_manager() as variabila:
        # fa ceva cu variabila care rezulta din manager
    aici nu vom mai avea acces la variabila deoarece s-a inchis aceasta resursa



'''

with open('test_file.txt', 'r') as f: # r = read
    print(f.readline())
# print(f.readline()) # fisierul a fost inchis in acest punc si nu mai avem aces la el
'''
Ca sa definim propriul .....
'''
class FileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None
    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
with FileManager('test_file.txt', 'r') as f:
    print(f.readline())

class HelloContext_Manager:
    def __enter__(self):
        print('intram in context')
        return 'Hello Word'
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Leaving the context')
        if exc_type == IndexError:
            print(f'Eception type{exc_type}')
            print(f'Eception message{exc_val}')
        return True
with HelloContext_Manager() as hello:
    print(hello)
    hello[100]


from contextlib import contextmanager

@contextmanager
def file_manager(file_name, mode):
    f = open(file_name, mode)
    yield f
    f.close()
with file_manager('test_file.txt', 'r') as f:
    print(f.readline())

# x = ([1, 2],)
#
# try:
#     x[0] += [3, 4]
# except Exception as e:
#     print(e)
#     print(x)
