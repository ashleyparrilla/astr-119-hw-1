#string

s = "I am a string."
print(type(s))   #will say str

#boolean

yes = True  #boolean true
print(type(yes))

no = False
print(type(no))

#list--- ordered and changeable

alpha_list = ["a", "b", "c"]   #list initialization
print(type(alpha_list))
print(type(alpha_list[0]))   #will say string
alpha_list.append("d")       #will add d to the list end
print(alpha_list)            #prints list

#Tuple -- ordered and unchangeable

alpha_turple = ("a", "b", "c")  #tuple initialization
print(type(alpha_turple))       #will say tuple

try:
	alpha_turple[2] = "d"  #attempt the following line, wont work and will raise typeerror
except TypeError:    #when we get a typeerror, print this message
	print("We can't add elements to turple!")
print(alpha_turple)
