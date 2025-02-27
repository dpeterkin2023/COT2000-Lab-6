Introduction to Sets in Python
my_set = {333, 22, 1}   
print(my_set)              

{7, 8, 9, 10, 11}

Membership Testing
print(9 in my_set)  
print(14 in my_set) 
True
False

Subset and Superset Operations
subset = {8, 10}                      
print(subset.issubset(my_set))       
print(my_set.issuperset(subset))     
True
True

Set Operations (Union, Intersection, Difference)
another_set = {3, 4, 5, 6, 7}                        
union_set = my_set.union(another_set)                
intersection_set = my_set.intersection(another_set)  
difference_set = my_set.difference(another_set)      

print("Union:", union_set)                           
print("Intersection:", intersection_set)             
print("Difference:", difference_set)                

Union: {3, 4, 5, 6, 7, 8, 9, 10, 11}
Intersection: {7}
Difference: {8, 9, 10, 11}

Ordered Pairs and Cartesian Products
A = {3, 4}  
B = {5, 6}  
cartesian_product = {(a, b) for a in A for b in B}  
print("Cartesian Product: A x B =", cartesian_product)  

Cartesian Product: A x B = {(4, 5), (4, 6), (3, 5), (3, 6)}

Cartesian Plane
import matplotlib.pyplot as plt


points = list(cartesian_product)
x_coords = [x for x, y in points]  
y_coords = [y for x, y in points]  


plt.scatter(x_coords, y_coords)  
plt.title("Cartesian Plane")  
plt.xlabel("X-axis")  
plt.ylabel("Y-axis")  
plt.grid(True)  
plt.show() 

Relations

A = {3, 4}  
B = {5, 6}  


R = {(3, 5), (4, 6)}
print("Relation R:", R)
Relation R: {(4, 6), (3, 5)}

Functions (Mathematical Definition)

def is_function(relation, domain):
    domain_elements = [pair[0] for pair in relation]
    return all(domain_elements.count(e) == 1 for e in domain)

A = {3, 4} 
B = {5, 6}  

f = {(3, 5), (4, 6)}

print("f is a function:", is_function(f, A))

f is a function: True
