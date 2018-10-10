#define a dictionary data structure 

#dictionaries have key : value for the elements
example_dict = {
		"class"		:	"Astr 119",
		"prof"		:	"Brant",
		"awesomness"	:	10
}
print(type(example_dict))   #will say dict 

#get a value via key
course = example_dict["class"]  #given a key
print(course)

#change a value via key
example_dict["awesomness"] += 1   #increase awesomeness by factor of 1

#print the dictionary
print(example_dict)

#print dictionary element by element
for x in example_dict.keys():
	print(x,example_dict[x])