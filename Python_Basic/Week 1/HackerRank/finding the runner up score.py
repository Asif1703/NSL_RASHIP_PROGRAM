if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())[:n]
    i=0; 
    x=max(arr)
    
    while True:
        if i<n:
            if arr[i]!=x:
                i+=1
            else:
                arr.remove(x)
                
                n-=1
                
                i-=1
               
                if i<0:
                    i+=1
                
                
        else:
            break
    print(max(arr))    

        
            
       


    


