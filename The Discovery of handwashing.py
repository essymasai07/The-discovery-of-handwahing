# The importance of handwashing. A discovery made by Dr. Ignaz
import pandas as pd
yearly=pd.read_csv('yearly_deaths_by_clinic.csv')
# This is the number of women that gave birth in two clinics where Dr.Ignaz was working from 1841 to 1846.
print(yearly)
# Calculating the proportion of deaths per birth
yearly['proportion_deaths'] = yearly['deaths'] / yearly['births']
# Extracting clinic 1 data to clinic_1 and clinic 2 data to clinic_2.
clinic_1= yearly.loc[0:5]
clinic_2 = yearly.loc[6:11]
print(clinic_1)
print(clinic_2)
# Plotting the proportions of death at both clinic 1 and clinic2
import matplotlib.pyplot as plt
ax= clinic_1.plot(x='year', y='proportion_deaths')
ax= clinic_2.plot(x='year', y='proportion_deaths', label='clinic 1', ylabel='Proportion deaths', ax=ax)
plt.show()
# Loading monthly data from Clinic 1 to see if handwashing had any effect on the number of deaths.
monthly= pd.read_csv('monthly_deaths.csv', parse_dates=['date'])
# Calculating the proportion of deaths per birth
monthly['proportion_deaths'] = monthly['deaths'] / monthly['births']
print(monthly.head())
# plotting monthly proportions of deaths
ax = monthly.plot(x='date', y='proportion_deaths', ylabel='Proportion deaths')
plt.show()
# Date when Handwashing was made mandatory in the hospitals.
handwashing_start= pd.to_datetime('1847-06-01')
before_washing = monthly[monthly["date"] < handwashing_start]
after_washing = monthly[monthly["date"] >= handwashing_start]
# Plotting monthly proportions of deaths before and after handwashing 
ax= before_washing.plot(x="date", y="proportion_deaths", label="Before handwashing")
ax=after_washing.plot(x="date", y="proportion_deaths", label="After handwashing", ax=ax, ylabel="Proportion deaths")
plt.show()
# Difference in mean monthly proportion of deaths due to handwashing
before_proportion= before_washing['proportion_deaths']
after_proportion = after_washing['proportion_deaths']
mean_difference= after_proportion.mean() - before_proportion.mean()
print(mean_difference)
# A bootstrap analysis of the reduction of deaths due to handwashing
boot_mean_diff=[]
for i in range (3000):
    boot_before=before_proportion
    boot_after=after_proportion
    boot_mean_diff.append(boot_before.mean() - boot_after.mean())
# Calculating a 95% confidence interval from boot_mean_diff 
confidence_interval= pd.Series(boot_mean_diff).quantile([0.025, 0.975])
print(confidence_interval)
# According to the data that Dr.Ignaz collected:
doctors_should_wash_their_hands = True