
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure: #DEFINIMOS LA CLASE FAMILIA CON SU ESTRUCTURA
    def __init__(self,last_name):      
        self.last_name = last_name

        self._members = [
            {"id": self._generateId()        
            "nombre": "Jane",
            "edad" 35,
            "suerte": [10, 14, 3]},
            {"id": self._generateId()        
            "nombre": "John",
            "edad" 33,
            "suerte": [7, 13, 22]},
            {"id": self._generateId()        
            "nombre": "Jimmy",
            "edad" 5,
            "suerte": [1]}
        ]
        # example list of members
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):        
       # fill this method and update the return
       #Generamos el id , utilizando el metodo generateid
       #member['id'] = _generateId()
       #añadimos a _members el elemento
       member['id'] = self._generateId()
       self._members.append(member)
       print(member)
       return self.member
        
    def delete_member(self, id):
        # fill this method and update the return
        print("estamops en delete_member - id por parametro = " + str(id))
        #Recorremos el array de elementos _selfmembers
        for indice in range(0,len(self._members)):  
            #si el indice que contiene el id es igual al id recibido
            if self._members[indice]['id'] == id: 
                #eliminamos ese elemento del array
                self._members.pop(indice)
                print(self._members)
        return self._members





    def get_member(self, id):
        # fill this method and update the return
        print("estamops en get_member - id por parametro = " + str(id))        
        
        for people in self._members:  
            if people['id'] == id:
                print(people)# Para testear print(lst.index(20))
                #print(self._members.index(people[id]))
            return people
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

