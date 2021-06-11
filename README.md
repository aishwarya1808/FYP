# Context Management in Smart Energy Metering systems in homes

The objective of this project is to develop a context-aware smart energy metering system for households. The proposed context-aware smart energy meter not only measures the electricity consumption of devices but also offers valuable insights to optimize the overall consumption. Generic smart energy meters can only measure the consumption of devices but cannot narrow down the causes of peak consumption or offer logical explanations as to why they consumed large amounts of electricity. Context management in this regard is the requirement of the day as this can bring down both the consumption of resources, as well the money spent on unnecessary consumption. 

The system consists of the following modules: 
●	Sensors from the environment 
●	Ontology generated using protégé 
●	Python code using owlready API 
●	Sending mail to the user 


**Sensors from the environment **
The temperature sensor is used to measure the surrounding temperature. This is used to infer if  fan/cooling devices need to be up and running. This coupled with the data from the IR sensor can tell if the devices are running wastefully (i.e) without any people around.
The PIR sensor is installed in every room of the house. This can detect the presence of a person in the vicinity. The sensitivity of the PIR sensor can be adjusted to pick up movement only from people and not from smaller objects or beings like insects. The value from this sensor is used in conjunction with the values from the temperature sensor and the current sensing module to derive inference.
The current sensor measures the electrical consumption of devices. The value returned is in ampere. For the purpose of the project, suitable conversion to watt is done. The 
consumption of the devices connected are measured over a period of time and their average is taken for inference.


**Complete Ontology Generated**
![image](https://user-images.githubusercontent.com/61593310/121636375-736efc00-caa5-11eb-8063-f9a4ae0aeff9.png)

**SWRL Rules**
![image](https://user-images.githubusercontent.com/61593310/121636418-85509f00-caa5-11eb-9b47-3cf4721f994b.png)


The rules written using Python script are synchronized using the Pellet reasoner available in the Protégé tool accessed via the owlready2 API. 
Pellet reasoner is used to run the two rules used for calculating the average power consumption of the light bulb from the values provided by the current sensor and the average surrounding temperature from the values provided by the temperature sensor. Based on theses average values, suitable suggestions are offered to the users
