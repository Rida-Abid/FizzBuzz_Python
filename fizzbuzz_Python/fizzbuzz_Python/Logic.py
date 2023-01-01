class logic: 
    def process ( fizzId, buzzId, maxCount):
        result = []
        pros = logic()
        if (maxCount < 1) or (fizzId < 1) or (buzzId < 1):
            result.append("Please enter all values greater than 0")
            return result
       
        for i in range(1, maxCount):
    
            result.append(pros.calculation(i, fizzId, buzzId))
          
        return result

    
    def calculation(self, i, fizzId, buzzId):
         if (fizzId == 0) or (buzzId == 0):
            return "0"
         if (i % fizzId == 0) and (i % buzzId == 0):
            return "fizzbuzz"
         elif (i % fizzId == 0):
            return "fizz"
         elif (i % buzzId == 0):
            return "buzz"
         else: 
            return str(i)
 
    

   
