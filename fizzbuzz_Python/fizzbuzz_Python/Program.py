import sys
from Logic import logic

class Program:
    
    fizzId, buzzId, maxCount = map (int,input("Enter fizzId, buzzId, maxCount").split())
    

    if len(sys.argv) <3:
        print("Enter 3 values")
    
    else:
        results = logic.process( fizzId, buzzId, maxCount )
        for result in results:
    
            print (result)
        
          

    