from owlready2 import *	
onto = get_ontology("file://C:/Users/Aishwarya/Desktop/New folder/Ontology/new_python_owl.owl")
onto.load()

class Devices(Thing):
    namespace=onto
    
class House(Thing):
    namespace=onto

class Modules(Thing):
    namespace=onto

class Person(Thing):
    namespace=onto

class Rooms(Thing):
    namespace=onto

class Sensors(Thing):
    namespace=onto

class Watt(Thing):
    namespace=onto
    
class LightBulb(Devices):
    pass

class IRSensor(Sensors):
    pass

class GSM(Modules):
    pass

class consumes(ObjectProperty):
    domain=[Devices]
    range=[Watt]
    
class no_consumption(ObjectProperty):
    domain=[Devices]
    range=[Watt]    

class present_in(ObjectProperty):
    domain=[Person]
    range=[Rooms]

class absent_in(ObjectProperty):
    domain=[Person]
    range=[Rooms]
    
class consists_of(ObjectProperty):
    domain=[House]
    range=[Devices,Rooms,Sensors]
    
class detects_motion(ObjectProperty):
    domain=[Sensors]
    range=[Person]
    
class no_detection(ObjectProperty):
    domain=[Sensors]
    range=[Person]
    
class sends_message(ObjectProperty):
    domain=[Modules]
    range=[Person]

class switches_on(ObjectProperty):
    domain=[Person]
    range=[Devices]
    
class switches_off(ObjectProperty):
    domain=[Person]
    range=[Devices]