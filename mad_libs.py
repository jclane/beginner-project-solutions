

adj1 = input("Please enter an adjective >> ")
adj2 = input("PLease enter another adjective >> ")
noun1 = input("Please enter a noun >> ")
verb = input("Please enter a verb >> ") 
adj3 = input("Please enter an adjective >> ")
noun2 = input("Please enter a noun >> ")
name = input("Please enter a name >> ")

name = name.title()

print("The {} {} {} {} over the {} {}.".format(adj1, adj2, noun1, verb, adj3, noun2))
print("I {} {}, but I didn't {} the {}.".format(verb, name, verb, noun2))
