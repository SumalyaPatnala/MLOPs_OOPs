# initiate a class
class employee:
    # special method/magic method /dunder method - constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "MLE"
        print("attributes/data have been initiated")

    def travel(self, destination):
        print("This travel function was called manually")
        print(f"Employee is now travelling to {destination}")



# create as obj/instance of the class
sam = employee()
# print(sam.id)
# sam.travel("Sunnyvale, CA")
print(type(sam))

