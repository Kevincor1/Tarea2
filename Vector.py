#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[12]:


class VectorCartesiano:
    def __init__(self, x0, y0, z0):
        self.x=float(x0)
        self.y=float(y0)
        self.z=float(z0)
        self.magnitud=((self.x)**2.+(self.y)**2.+(self.z)**2.)**(1/2.) #magnitud  en la instanciacion
        self.vector=[self.x,self.y,self.z]
    def __mul__(self,other):
        '''Sobrecarga del operador *'''
        return self.x*other.x+self.y*other.y+self.z*other.z
    
    def Cruz(self,other):
        '''Producto Cruz'''  # a.cruz(b)=axb
        return  VectorCartesiano(float("{0:.3f}".format(self.y*other.z-self.z*other.y)),float("{0:.3f}".format(-(self.x*other.z-self.z*other.x))),float("{0:.3f}".format(self.x*other.y-self.y*other.x)))
    
    def __add__(self,other):
        '''Sobrecarga del operador suma'''
        return VectorCartesiano(self.x + other.x, self.y + other.y, self.z + other.z)
           
    def __sub__(self,other):        
        '''Sobrecarga del operador resta'''
        return VectorCartesiano(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __getitem__(self,index):
        '''Sobrecarga del operador []'''
        return self.vector[index]
    
    def __eq__(self,other):
        '''Sobrecarga del operador =='''
        if self.x==other.x and self.y==other.y and self.z==other.z:
            return True
        else:
            return False
    def Coord_Esf(self): #Transformacion de cartesianas a esfericas
        if self.x==0:
            if abs(self.y)==self.y:
                E=VectorCartesiano(self.magnitud,np.arccos(self.z/self.magnitud),np.pi/2)
            else:
                E=VectorCartesiano(self.magnitud,np.arccos(self.z/self.magnitud),-np.pi/2)
    
        elif self.x>0 and self.y>=0:
            E=VectorCartesiano(self.magnitud,np.arccos(self.z/self.magnitud),np.arctan(self.y/self.x))
        elif self.x>0 and self.y<=0:
            E=VectorCartesiano(self.magnitud,np.arccos(self.z/self.magnitud),2*np.pi+np.arctan(self.y/self.x))
        elif self.x<0 :
            E=VectorCartesiano(self.magnitud,np.arccos(self.z/self.magnitud),np.pi+np.arctan(self.y/self.x))
        return E
        
    
    def Print(self):
        '''Imprime el vector'''
        print("x: ", self.x)
        print("y: ", self.y)
        print("z: ", self.z)
        print("Magnitud:", self.magnitud)      
        
class VectorPolar(VectorCartesiano):
    def __init__ (self,r0,theta0,fi0):
        if r0<0:
            print("ingrese un valor r>0")
        self.r=r0
        self.theta = abs(theta0-np.pi*int(theta0/(2*np.pi)))
        if fi0<0:
            self.fi = 2*np.pi+(fi0-2*np.pi*int(fi0/(2*np.pi)))
        else:
            self.fi = (fi0-2*np.pi*int(fi0/(2*np.pi)))
        VectorCartesiano.__init__(self,self.r*np.sin(self.theta)*np.cos(self.fi), self.r*np.sin(self.theta)*np.sin(self.fi),self.r*np.cos(self.theta))
    def transP_C(self):
        return VectorCartesiano(self.r*np.sin(self.theta)*np.cos(self.fi), self.r*np.sin(self.theta)*np.sin(self.fi),self.r*np.cos(self.theta))
        
    def Transf_base(self):
        return VectorCartesiano(self.x*np.sin(self.theta)*np.cos(self.fi)+self.y*np.sin(self.theta)*np.sin(self.fi)+self.z*np.cos(self.theta), self.x*np.cos(self.theta)*np.cos(self.fi)+self.y*np.cos(self.theta)*np.sin(self.fi)-self.z*np.sin(self.theta),-self.x*np.sin(self.fi)+self.y*np.cos(self.fi))
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




