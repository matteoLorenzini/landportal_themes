import pandas as pd
import fasttext as ft

# here you load the csv into pandas dataframe
df=pd.read_csv('test_ft.csv')


# here you load your fasttext module
model=ft.load_model('themes_landvoc.bin')

# line by line, you make the predictions and store them in a list
predictions=[]
for line in df['Abstract/Description']:
    pred_label=model.predict(line, k=4, threshold=0.001) 
    predictions.append(pred_label)

# you add the list to the dataframe, then save the datframe to new csv
df[['prediction','value']]=predictions
df.replace(regex=['__label__'], value='')
print(df)

exit()
df.to_csv('themes_predicted.csv',sep=',',index=False)