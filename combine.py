# -*- coding: utf-8 -*-
"""combine.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11cN0aRULn-XB2dE9Aovz4t4XncYewmsZ
"""
# import streamlit_theme as stt

# stt.set_theme({'primary': '#000000'})

import numpy as np
class smith_waterman(object):
    def __init__(self,string1,string2, match=None, mismatch=None, gap=None):
        self.q = string1
        self.p = string2
        self.gapPen = int(gap)
        self.mismatchPen = int(mismatch)
        self.matchScore = int(match)
        self.finalQ = ""
        self.finalP = ""
        self.MatrixA = np.empty(shape=[len(self.p)+1,len(self.q)+1])
        self.MatrixB = np.empty(shape=[len(self.p)+1,len(self.q)+1])
        self.maxScore = 0
        self.maxI = None
        self.maxJ =None

    def calcTables(self):
        try:
            self.q = '-' + self.q
        except IOError:
            print("Error with sequence 1")

        try:
            self.p = '-' + self.p
        except IOError:
            print("Error with sequence 2")

        self.MatrixA[:,0] = 0
        self.MatrixA[0,:] = 0
        self.MatrixB[:,0] = 0
        self.MatrixB[0,:] = 0

        for i in range(1,len(self.p)):
            for j in range(1, len(self.q)):

                if self.p[i] == self.q[j]:
                    self.MatrixA[i][j] = self.MatrixA[i-1][j-1] + self.matchScore
                    self.MatrixB[i][j] = 3

                    if self.MatrixA[i][j] > self.maxScore:
                        self.maxScore = self.MatrixA[i][j]
                        self.maxI = i
                        self.maxJ = j

                else:
                    self.MatrixA[i][j] = self.findMaxScore(i,j)

    def findMaxScore(self, i, j):

        
        qDelet = self.MatrixA[i-1][j] + self.gapPen
        pDelet = self.MatrixA[i][j-1] + self.gapPen
        mismatch = self.MatrixA[i-1][j-1] + self.mismatchPen
        maxScore = max(qDelet, pDelet, mismatch)

        if qDelet == maxScore:
            self.MatrixB[i][j] = 2 

        elif pDelet == maxScore:
            self.MatrixB[i][j] = 1 

        elif mismatch == maxScore:
            self.MatrixB[i][j] = 3

        return maxScore


import textdistance
# sw = smith_waterman()
class String_matching:
    def lcs(X,Y): 
        m = len(X) 
        n = len(Y) 

        L = [[None]*(n+1) for i in range(m+1)] 

        for i in range(m+1): 
            for j in range(n+1): 
                if i == 0 or j == 0 : 
                    L[i][j] = 0
                elif X[i-1] == Y[j-1]: 
                    L[i][j] = L[i-1][j-1]+1
                else: 
                    L[i][j] = max(L[i-1][j] , L[i][j-1]) 
        return L[m][n]/(max(len(X),len(Y)))
    
    def iterative_levenshtein(s, t):
        rows = len(s)+1
        cols = len(t)+1
        dist = [[0 for x in range(cols)] for x in range(rows)]

        for i in range(1, rows):
            dist[i][0] = i

        for i in range(1, cols):
            dist[0][i] = i
            
        for col in range(1, cols):
            for row in range(1, rows):
                if s[row-1] == t[col-1]:
                    cost = 0
                else:
                    cost = 1
                dist[row][col] = min(dist[row-1][col] + 1,dist[row][col-1] + 1,dist[row-1][col-1] + cost) 
        
        return dist[row][col]/(max(len(s),len(t)))

    def hamming_distance(string1, string2):
        try:
            distance = 0
            L = len(string1)
            for i in range(L):
                if string1[i] != string2[i]:
                    distance += 1
            return distance/(max(len(string1),len(string2)))
        except:
            return textdistance.hamming.normalized_similarity(string1,string2)
    
    def smith_waterman(string1,string2):
        return textdistance.smith_waterman.normalized_similarity(string1,string2)
    
    def jaro_winkler(string1,string2):
        return textdistance.jaro_winkler.normalized_similarity(string1,string2)
    
    def Strcmp95(string1,string2):
        return textdistance.strcmp95.normalized_similarity(string1,string2)
    
    def Needleman_wunsch(string1,string2):
        return textdistance.needleman_wunsch.normalized_similarity(string1,string2)

    def gotoh(string1,string2):
        return textdistance.gotoh.normalized_similarity(string1,string2)
    
    def jaccard(string1,string2):
        return textdistance.jaccard.normalized_similarity(string1,string2)
    
    def sorensen_dice(string1,string2):
        return textdistance.sorensen_dice.normalized_similarity(string1,string2)
    
    def tversky(string1,string2):
        return textdistance.tversky.normalized_similarity(string1,string2)
    
    def overlap(string1,string2):
        return textdistance.overlap.normalized_similarity(string1,string2)
    
    def tanimoto(string1,string2):
        return textdistance.tanimoto.normalized_similarity(string1,string2)
    
    def cosine(string1,string2):
            return textdistance.cosine.normalized_similarity(string1,string2)
    
    def mra(string1,string2):
            return textdistance.mra.normalized_similarity(string1,string2)
    
    def editex(string1,string2):
            return textdistance.editex.normalized_similarity(string1,string2)
import pandas as pd
import pyreadstat
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import os

# from openpyxl import load_workbook
import csv
# import openpyx

# from pandas_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report
# def explore(df):
#   pr = ProfileReport(df, explorative=True)
#   st_profile_report(pr)
filename =""
metafile = ""

def get_df(file):
  # get extension and read file
  extension = file.name.split('.')[1]  
  if extension.upper() == 'CSV':
    df = pd.read_csv(file)
  elif extension.upper() == 'XLSX':
    df = pd.read_excel(file, engine='openpyxl')
  elif extension.upper() == 'SAV':
    df = pyreadstat.read_sav(file)
  return df

def transform(df):
	  # Select sample size
	  frac = st.slider('Random sample (%)', 1, 100, 100)
	  if frac < 100:
	    df = df.sample(frac=frac/100)  # Select columns
	  cols = st.multiselect('Columns', 
	                        df.columns.tolist(),
	                        df.columns.tolist())
	  df = df[cols]  
	  return df

def highlight(x):
    c = 'background-color: lime'

    df1 = pd.DataFrame('', index=x.index, columns=x.columns)
    m = x.isna().any(axis=1)
    df1 = df1.mask(m, c)
    return df1

def highlightDuplicate(x):
    c = 'background-color: yellow'

    df1 = pd.DataFrame('', index=x.index, columns=x.columns)
    m = x.duplicated()
    df1 = df1.mask(m, c)
    return df1

def highlightMeta(x,score):
	low =[] 
	for i in range(len(score)):
		if (score[i]<7):
			low.append(i)

	c = 'background-color: aqua'
	df1 = pd.DataFrame('', index=x.index, columns=x.columns)
	m = low
	df1 = df1.mask(m, c)
	return df1





def getSummary(df):
  df_types = pd.DataFrame(df.dtypes, columns=['Data Type'])
  numerical_cols = df_types[~df_types['Data Type'].isin(['object','bool'])].index.values  
  df_types['Count'] = df.count()
  df_types['Unique Values'] = df.nunique()
  df_types['Min'] = df[numerical_cols].min()
  df_types['Max'] = df[numerical_cols].max()
  df_types['Average'] = df[numerical_cols].mean()
  df_types['Median'] = df[numerical_cols].median()
  df_types['St. Dev.'] = df[numerical_cols].std()  
  st.write('Summary:')
  st.write(df_types)

st.sidebar.title("Data Quality Portal")
analysis = st.sidebar.selectbox('Select an Option',['Explore Data','Data Quality','About the metric','Data Quality Label'])


if analysis=='Explore Data':
	st.header("Data Explorer")

	
	filename = st.file_uploader("Upload file", type=['csv','xlxs','sav'])
	if not filename:
		st.write("Upload a .csv or .xlsx file to get started")

	df = get_df(filename)

	df.to_pickle("dummy.pkl")

	if st.checkbox('Show dataframe'):
	    st.dataframe(df[:10])
	

	metafile = st.file_uploader("Upload file", type=['csv'])
	if not metafile:
		st.write("Upload a .csv file to get started")

	metadata = get_df(metafile)

	if st.checkbox('Show metadata'):
	    st.dataframe(metadata[:10])

	metadata.to_pickle("dummy_meta.pkl")

  
	transformedDf = transform(df)
	st.dataframe(transformedDf)



	getSummary(df)

	menu = df.columns
	choice = st.selectbox("Select Parameter to get more information",menu)
	temp = df[choice].describe().to_dict()
	st.subheader("Column description : "+choice)
	st.markdown("Count : "+str(temp["count"]))
	# st.markdown(temp)
	if(df[choice].dtype == "float64" or df[choice].dtype == "int" ):
		st.markdown("DataType : Numeric")
		st.markdown("Mean : "+str(temp['mean']))
		st.markdown("Standard deviation : "+str(temp['std']))
		st.markdown("Minimum Value : "+str(temp['min']))
		st.markdown("Maximum Value : "+str(temp['max']))
	else:
		st.markdown("DataType : Categorical")
		# st.markdown("Top : "+str(temp["top"]))
		# st.markdown("Top Frequency : "+str(temp["freq"]))
	
	# explore(df)



if analysis=='Data Quality':
	st.header("Data Quality")


	df = pd.read_pickle("dummy.pkl")
	metadata = pd.read_pickle("dummy_meta.pkl")

# fig = plt.subplots()
	corrMatrix = df.corr()
	# # st.markdown (corrMatrix)
	# sn.heatmap(corrMatrix)
	# st.write(fig)
	st.set_option('deprecation.showPyplotGlobalUse', False)
	if st.checkbox("Simple Correlation Plot with Matplotlib "):
		plt.matshow(df.corr())
		st.pyplot()


	st.subheader("Highly correlated columns :")
	correlatedColumns = []
	count=0
	myset = set() 
	for i in corrMatrix:
	  for j in corrMatrix:
	    temp=[]
	    if(i!=j and i not in myset and j not in myset):
	      if(corrMatrix[i][j]>0.7 and corrMatrix[i][j]<1):
	        myset.add(i)
	        myset.add(j)
	        temp.append(i)
	        temp.append(j)
	        # st.markdown(corrMatrix[i][j] )
	        count= count+1
	        correlatedColumns.append(temp)
	st.markdown(correlatedColumns)

	Correlation = ((count*2)/len(df.columns) )*100

	st.subheader("Percentage of correlated columns : " + str(Correlation))

	TotalVar = len(df.columns)

	st.subheader('Number of variables : '+str(TotalVar))

	st.subheader("Number of observations : "+str(df.shape[0]))

	MissingCells = ((df.isnull().sum().sum())/(df.shape[0]*df.shape[1]))*100

	st.subheader("% of missing cells : "+ str(MissingCells))

	# df.style.apply(highlight, axis=None).to_excel('styled.xlsx', engine='openpyxl', index=False)
	# miss_df = pd.read_excel("styled.xlsx")
	st.dataframe(df.style.apply(highlight, axis=None))


	DupicatedRows = ((df.duplicated().sum().sum())/df.shape[0])*100

	st.subheader("% of duplicated rows : "+ str(DupicatedRows))

	st.dataframe(df.style.apply(highlightDuplicate, axis=None))



	colnames_numerics_only = df.select_dtypes(include=np.number).columns.tolist()
	len(colnames_numerics_only)
	CategoricalColumns = df.shape[1]-len(colnames_numerics_only)

	st.subheader("Categorical Columns : "+str(CategoricalColumns))

	st.subheader("Continuous Columns : "+str(len(colnames_numerics_only)))


	x= df.skew(axis = 0, skipna = True).sort_values(ascending=False)
	skewedCols=x[x>9]
	

	st.subheader("Highly Skewed columns : "+str(skewedCols))

	
	Skewness = (len(skewedCols)/len(x)) *100
	st.subheader("Percentage of Skewness- "+str(Skewness))
	NonMissingCells = 100- MissingCells
	NonDuplicatedRows = 100 - DupicatedRows
	UnSkewness = 100-Skewness
	CategoricalRatio = CategoricalColumns/TotalVar
	Uncorrelation = 100 - Correlation
	



	import pandas as pd
	import textdistance
	# from String_matching import String_matching as sm
	from sklearn.feature_extraction.text import CountVectorizer
	from sklearn.metrics.pairwise import euclidean_distances,cosine_distances
	import inflect
	import nltk
	from nltk.stem import WordNetLemmatizer
	from nltk.corpus import stopwords
	from nltk.tokenize import word_tokenize
	nltk.download('stopwords')
	nltk.download('wordnet')
	nltk.download('punkt')
	sm = String_matching()
	p = inflect.engine()
	data= metadata['codebook_desc']
	similarity_metrics=[sm.lcs,sm.hamming_distance,sm.cosine,sm.smith_waterman,sm.jaccard,sm.jaro_winkler,sm.Needleman_wunsch,sm.Strcmp95,sm.gotoh,sm.sorensen_dice,sm.tversky,sm.overlap,sm.tanimoto,sm.mra,sm.editex]
	print('Trying 17 string matching metrics including edit distance, token based, sequence based and phonetic based')
	labels= metadata['dataset_desc']
	similarity_order={}
	def Sort_Tuple(tup):  
		# reverse = None (Sorts in Ascending order)  
		# key is set to sort using second element of  
		# sublist lambda has been used  
		tup.sort(key = lambda x: x[1])  
		return tup  
	temp_arr=[]
	s=0
	count=0
	def engg(article):
		article_copy = article
		stop_words = set(stopwords.words('english'))
	
	 
		article_copy = str(article_copy).lower()
		article_copy = article_copy.replace("\r"," ")
		article_copy = article_copy.replace("\n"," ")
		article_copy = article_copy.replace("   "," ")
		article_copy =article_copy.replace('“',' ')
		article_copy =article_copy.replace('”',' ')
		article_copy =article_copy.replace("’s",'')
		article_copy =article_copy.replace("_",' ')
		article_copy =article_copy.replace("/",' ')
		article_copy =article_copy.replace(".",' ')
		article_copy =article_copy.replace(",",' ')
		article_copy =article_copy.replace(":",' ')
		article_copy =article_copy.replace("?",' ')
		article_copy =article_copy.replace(";",' ')
		article_copy =article_copy.replace(">",' ')
		article_copy =article_copy.replace("-",' ')


			 
		wordnet_lemmatizer = WordNetLemmatizer()
		word_list = article_copy.split(" ")
		final_article = list()
		for word in word_list:
			final_article.append(wordnet_lemmatizer.lemmatize(word, pos ="v"))
		#print(final_article)
	#    Joining the list
		final_article = sorted(final_article)
		article_copy = " ".join(final_article) 
		word_list = word_tokenize(article_copy)
		filtered_sentence = {w for w in word_list if not w in stop_words}
		article_copy = " ".join(filtered_sentence)
		
		return filtered_sentence



	for i,j in zip(labels,data):
		x= engg(str(i))
		y=engg(str(j))
		z = x.intersection(y)
		temp1 = " ".join(z)
		temp2 = " ".join(x)
		# print("start lol")
		# print(temp1)
		# print(temp2)
		# print("end lol")
		metric_score=0
		for k in similarity_metrics:
			if k!=sm.iterative_levenshtein and k!=sm.hamming_distance and k!=sm.tanimoto:
				metric_score+=k(temp1,temp2)
			else:
				metric_score-=k(temp1,temp2)
		if(metric_score==float("inf")):
			metric_score=0
		s= s+metric_score
		count = count+1
		#print(metric_score)
		temp_arr.append(metric_score)

	print(temp_arr)

	metadata['score'] = temp_arr

	
	def highlightMeta(x):
		if x.score > 7:
			return ['background-color: white']*3
		else:
			return ['background-color: aqua']*3


	check = (s/(13*count))
	st.subheader("Metadata matching score : "+str(check*100))

	st.dataframe(metadata.style.apply(highlightMeta, axis=1))


	metadataCoupling = check*100
	dq = (0.0974 * 100) + (0.1702 * 100) + (0.1706 * 100) + (0.0835 * metadataCoupling) + (0.0727 * NonDuplicatedRows) + (0.1004 * NonMissingCells) + (0.1553 * UnSkewness) + (0.0837 * CategoricalRatio) + (0.0658 * Uncorrelation)
	
	st.subheader("Data Quality Score : "+str(dq))
	
	# print("Percentage out of 40 : ",(check*40))
	    

	import csv
	with open('label.csv', 'w', newline='') as file:
	    writer = csv.writer(file)
	    writer.writerow(["Dataset : ", filename])
	    writer.writerow(["Data Quality Parameter", "Score"])
	    writer.writerow(["Provenance", "100"])
	    writer.writerow(["Uniformity", "100"])
	    writer.writerow(["Metadata Coupling",str(check*100) ])
	    writer.writerow(["Dataset Characteristics", "100"])
	    writer.writerow(["Categorical Columns wrt all columns", CategoricalRatio])
	    writer.writerow(["Percentage of Missing Values", str(df.isnull().sum().sum()/(df.shape[0]*df.shape[1])*100)])
	    writer.writerow(["Percentage of duplicate values", str(df.duplicated().sum().sum()/df.shape[0]*100)])
	    writer.writerow(["Percentage of Skewness",Skewness])
	    writer.writerow(["Correlation", str(Correlation)])
	    writer.writerow(["Data Quality : ",dq])





if analysis=='About the metric':
# column_names= pd.read_csv(metafile) 
# st.markdown(df.columns)
	
	st.title("Data Quality Metric")
	st.subheader("Data Quality Parameters")
	st.image("ingredients.png",width = 700)
	
	

	menu = ["Provenance","Un 13, iformity","Dataset Characteristics","Metadata Coupling","Statistics","Correlations","Inconsistency"]
	choice = st.selectbox("Select Parameters",menu)

	if choice =="Provenance":
		st.subheader("Provenance")
		st.markdown("Provenance is the chronology of the ownership or location of a particular object. It refers to the personal information related to the dataset which specifies the origin, author, version and date uploaded of that particular dataset. While extracting the dataset, we cross-referenced the information regarding these parameters of the dataset and verified them with the ones retrieved from the metadata. ")
	
	elif choice =="Uniformity":
		st.subheader("Uniformity")
		st.markdown("All columns should have all the data values similar in datatypes.")
		st.markdown("The values of mean, median, mode, max and min should match the description given in the metadata and the one calculated from the dataset.")	

	elif choice =="Dataset Characteristics":
		st.subheader("Dataset Characteristics")
		st.markdown("This should match the details given in the metadata.")
		st.markdown("1.  Number of observation")
		st.markdown("2. Number of variables")
		st.markdown("3. Size of the dataset ")
	
	elif choice =="Metadata Coupling":
		st.subheader("Metadata Coupling")
		st.markdown("One of our main focuses was that the documentation of the dataset should be neatly and properly defined. The similarity between the column descriptions in metadata and the dataset is calculated to see if they correspond to the same information")
		st.markdown("1.Preprocessing data: Both the column descriptions from metadata and the recode manual are preprocessed using features of the NLTK library in python. In this process, the data is converted to lowercase, all the special characters and integers are removed. Further, stemming and lemmatization is carried out to get a complete understanding of the description and generate keywords and stopwords.")
		st.markdown("2.Similarity score calculation: Thirteen text similarity algorithms help calculate the similarity score, which is further normalized to values between 0 and 1. This normalisation makes the different algorithms at par with each other which facilitates analysis. After this normalization, we classify each result as similar or not similar based on the algorithm and generate thirteen values of 0 and 1 where 0 represents low similarly and 1 represents high similarity. These scores are finally averaged to generate the metadata matching score.")
		st.markdown("3.Results: For each algorithm, the results 1 and 0 values being averaged help us understand the similarity of the metadatas in a more generic manner and removes all biases.  The highest similarity value is 13, and the lowest is 0. The final percentage of metadata matching is calculated based on this score.")
		
	elif choice =="Statistics":
		st.subheader("Statistics")
		st.markdown("Statistical Modelling in order to adjudge the data quality are :")
		st.markdown("1. Percentage of Missing Values") 
		st.markdown("2. Percentage of duplicate values")
		st.markdown("3. Skewness of the data.")

	elif choice =="Correlations":
		st.subheader("Correlations")
		st.markdown("Our study uses the Pearson Correlation model to generate the correlation heatmap plots for the data. The columns resulting in high correlations should be taken into account and their interpretation should be handled separately.")
		st.markdown("Our system includes these highly correlated columns in the comprehensive report published to the end-user.")
		st.markdown("Pearson Correlation plots are also provided in the comprehensive report")
	
	elif choice =="Inconsistency":
		st.subheader("Inconsistency")
		st.markdown("The highly correlated columns are analyzed individually and inconsistencies are taken into account by the following ways : ")
		st.markdown("1. Comparing the distribution of data in the dataset with the census data.")
		st.markdown("2. If two or more columns are interdependent they must correspond to the similar information.")
		st.markdown("3. If two columns are highly correlated they must have a strong relation and should also match when checked.")

	st.subheader("Process of Calculating Data Quality")
	st.image("btp.png",width = 700)



if analysis=='Data Quality Label':

	st.title("Data Quality Nutrition Label ")

	label = pd.read_csv("label.csv")

	st.dataframe(label)


	st.image("Label.png",width=500)

