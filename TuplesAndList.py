

def main():
    #string
    Data="software engineer"
    print(Data[0:5])
    #List
    Ages=[44,33,45,33,54]
    Ages.append(100)
    Ages.insert(0,33)
    Ages.pop()
    Ages.pop(2)
    Ages.remove(44)
    print(Ages)
    print(sum(Ages))
    print(Ages[:2])
    #Tuples
    Ages=[44,33,45,33,54]
    Ages.append(100)
    Ages.insert(0,33)
    print(Ages)
    



if __name__ == '__main__':main()
