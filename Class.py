help(dir)
class SomeClass:
    # use self.somevar statement for bind it to the class storage and make it a class variable accessible like this: classname.statement
    astring = "abc"
    anumber = 123    
    def Display(self):
        print(self.anumber)

obj = SomeClass()
obj.Display()



