#LIST OF DICTIONARIES

a = [{"name": "alice", "age":25}, {"name":"bob", "age": 28}]
print(a)

#LIST OF DICTIONARIES USING A LOOP

a =[]
for i in range (3):
    a.append({"name": f"person{i+1}", "age": 20+i}, )
    print(a)