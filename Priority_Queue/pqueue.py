class Pqueue:
    def _init_(self):
        self.data = [None]
        self.size = 0
    #def my_cmp(a,b):

    def pushup(index):
        if (index == 0 or index == 1):
            return
        upIndex = (index - 1) / 2
        prev_val = data[upIndex]
        if (prev_val > data[index]):
            dummy = data[index]
            data[index] = data[upIndex]
            data[upIndex] = dummy
            pushup(upIndex)
            
    def push(item):
        data.append(item)
        size += 1
        pushup(size)
        return 0


    def pushdown(index):
        left_child = data[index * 2]
        right_child = data[index * 2 + 1]
        if data[index] > left_child and data[index] > right_child:
            return
        if data[index] < left_child and left_child >= right_child:
            dummy = data[index]
            data[index] = left_child
            data[index * 2] = dummy
            pushdown(index * 2)
        if data[index] > right_child and right_child > left_child:
            dummy = data[index]
            data[index] = right_child
            data[index * 2 + 1] = dummy
            pushdown(index * 2 + 1)
    def pop():
        size -= 1
        data.pop(1)
        data[1] = data[size]
        data.pop(size)
        pushdown(1)
        return 0
    
    def peek():
        if size == 0:
            return None
        ans = data[1]
        i = 1
        while i < size:
            ans = min(ans,data[i])
        return ans
        
            
    def tolist():
        if size == 0:
            return []
        
