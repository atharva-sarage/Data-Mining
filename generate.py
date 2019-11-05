import pandas as pd

f=open('movie_id.txt','r')
s=f.read()
s_list=s.split('\n')
df_reviews = pd.read_json('datasets/IMDB_reviews.json', lines=True)
df_reviews.drop(["rating",'review_date','review_summary','user_id'],axis=1,inplace=True)
i=5
for idd in s_list:
	df2=df_reviews.loc[df_reviews['movie_id']==idd]
	print(df2.shape)
	df2.drop(['movie_id'],axis=1,inplace=True)
	df2.to_csv('dataset'+str(i)+'.csv')
	i+=1
