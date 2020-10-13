while True:
    
        print('How many cats do you want?')
        try:
            total = int(input())
            count = 0
            while count < total:
                print('cat')
                count = count + 1
            print('Hope you can feed them all')
            print('Would you like to continue?')
            useranswer = input()

            if useranswer==('y' or 'yes' or 'YES' or 'Yes' or 'yeS'):
                print('All the cats are belong to you')
                continue
            elif useranswer== ("n" or 'no' or 'NO' or 'No' or 'nO'):
                print('No more cats for you')
                break
            
                
             
        except ValueError:
            print("Uno Dos Tres..Also note cats only come in whole..This isnt china")
    
        

      
   

