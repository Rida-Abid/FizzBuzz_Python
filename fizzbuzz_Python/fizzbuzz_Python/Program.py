from Logic import logic

class Program:

    fizzId, buzzId, maxCount = map (int,input("Enter fizzId, buzzId, maxCount").split())
    
    #if input!=3:
    # print("Enter 3 values")
    
    results = logic.process(self, fizzId, buzzId, maxCount )
    for result in results:
    
      print (result)   

    