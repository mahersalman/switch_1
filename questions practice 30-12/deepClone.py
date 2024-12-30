"""
DeepClone
Create the deepClone function:
  x = {a: "b", a2: ["first", "second"]};
  y = {b: x, b3: ["firtsY", x]};
  z = deepClone(y);
  def deepClone(obj) {}
"""

def deepClone(obj):
    if obj is None or not isinstance(obj,(list,dict)):
        return obj
    if isinstance(obj,list):
        return [deepClone(element) for element in obj]
    if isinstance(obj,dict):
        return {key: deepClone(value) for key ,value in obj.items()}
    
x = {'a': "b", 'a2': ["first", "second"]}
y = {'b': x, 'b3': ["firtsY", x]}
z = deepClone(y)
print(z)