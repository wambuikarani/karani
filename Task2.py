# A python programme that will grade students according to their marks using 
marks=int(input("input marks:"))
if marks >=0 and marks<=15:
    print("E")
elif marks>=16 and marks<=25:                         
    print("D-") 
elif marks>=26 and marks<=30:                         
    print("D")   
elif marks>=31 and marks<=35:                         
    print("D+") 
elif marks>=36 and marks<=45:                         
    print("C-") 
elif marks>=46 and marks<=55:                         
    print("C")  
elif marks>=56 and marks<=60:                         
    print("C+") 
elif marks>=61 and marks<=65:                         
    print("B-") 
elif marks>=66 and marks<=75:                         
    print("B")  
elif marks>=76 and marks<=80:                         
    print("B+")
elif marks>=81 and marks<=85:                         
    print("A-") 
elif marks>=86 and marks<=100:                         
    print("A")    
else:
    print("invalid marks")                                                  
           
       
