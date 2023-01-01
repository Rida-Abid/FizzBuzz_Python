from Logic import logic

class Program:
    
    fizzId, buzzId, maxCount = map (int,input("Enter fizzId, buzzId, maxCount").split())
    

   # if (input == 3):
    results = logic.process( fizzId, buzzId, maxCount )
    for result in results:
    
        print (result)
    
    #else:
       # print("Enter 3 values")
          

    