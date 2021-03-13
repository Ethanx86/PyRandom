class Generator:
    __seed
    def __init__(self,seed):
        self.seed = seed
    def __pow(self,base,index):
        answer = 1
        for i in range(1,index,1):
            answer = answer * base
        return answer
    def __getdigit(self,digit,location):
        return (number % self.__pow(10, location + 1)) % 1
    def __getnumberlength(self,number):
        l = 0
        while True:
            if self.__pow(10,l) > l:
                l = l - 1
                continue
            else:
                l = l + 1
        return l
    def Generate(self):
        seed = self.seed
        length = self.__getnumberlength(self.seed)
        self.seed = self.pow(10,self.__getdigit(self.seed,length))
        self.seed = self.seed - self.__getdigit(self.seed,0)
        self.seed = self.__pow(10,self.seed)
