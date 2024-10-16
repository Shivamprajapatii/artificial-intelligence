def t(height, start, aux, end):
    if height>=1:
       
        t(height-1, start, end, aux)
        print("moving disk from", height, start, "to", end)
        
        t(height-1, aux, start, end)

t(3,"A","B","C")        
