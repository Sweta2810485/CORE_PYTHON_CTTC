# for i in range(1,5,1):
#     for j in range(1,i+1,1):
#         print(j, end="\t")
#     print()

# #



# for i in range(4,0,-1):
#     for j in range(4,i-1,-1):
#         print(j, end="\t")
#     print()


# for i in range(1,5,1):
#     for j in range(4,i-1,-1):
#         print(j, end="\t")
#     print()

# for i in range(1,5,1):
#     for j in range(i,0,-1):
#         print(j, end="\t")
#     print()


# for i in range(4,0,-1):
#     for j in range(i,5,1):
#         print(j, end="\t")
#     print()

# class demo:
#     def __init__(self):
#         print("Constructor")
#     def __del__(self):
#         print("Destructor")
# d = demo()
# d1 = demo()
# d2=demo()



class demo:
    def __init__(self):
        self.a=10
        self.b=20
    def show(self):
        print(self.a,self.b)
