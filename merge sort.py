

def sort(x,length):
    length=length-1
    i=length
    if length>0:
        while i>0:
            i=i-1
            if x[i]>x[i+i]:
                x[i+1],x[i]=x[i],x[i+1]
        x=sort(x,length)
    return x   
#merge sort algorithm
# try block to handle the exception 
try: 
	list = [] 
	
	while True: 
		list.append(int(input())) 
		
# if input is not-integer, just print the list 
except: 
	print(list) 
n=len(list)
sort(list,n)
print('length is ',n)

    
