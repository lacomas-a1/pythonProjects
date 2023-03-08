class customer:
    def __init__(self,name,membership_type):
        self.name =name
        self.membership_type =membership_type

c = customer("caleb", "gold")
print(c.name, c.membership_type)
c2 = customer("bead", "bronze")
print(c2.name , c2.membership_type)

customers  = [customer("caleb", "gold"),customer("bead", "bronze")]
print(customers[0].name)