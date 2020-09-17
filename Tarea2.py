#!/usr/bin/env python
# coding: utf-8

# In[31]:


from Vector import *
import numpy as np


# In[32]:


a=VectorCartesiano(1.5,0,2.4)
b=VectorCartesiano(0,1,9)
c=VectorCartesiano(4.2,0.05,0)


# In[33]:


# componentes esfericas de a
A=VectorCartesiano.Coord_Esf(a)
AA=VectorPolar.Transf_base(VectorPolar(A.vector[0],A.vector[1],A.vector[2]))
print("La componente en la direccion  r es : {0:.3f}".format(AA.x))
print("La componente en la direccion  theta es : {0:.3f}".format(AA.y))
print("La componente en la direccion  fi es : {0:.3f}".format(AA.z))


# In[34]:


# componetes esfericas de b
B=VectorCartesiano.Coord_Esf(b)
BB=VectorPolar.Transf_base(VectorPolar(B.vector[0],B.vector[1],B.vector[2]))
print("La componente en la direccion  r es : {0:.3f}".format(BB.x))
print("La componente en la direccion  theta es : {0:.3f}".format(BB.y))
print("La componente en la direccion  fi es : {0:.3f}".format(BB.z))


# In[35]:


#componentes esfericas de c
C=VectorCartesiano.Coord_Esf(c)
CC=VectorPolar.Transf_base(VectorPolar(C.vector[0],C.vector[1],C.vector[2]))
print("La componente en la direccion  r es : {0:.3f}".format(CC.x))
print("La componente en la direccion  theta es : {0:.3f}".format(CC.y))
print("La componente en la direccion  fi es : {0:.3f}".format(CC.z))


# In[36]:


# Productos Internos
print("a.b: {0:.3f}".format(a*b))
print("a.c: {0:.3f}".format(a*c))
print("b.c: {0:.3f}".format(b*c))


# In[37]:


#roducto Cruz
print("axb : ", (a.Cruz(b)).vector)
print("axc : ", (a.Cruz(c)).vector)
print("bxc : ", (b.Cruz(c)).vector)


# In[46]:


#angulos
ang_ab=np.arccos((a*b)/(a.magnitud*b.magnitud))
ang_ac=np.arccos((a*c)/(a.magnitud*c.magnitud))
ang_bc=np.arccos((b*c)/(b.magnitud*c.magnitud))
print("El angulo entre a y b es :{0:.4f}".format(ang_ab), " radianes")
print("el angulo entre a y c es :{0:.4f}".format(ang_ac), "radianes")
print("el angulo entre b y c es :{0:.4f}".format(ang_bc), "radianes")


# In[ ]:





# In[ ]:





# In[ ]:




