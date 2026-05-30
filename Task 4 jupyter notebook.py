# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
df = pd.read_csv('AI_Impact_on_Jobs_2030.csv')
df

# %%
import pandas as pd
import numpy as np
def clean_AI_Impact_on_Jobs_2030(df):
    df_clean = df.copy()
df_clean.columns = df_clean.columns.str.strip().str.lower().str.replace(' ','_')
cat_cols = ['job_title','industry','country','education_level','remote_work_possibility']
for col in cat_cols:
    if col in df_clean.columns:
        df_clean[col] 
        df_clean[col].fillna('Unknown').str.strip()
num_cols = ['years_experience','ai_replacement_risk','future_demand_score']
for col in num_cols:
    if col in df_clean.columns:
        df_clean[col] 
        df_clean[col].fillna(df_clean[col].median()
if 'employee_id' in df_clean.columns
        df_clean['employee_id'] = 
df_clean['employee_id'].astype(str)
if 'years_experience' in df_clean.columns:
    df_clean['years_experience'] =
df_clean['years_experience'].astype(int)
if 'education_level' in df_clean.columns:
    df_clean['education_level'] =
df_clean['education_level'].str.title().replace({
    'High School':'High School',
    'Bachelor':'Bachelor',
    'Phd':'Phd',
})
if 'remote_work_possibility' in 
df_clean.columns:
    df_clean['remote_work_possibility'] = 
    df_clean['remote_work_possibility'].str.title()
if'country' in df_clean.columns:
    df_clean['country'] = 
    df_clean['country'].replace({'UK':'United Kingdom','UAE';'United Arab Emirates'})
if 'employee_id' in df_clean.columns:
    df_clean = df_clean.drop_duplicates(subset=['employee_id'], keep='first')
score_col = ['ai_replacement_risk','future_demand_score']
for col in score_cols:
    if col in df_clean.columns:
        df_clean[col] = df_clean[col].clip(0,1)
if 'years_experience' in df_clean.columns:
    df_clean['years_experience'].clip(0,50)
    return df_clean
    df_clean = clean_AI_Impact_on_Jobs_2030.csv(df)
    print(f"Shape before:{df.shape},after:
    {df_clean.shape}")
    print(df_clean.isna().sum())
    print(df_clean.head())


# %%
