import pandas as pd
#(pip install pandas)
#df = pd.read_csv("c1.csv") #Location of CSV DataFrame
df = pd.read_excel("c1.xlsx") #Location of Excel DataFrame (pip install openpyxl)

newlist = []

def detailedIndex(list1): #This function prints value of each row for our column as long as index is a string. Note that empty cells in df has type of "float" represented as "nan".
        for i in range(len(list1)):
            if type(list1[i]) == str:                       
                print(f"{i+1}=", list1[i]) #My document got info details at first row and indexing starts from 0, this is why we add +1 to i. Which you can change on your benefit.
            else:
                continue
        

def columnPicker(df, colNum, list1): # This function stores all values belong to the given column as a Series type. Index starts with 0.
    category = df.iloc[:, colNum] 
    counter = category.value_counts()
    list1 = category.tolist() #Turning Series type into List type. (This is necessary for easy manupilation)
    print("Topic = ", counter) #This line prints which topic currently we are working on and counts each different countables on given column
    return list1
    
newlist = columnPicker(df, 2, newlist)
detailedIndex(newlist)


