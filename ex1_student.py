class Student :
     def __init__(self, nom , age) :
      self.nom = nom
      self.age = age
student1 = Student("Alice" , 20)
student2 = Student("Marc", 24)
student3 = Student("Sarah" , 19)
print(student1.nom)
print(student1.age)
print(student2.nom)
print(student2.age)
print(student3.nom)
print(student3.age)

def afficher_infos(nom, age) :
  student1 = Student ("Alice" ,20)
  student2 = Student ("Marc" , 24)
  student3 = Student ("Sarah" , 19)
  afficher_infos(student1)
  afficher_infos(student2)
  afficher_infos(student3)
  
  
    
    
    
    
        
    






        


  
  

        