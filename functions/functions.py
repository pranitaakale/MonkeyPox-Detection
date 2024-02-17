import pandas as pd

df = pd.read_csv('data\DATA.csv')
df.columns = df.columns.str.replace(' ', '_')
main_df = df.drop(columns = ['Patient_ID', 'Sexually_Transmitted_Infection'])
systemic_illness_values = main_df['Systemic_Illness'].unique()
map_result = {'Positive': 1, 'Negative':0}
main_df['MonkeyPox'] = main_df['MonkeyPox'].replace(map_result)

total_records = main_df.shape[0]

def filter_records(Systemic_Illness, Rectal_Pain, HIV_Infection, Oral_Lesions, Penile_Oedema, Sore_Throat, Solitary_Lesion, Swollen_Tonsils):
  filtered_records = main_df[
      (main_df['Systemic_Illness'] == Systemic_Illness) &
      (main_df['Rectal_Pain'] == Rectal_Pain) &
      (main_df['HIV_Infection'] == HIV_Infection) &
      (main_df['Oral_Lesions'] == Oral_Lesions) &
      (main_df['Penile_Oedema'] == Penile_Oedema) &
      (main_df['Sore_Throat'] == Sore_Throat) &
      (main_df['Solitary_Lesion'] == Solitary_Lesion) &
      (main_df['Swollen_Tonsils'] == Swollen_Tonsils)
  ]
  
  positive_filtered_records = filtered_records[filtered_records['MonkeyPox']==1]
  
  num_filtered_records = filtered_records.shape[0]
  num_positive_filtered_records = positive_filtered_records.shape[0]

  # print("Total records for above condition = ", num_filtered_records)
  # print("Total records for positive cases = ", num_positive_filtered_records)
  percent_of_pos_record = (num_positive_filtered_records/num_filtered_records)*100
  # print("Chances of the case being MonkeyPox = ", percent_of_pos_record)

  return percent_of_pos_record
