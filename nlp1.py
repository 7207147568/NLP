#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import ssl

# Set the SSL certificate bundle path
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append("/path/to/certifi/cacert.pem")

# Download NLTK data
nltk.download()


# In[4]:


from nltk.corpus import brown
brown.categories()


# In[5]:


brown.words(categories='adventure')


# In[12]:


inaugural.words(fileids='1861-Lincoln.txt')


# In[13]:


from nltk.corpus import webtext
webtext.fileids()


# In[17]:


from nltk import FreqDist

text1 = "Karthikeya is a good boy"

fd = FreqDist(text1.split())

print(fd)


# In[18]:


from nltk import FreqDist

text1 = "Karthikeya is a good boy and he studies in Vit Vellore"

fd = FreqDist(text1.split())

print(fd)


# In[ ]:




