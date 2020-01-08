
class Qunen_ls(object):
    def __init__(self):
        self.__list=[]

    def is_empty(self):
        return self.__list==[]

    def push(self,item):
        self.__list.append(item)

    def pop(self):
        if self.is_empty():
            return
        else:
            return self.__list.pop(0)
    

class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = Node

class Quene_Dic(object):
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__size = 0
    
    def is_empty(self):
        return self.__size == 0
    
    def push(self,item,index):
        #入头
        node_n = Node(item)
        if index == 0:
            self.__head = node_n
            self.__head.next = None
        elif index == self.__size - 1:
        #入尾
            node = self.get_Node(index-1)
            node.next = node_n
            self.__last = node_n
            self.__last.next = None
        else:
            if self.is_empty():
                return
            node = self.get_Node(index-1)
            node_next = node.next
            node.next = node_n
            node_n.next = node_next
        #中间
        self.__size = self.__size + 1

    def pop(self):
        node = self.__head
        self.__head = self.__head.next
        self.__size = self.__size - 1
        return node.item

    def get_Node(self,index):
        node = self.__head
        for i in range(index):
            node = node.next
        return node

quene_ls = Qunen_ls()
quene_dic = Quene_Dic()
ls = [1,34,5,25323,62,123,4124]

def test_quene_ls():
    for i in ls:
        quene_ls.push(i)

    print(quene_ls.pop())
    print(quene_ls.pop())
    print(quene_ls.pop())

def test_quene_dic():
    for i in range(len(ls)):
        quene_dic.push(ls[i],i)
    

    print(quene_dic.pop())
    print(quene_dic.pop())
    print(quene_dic.pop())
    print(quene_dic.pop())

def main():
    test_quene_ls()
    test_quene_dic()

if __name__=='__main__':
    main()