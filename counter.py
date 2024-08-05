import pandas as pd
#(pip install pandas)
df = pd.read_csv("Correction_Check_3-4.csv") #Location of CSV File
#df = pd.read_excel("c1.xlsx") #Location of Excel File (pip install openpyxl)
cat = df.iloc[:, 2]
cat2 = df.iloc[:, 3]

#a = pd.concat([cat, cat2]).reset_index()

#a.dropna(how='any', inplace=True)

#print(a)





#print("sum =" ,cat.value_counts().sum())
newlist = []
newlist2 = []
newlist3 = []
def detailedIndex(list1): #This function prints value of each row for our column as long as index is a string. Note that empty cells in df has type of "float" represented as "nan".
        for i in range(len(list1)):
            if type(list1[i]) == str:                       
                print(f"{i+1}=", list1[i]) #My document got info details at first row and indexing starts from 0, this is why we add +1 to i. Which you can change on your benefit.
            else:
                continue
        

def columnPicker(df, colNum, list1): # This function stores all values belong to the given column as a Series type. Index starts with 0.
    category = df.iloc[:, colNum] 
    counter = category.value_counts()
    df2 = pd.DataFrame(counter)
    df2.to_csv('a.csv')
    list1 = category.tolist() #Turning Series type into List type. (This is necessary for easy manupilation)
    print("Topic = ", counter) #This line prints which topic currently we are working on and counts each different countables on given column
    return list1
    
#newlist = columnPicker(df, 2, newlist)
#newlist2 = columnPicker(df, 3, newlist)
#detailedIndex(newlist)



               
#detailedIndex(newlist2)


newlist = columnPicker(df, 3, newlist)
print(newlist)

