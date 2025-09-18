import pandas as pd

def calculate_demographic_data(print_data=True):
             #read data
             df = pd.read_csv('../adult.data.csv')
             print(df.head())

             #number of people in each race

             race_count = df['race'].value_counts()

             #average age of men
             men_df = df[df['sex'] == 'Male']
             average_age_men = round(men_df['age'].mean(), 1)

             #percentage off people with bachelors degree
             bachelors_count = len(df[df['education'] == 'Bachelors'])
             total_count = len(df)
             percentage_bachelors = round((bachelors_count / total_count) * 100, 1)

             #Analyze Salary Based on Education Level
             advanced_education = ['Bachelors', 'Masters', 'Doctorate']
             advanced_education_df = df[df['education'].isin(advanced_education)]
             #using the logical ~ operator
             non_advanced_education_df = df[~df['education'].isin(advanced_education)]

             higher_education_rich = round(len(advanced_education_df[advanced_education_df['salary'] == '>50K']) / len(
                 advanced_education_df) * 100, 1)
             lower_education_rich = round(len(non_advanced_education_df[non_advanced_education_df['salary'] == '>50K']) / len(
                 non_advanced_education_df) * 100, 1)

             min_work_hours = df['hours-per-week'].min()
             min_hours_workers = df[df['hours-per-week'] == min_work_hours]
             num_min_hours_rich = len(min_hours_workers[min_hours_workers['salary'] == '>50K'])
             rich_percentage = round((num_min_hours_rich / len(min_hours_workers)) * 100, 1)

             country_salary_counts = df.groupby('native-country')['salary'].value_counts()
             country_totals = df['native-country'].value_counts()

             country_percentages = (country_salary_counts.loc[:, '>50K'] / country_totals) * 100
             highest_earning_country = country_percentages.idxmax()
             highest_earning_country_percentage = round(country_percentages.max(), 1)

             india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
             top_india_occupation = india_rich['occupation'].value_counts().idxmax()

             if print_data:
                 print("Number of each race:\n", race_count)
                 print("Average age of men:", average_age_men)
                 print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
                 print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
                 print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
                 print(f"Min work time: {min_work_hours} hours/week")
                 print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
                 print("Country with highest percentage of rich:", highest_earning_country)
                 print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
                 print("Top occupations in India:", top_india_occupation)

             return {
                 'race_count': race_count,
                 'average_age_men': average_age_men,
                 'percentage_bachelors': percentage_bachelors,
                 'higher_education_rich': higher_education_rich,
                 'lower_education_rich': lower_education_rich,
                 'min_work_hours': min_work_hours,
                 'rich_percentage': rich_percentage,
                 'highest_earning_country': highest_earning_country,
                 'highest_earning_country_percentage':
                     highest_earning_country_percentage,
                 'top_IN_occupation': top_india_occupation
             }


