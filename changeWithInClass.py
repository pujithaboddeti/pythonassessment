class changeWithInClass():
    count=0
    def change(self):
        self.count+=1
    def display(self):
        print(self.count)
obj=changeWithInClass()
obj.change()
obj.change()
obj.display()
        