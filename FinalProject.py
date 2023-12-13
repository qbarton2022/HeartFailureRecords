import pandas as pd

#get datset
dataset = pd.read_csv('C:/Users/barto/Documents/heart_failure_clinical_records_dataset.csv')

#split the dataset into people who died and people who survived
datasetDead = dataset[dataset['DEATH_EVENT'] == 1]
datasetAlive = dataset[dataset['DEATH_EVENT'] == 0]

#display desriptive analysis for ejection_fraction
#print(datasetDead.loc[:,'ejection_fraction'].describe())
#print(datasetAlive.loc[:,'ejection_fraction'].describe())

#display descriptive analysis for serum_creatinine
#print(datasetDead.loc[:,'serum_creatinine'].describe())
#print(datasetAlive.loc[:,'serum_creatinine'].describe())

#display descriptive analysis for serum_sodium
#print(datasetDead.loc[:,'serum_sodium'].describe())
#print(datasetAlive.loc[:,'serum_sodium'].describe())

#display descriptive analysis for platlets
#print(datasetDead.loc[:,'platelets'].describe())
#print(datasetAlive.loc[:,'platelets'].describe())

#display descriptive analysis for creatinine_phosphokinase
print(datasetDead.loc[:,'creatinine_phosphokinase'].describe())
print(datasetAlive.loc[:,'creatinine_phosphokinase'].describe())