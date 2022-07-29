def seq_search(a, key):
    count = i = 0
    
    while True:
        count+= 1
        if i == len(a):
            return count + 1
        count += 1
        if a[i] == key:
            return count + 1
        i += 1
        
        
def seq_search_sentinel(b, key):
    a = list(b)
    a.append(key)
    
    count = i = 0
    
    while True:
        count += 1
        if a[i] == key:
            break
        i += 1
        
    if i == len(b):
        return count + 1
    else:
        return count + 1

a = [2,5,1,3,9,6,7]
key = 7

print(seq_search(a, key))
print(seq_search_sentinel(a,key))