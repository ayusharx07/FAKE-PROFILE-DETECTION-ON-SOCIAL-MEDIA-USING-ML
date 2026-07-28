#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[30]:


import pandas as pd


# In[31]:


fake_df = pd.read_csv("fake_users.csv")
real_df = pd.read_csv("real_users.csv")


# In[32]:


print("Fake Dataset Shape :", fake_df.shape)
print("Real Dataset Shape :", real_df.shape)


# In[33]:


print(fake_df.columns.equals(real_df.columns))


# In[34]:


fake_df["label"] = 1      # Fake Profile
real_df["label"] = 0      # Genuine Profile


# In[35]:


df = pd.concat([fake_df, real_df], ignore_index=True)


# In[36]:


print(df["label"].value_counts())


# In[37]:


df.head()


# In[38]:


df.info()


# In[39]:


df.isnull().sum()


# In[40]:


df.to_csv("final_fake_profile_dataset.csv", index=False)


# In[41]:


print("Final Dataset Shape :", df.shape)


# In[42]:


print(df["label"].value_counts())


# In[43]:


print("Fake Profiles :", (df["label"] == 1).sum())
print("Genuine Profiles :", (df["label"] == 0).sum())


# In[44]:


import pandas as pd

# Load datasets
fake_df = pd.read_csv("fake_users.csv")
real_df = pd.read_csv("real_users.csv")

# Check dataset shape
print("Fake Dataset Shape :", fake_df.shape)
print("Real Dataset Shape :", real_df.shape)

# Verify columns
print("Same Columns :", fake_df.columns.equals(real_df.columns))

# Add labels
fake_df["label"] = 1
real_df["label"] = 0

# Merge datasets
df = pd.concat([fake_df, real_df], ignore_index=True)

# Final dataset shape
print("Final Dataset Shape :", df.shape)

# Count classes
print("Fake Profiles :", (df["label"] == 1).sum())
print("Genuine Profiles :", (df["label"] == 0).sum())

# Preview dataset
print(df.head())

# Dataset information
df.info()

# Missing values
print(df.isnull().sum())

# Save final dataset
df.to_csv("final_fake_profile_dataset.csv", index=False)

print("Dataset saved successfully!")


# In[ ]:




