class Array:

    def __init__(self,size):
        self.arr = ['*'] * size
        self.size = size

    def insert(self, value, position):
        newSize = self.size + 1
        tempArray = self.arr

        for i in range(self.arr):
            if(i < position):
                tempArray[i] = self.arr[i]
        
    





if __name__ == "__main__":
    print("hello")