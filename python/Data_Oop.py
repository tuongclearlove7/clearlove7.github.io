class MyQuery():
    def MyData():
        print("\n\nWELCOME Function MyData !")
        class Main():
            def __init__(self,name, nickname):
                self.myname = "cl7\ntoi "+name
                self.mynickname = nickname
            def Hi(self):
                return "Hi! "+self.myname
                
        log = Main("yeu thao","toilaclearlove7")# gán class main() cho log
        # "yeu thao" được gán cho name và name gán cho self.myname
        # "toilaclearlove7" được gán cho nickname và nickname gán cho selfmynickname 
        print(log)# print class
        print("toi la  "+log.myname,
            "\ntoi la "+log.mynickname)# class main() được gán cho log và  in ra log.myname , log.mynickname
        # thuộc tính (attribute) name 
        print(Main.Hi(log))
        print(log.Hi)

        class Class_Method():
            def __init__(self,value,value2) -> None:
                self.method = value
                self.method2 = value2
        console = Class_Method("this is method 1 : "+log.Hi()+"\nthis is method 2 :"," hello --  ")
        print(console.method,console.method2)
        # tương tự class ở trên nhưng class này có sự khác biệt đó là  
        #  gán class log.main() được khởi tạo ở trên cho value và value gán cho method

        def SUM(a,b):
            #print("hello world !")
            c = a+b
            return c
        total = SUM(a=16,b=9)
        print(total) 

def Paint():
    print("\n\nWELCOME Function Paint ! ")
    print("Module : ",__name__)
    print(type(exit))
def Hacker():
    print("\n\nWELCOME Function Hacker !")
    Tolist = []
    Anonymous = lambda pass1,pass2,pass3 :pass1+pass2+pass3 
    print(Anonymous("tuongyeuthao\n", "tuongyeuthao1\n" ,"tuongyeubame"))
#MyQuery.MyData()
def Welcome():
    MyQuery.MyData()
    Paint()
    Hacker()

if __name__ == "__main__":
    Welcome()


class private_App:

    def app():

        data = [] # private data

        def set(*value):

            data.append(value)

        def get(index):

            return data[index]
        
        def gets():

            index = 0

            for i in data[index]:

                print(i)

        def edit_dict(index,key,value):
            
            data[index][index][key] = value

        set({"me" : "","crush" : ""},{},dict(),[])
        print(get(0))
        edit_dict(0,"me","tuong")
        edit_dict(0,"crush","thao")
        print(get(0))
        gets()
        
        for i in get(0)[0]:

            print(get(0)[0][i])

def main():

    private_App.app()

main()







