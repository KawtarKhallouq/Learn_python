def occurrece(n):
    T=[1,8,3,6,9,8,0,2,1,7,0,1,2,8,3,0,9,7,4,6]
    occ=0
    for i in T:
        if n==i:
            occ+=1
        
    
    return occ


#print(occurrece(1)) # affiche 4
#print(occurrece(8)) # affiche 3
#print(occurrece(7)) # affiche 2
#print(occurrece(9)) # affiche 2
#print(occurrece(0)) # affiche 3
            
  
  
def occurrence_dc(arr, target):
    if not arr:  # Base case: empty list
        return 0

    mid = len(arr) // 2
    left_count = occurrence_dc(arr[:mid], target)  # Count occurrences in left half
    right_count = occurrence_dc(arr[mid + 1:], target)  # Count occurrences in right half

    mid_count = 1 if arr[mid] == target else 0  # Check occurrence in the current mid element

    return left_count + right_count + mid_count
  
  
          
def TriOccurrence(n):
    T=[1,1,1,1,1,3,3,3,3,3,3,6,6,6,6,6,6,8,8,8,8,9,9,9,9,9,9,9,9]
    occ=0
    start=0 
    end=0
    for i in range(0,len(T)+1):
        if T[i]==n:
            start=i
            break
    if start == 0: # If the number 'n' does not exist in the array 'T', we return 0
        return 0
    for j in range(start+1,len(T)+1):
        if T[j-1]!=n:
            end=j-1
            break
        
    return end-start    

print(TriOccurrence(1)) # Output: 5
print(TriOccurrence(3)) # Output: 5
print(TriOccurrence(6)) # Output: 6
print(TriOccurrence(8)) # Output: 5
print(TriOccurrence(9)) # Output: 8    
        
        
    
