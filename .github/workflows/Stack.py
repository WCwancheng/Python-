class Stack_ls(object):
    def __init__(self):
        self.__list = []

    def is_empty(self):
        return self.__list==[]
    
    def push(self,item):
        self.__list.append(item)

    def pop(self):
        if self.is_empty():
            return 
        else:
            return self.__list.pop()

    def top(self):
        if self.is_empty():
            return
        else:
            return self.__list[-1]

class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.next = None

class Stack_Dic(object):
    def __init__(self):
        self.__head = None
    
    def is_empty(self):
        return self.__head is None

    def push(self,item):
        node = Node(item)
        node.next = self.__head
        self.__head = None
    
    def pop(self):
        if self.is_empty():
            return
        else:
            p = self.__head
            self.__head = p.next
            return p.elem


stack_ls = Stack_ls()
ls = [1,34,5,25323,62,123,4124]
def test_stack_ls():
    for i in ls:
        stack_ls.push(i)

    ls_2 = []
    while not stack_ls.is_empty():
        ls_2.append(stack_ls.pop())

    print(ls_2)

stack_dic = Stack_Dic()
def test_stack_dic():
    for i in ls:
        stack_dic.push(i)
    
    ls_3 = []
    while not stack_dic.is_empty():
        ls_3.append(stack_dic.pop())
    
    print(ls_3)

def main():
    test_stack_ls()

if __name__=='__main__':
    main()