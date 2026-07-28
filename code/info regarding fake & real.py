#!/usr/bin/env python
# coding: utf-8

# In[1]:


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




