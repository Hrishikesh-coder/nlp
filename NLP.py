#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


import nltk
import nltk.corpus


# In[6]:


nltk.download('popular')


# In[7]:


print(os.listdir(nltk.data.find("corpora")))


# In[10]:


from nltk.corpus import movie_reviews


# In[11]:


movie_reviews.words()


# In[13]:


nltk.corpus.gutenberg.fileids()


# In[18]:


hamlet = nltk.corpus.gutenberg.words('shakespeare-caesar.txt')


# In[19]:


hamlet


# In[20]:


for word in hamlet[:500]:
    print(word, sep=' ',end=' ')


# In[36]:


snippet = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
            Aenean commodo ligula eget dolor. Aenean massa. 
            Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. 
            Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
            Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. 
            In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. 
            Nullam dictum felis eu pede mollis pretium. Integer tincidunt. 
            Cras dapibus. Vivamus elementum semper nisi. 
            Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. 
            Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. 
            Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. 
            Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. 
            Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. 
            Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. 
            Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. 
            Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc."""


# In[37]:


type(snippet)


# In[38]:


from nltk.tokenize import word_tokenize


# In[39]:


snippet_tokens = word_tokenize(snippet)


# In[40]:


snippet_tokens


# In[41]:


len(snippet_tokens)


# In[42]:


from nltk.probability import FreqDist


# In[43]:


dist = FreqDist()


# In[44]:


for word in snippet_tokens:
    dist[word.lower()]+=1


# In[45]:


dist


# In[47]:


dist[',']


# In[48]:


len(dist)


# In[49]:


dist_top = dist.most_common(10)


# In[50]:


dist_top


# In[ ]:




