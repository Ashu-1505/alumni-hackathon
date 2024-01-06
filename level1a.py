import json
#Data
f = open('Input data/level1a.json')
data = json.load(f)
route=[]
food=[]
nd=[0]
nd=nd+(data['restaurants']['r0']['neighbourhood_distance'])
route.append(nd)
j=1
for i in data['neighbourhoods']:
    te=[nd[j]]
    te=te+(data['neighbourhoods'][i]['distances'])
    route.append(te)
    food.append(data['neighbourhoods'][i]['order_quantity'])
    j+=1
#[print(x, len(x)) for x in route]
#print(food)

cap=data['vehicles']['v0']['capacity']
#print(cap)

######################################################################################################

def knapsack(wt, val, W, n): 
  
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]
             
    # Build table K[][] in bottom
    # up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] 
                  + K[i - 1][w - wt[i - 1]],
                               K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
 
    # stores the result of Knapsack
    res = K[n][W]
     
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
 
            # This item is included.
            si.append(i-1)
             
            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]

#####################################################################################################

res=[]
profit=[]
for i in range(1,21):
    a=route[i]
    a.pop(i)
    profit.append(min(a))

a,b=food,profit
print(a,b,"\n\n")
'''while len(b)>0:
    s=[]
    si=[]
    n = len(b)
    knapsack(a, b, cap, n)
    res.append(si)
    for i in si:
        del a[i]
        del b[i]
    print(a,b)'''

while len(b) > 0:
    # Use the knapsack function to find the optimal selection
    selected_indices = knapsack(a, b, cap, len(b))
    res.append(selected_indices)
    
    # Create new lists without modifying the existing ones
    a = [a[i] for i in range(len(a)) if i not in selected_indices]
    b = [b[i] for i in range(len(b)) if i not in selected_indices]

    print("Remaining Order Quantities:", a)
    print("Remaining Minimum Distances:", b, "\n")

print(res)
    
    


    