#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing dependencies

import cv2
from matplotlib import pyplot as plt


# In[2]:


# creating a capture device

cap = cv2.VideoCapture(0)


# In[59]:


# Getting a frame from the capture device

ret, frame = cap.read()


# In[60]:


print(ret)


# In[65]:


print(frame)


# In[67]:


# PRINTING A FRAME / PICTURE

plt.imshow(frame)


# In[63]:


# Releases camera back to off

cap.release()


# In[69]:


# PRINTING A COLORED PHOTO/FRAME

plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))


# In[70]:


# writing a Function to take a photo & save it to "opencv" folder


# In[73]:


def take_photo():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('NAVIN.jpg', frame)
    cap.release()
    


# In[74]:


take_photo()


# # Rendering in Real time

# In[10]:


import cv2

#connect to webcam
cap = cv2.VideoCapture(0)

# Loop through every frame until we close webcam
while cap.isOpened():
    ret, frame = cap.read()
    
    #show image 
    cv2.imshow("Nav's cam",frame)
    
    # checks whether 'q' has been hit & closes the webcam/loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# Releases the webcam        
cap.release()
# closes the frame
cv2.destroyAllWindows()
    


# In[ ]:




