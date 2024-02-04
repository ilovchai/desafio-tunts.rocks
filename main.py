import gspread
import pandas as pd
import numpy as np

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key("1p_vrq4Pmi1JhqtZ-oLYCrZfazxtf5czdjmEzWqVVkVg")
worksheet= sh.sheet1

### create dataframe out of spreadsheet ###

v = worksheet.get_all_values()
df = pd.DataFrame(v[3:], columns=v[2])


### 

grades = df[['P1','P2','P3']]
absence = df['Faltas']
df['Faltas'] = absence.astype(str).astype(int)
grades_int = grades.astype(str).astype(int)
df['media'] = (grades_int['P1'] + grades_int['P2'] + grades_int['P3']) // 3

###

conditions_mean = {
    'reprovado por falta': df.Faltas.gt(15),
    'reprovado por nota': df.media.lt(50),
    'exame final': df.media.le(70, 50),
    'aprovado': df.media.ge(60)
}
df.iloc[:,6] = np.select(conditions_mean.values(), conditions_mean.keys())

###
df['Nota para Aprovação Final'] = np.where(df['Situação'] == 'exame final', df['media'] - 10, 0)

df.drop(columns=['', ''], inplace=True)
df.drop(columns=['media'], inplace=True)

worksheet.update('A4', df.values.tolist())

print(df)

