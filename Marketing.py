import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data Exploration and Preprocessing
df = pd.read_csv('marketing_campaign_dataset.csv')

print(df.head())
print(df.info())

print(df.isnull().sum())

df['Date'] = pd.to_datetime(df['Date'])
df['Acquisition_Cost'] = df['Acquisition_Cost'].str.replace('$', '',regex=False)
df['Acquisition_Cost'] = df['Acquisition_Cost'].str.replace(',','',regex=False)
df['Acquisition_Cost'] = df['Acquisition_Cost'].astype(float)

# Campaign Performance Metrics
averageConversionRate = df['Conversion_Rate'].mean()
averageAcquisitionCost = df['Acquisition_Cost'].mean()
averageROI = df['ROI'].mean()

print(f"Average Conversion Rate: {averageConversionRate:.2%}")
print(f"Average Acquisition Cost: {averageAcquisitionCost:,.2f}")
print(f"Average ROI: {averageROI:.2f}")

# Channel Performance Metrics
channelPerformance = df.groupby('Campaign_Type').agg({
    'Conversion_Rate': 'mean',
    'ROI': 'mean'
}).reset_index()

print(channelPerformance)

sns.set(style='whitegrid')


# Bar plot for Average Conversion Rate
plt.figure(figsize=(10, 6))
sns.barplot(x='Campaign_Type', y='Conversion_Rate', data=channelPerformance)
plt.title('Average Conversion Rate by Campaign Type')
plt.ylabel('Average Conversion Rate (%)')
plt.xticks(rotation=45)

# Adding data labels
for index, value in enumerate(channelPerformance['Conversion_Rate']):
    plt.text(index, value, f'{value:.2%}', ha='center', va='bottom')

plt.ylim(0, max(channelPerformance['Conversion_Rate']) + 0.01)  # Add some space above the bars
plt.show()

# Bar plot for Average ROI
plt.figure(figsize=(10, 6))
sns.barplot(x='Campaign_Type', y='ROI', data=channelPerformance)
plt.title('Average ROI by Campaign Type')
plt.ylabel('Average ROI')
plt.xticks(rotation=45)

# Adding data labels
for index, value in enumerate(channelPerformance['ROI']):
    plt.text(index, value, f'{value:.2f}', ha='center', va='bottom')

plt.ylim(0, max(channelPerformance['ROI']) + 1)  # Add some space above the bars
plt.show()

bestChannel = channelPerformance.loc[channelPerformance['ROI'].idxmax()]
print(f"The best performing campaign type is {bestChannel["Campaign_Type"]} with an average ROI of {bestChannel['ROI']:.2f}.")