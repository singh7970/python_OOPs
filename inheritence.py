# class employee:
#     def __init__(self,n,id):
#         self.name=n
#         self.id=id

#     def showdata(self):

#         print(f"employee nmae{self.name} and id {self.id}")

# class programmer(employee):
#     def showpro(self):
#         print(
#             "helo mu nam is"
#         )



# a=employee("alok",43)
# a.showdata()


class dog:
    def __init__(self,n,b):
        self.name=n
        self.color=b


    def showdata(self):
        print(f"Dog name is {self.name} and color is {self.color}")

class sound(dog):
    def __init__(self):
        print("hoooo")
        




a=dog("lebra","browen")


a.showdata()
c=sound()

























