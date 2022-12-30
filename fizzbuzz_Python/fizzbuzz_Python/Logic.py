class logic: 
    def calculation(self, i, fizzId, buzzId):
         if (i % fizzId == 0) and (i % buzzId == 0):
            return "fizzbuzz"
         elif (i % fizzId == 0):
            return "fizz"
         elif (i % buzzId == 0):
            return "buzz"
         else: 
            return str(i)
 
    def process(self, fizzId, buzzId, maxCount):
        result = []
        for i in range(maxCount):
    
            result.append(self.calculation(i, fizzId, buzzId))
          
        return result

   
