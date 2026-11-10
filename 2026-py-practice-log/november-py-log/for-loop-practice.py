""" 
Topic: For Loop Fundamentals & Iteration Patterns
Description: Daily practice exploring string traversal, numerical changes,
            list iteration, and index-based iteration in python.
Date: November 2026
"""
# ------------------------------------------------------------------------
# 1.Iterating over strings
# ------------------------------------------------------------------------
for i in "chinmay":
    print(i)
    
    
# ------------------------------------------------------------------------
# 2. Iterating with range()
# ------------------------------------------------------------------------  
for i in range(10):
    print(i)
    
for i in range(3, 10):
    print(i)
    
    
# ------------------------------------------------------------------------
# 3. Direct Iteration Over Lists
# ------------------------------------------------------------------------
studentID = ["chinmay", "Aundh, Pune", 'ID: 8833229', 25]
for i in studentID:
    print(i)
    
 
# ------------------------------------------------------------------------
# 4. Index-Based Iteration Using len() and range()
# ------------------------------------------------------------------------    
name = "Naina"
print("The length of name 'Naina' is", len(name))
for i in range(len(name)): 
    print(name[i])
   

friends = ["Priyanka", "Varun", "Shraddha", "Jimmy"]
for index in range(len(friends)):
    print(friends[index])
    



