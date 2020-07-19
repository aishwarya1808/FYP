from owlready2 import *	
onto = get_ontology("file://C://Users//Aishwarya//Desktop//Python/abc.rdf")
onto.load()
#print(onto["Devices"])
list(onto.classes())

#prints the classes in the ontology