var='The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'
lista=[]
var=var.replace(',',' ')
var=var.replace('.', ' ')
var=var.lower()
var=var.split(' ')
print(var)
for k in var:
    if k[0::] in 'python' or k[-1] in 'python':
        lista.append(k)
print(lista)