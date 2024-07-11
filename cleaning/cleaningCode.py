
import pandas as pd


class  Reading : 

    def __init__(self, df):
        self.df = df
        
        
    def read_json (self):
        self.df = pd.read_json('final_dataset.json')

        return self.df.head()
    
    def exploring_data (self):

        self.df.shape
        self.df.info()
        self.df.describe()

        return self.df.shape, self.df.info() and self.df.describe()
    
class Cleaning :

    def __init__(self,df):

        self.df = df
    
    def delete_blanks (self):
        for i in self.df :

            self.df['Url'] = self.df['Url'].str.strip()
            self.df['Country'] = self.df['Country'].str.strip()
            self.df['District'] = self.df['District'].str.strip()
            self.df['FloodingZone'] = self.df['FloodingZone'].str.strip()
            self.df['Kitchen'] = self.df['Kitchen'].str.strip()
            self.df['Locality'] = self.df['Locality'].str.strip()
            self.df['PEB'] = self.df['PEB'].str.strip()
            self.df['Province'] = self.df['Province'].str.strip()
            self.df['Region'] = self.df['Region'].str.strip()
            self.df['StateOfBuilding'] = self.df['StateOfBuilding'].str.strip()
            self.df['SubtypeOfProperty'] = self.df['SubtypeOfProperty'].str.strip()
            self.df['TypeOfSale'] = self.drop_duplicatesdf['TypeOfSale'].str.strip()

        return i and self.df.shape
    
    delete_blanks()

    def drop_duplicates (self):
        
        self.df.drop_duplicates('Url',  inplace = True)

        return self.df
    

    drop_duplicates()
    

    def fill_numerical(self):

        for i in self.df :

            self.df.fillna({'BathroomCount': df['BathroomCount'].median(),
                 'ConstructionYear': df['ConstructionYear'].median(),
                 'GardenArea': df['GardenArea'].median(),
                 'LivingArea': df['LivingArea'].median(), 
                 'MonthlyCharges': df['MonthlyCharges'].median(), 
                 'NumberOfFacades': df['NumberOfFacades'].median(), 
                 'RoomCount': df['RoomCount'].median(), 
                 'ShowerCount': df['ShowerCount'].median(), 
                 'SurfaceOfPlot': df['SurfaceOfPlot'].median(), 
                 'ToiletCount': df['ToiletCount'].median()
                 })
            
            return i and self.df.shape
        
    def fill_non_numerical(self):
        
        for i in self.df:

            self.df.fillna({'FloodingZone': self.df['FloodingZone'].mode()[0],
                'Country': self.df['Country'].mode()[0], 
                'District': self.df['District'].mode()[0], 
                'Kitchen': self.df['Kitchen'].mode()[0], 
                'Locality': self.df['Locality'].mode()[0], 
                'PEB': self.df['PEB'].mode()[0], 
                'Province': self.df['Province'].mode()[0], 
                'Region': self.df['Region'].mode()[0], 
                'StateOfBuilding': self.df['StateOfBuilding'].mode()[0], 
                'SubtypeOfProperty': self.df['SubtypeOfProperty'].mode()[0], 
                'TypeOfSale': self.df['TypeOfSale'].mode()[0],
                'Fireplace': self.df['Fireplace'].mode()[0],
                'Furnished': self.df['Furnished'].mode()[0],
                'SwimmingPool': self.df['SwimmingPool'].mode()[0], 
                'Terrace': self.df['Terrace'].mode() [0],
                'Garden': self.df['Garden'].mode() [0]
                 })
            

            return i and self.df.shape
        
    fill_non_numerical()

    def round_numerical (self):


        for i in self.df:

            self.df[['BathroomCount','ConstructionYear',
                'Fireplace','Furnished','GardenArea','LivingArea',
                'MonthlyCharges','NumberOfFacades','RoomCount',
                'ShowerCount','SurfaceOfPlot','SwimmingPool',
                'ToiletCount','Terrace']].astype(int)
            
            return i and self.df.shape
        
    round_numerical()


    def filter_outlier (self):

        for i in self.df :

            self.df.drop(self.df[self.df.BathroomCount > self.df.BedroomCount].index,inplace=True)
            self.df.drop(self.df[self.df.ConstructionYear > 2033].index,inplace=True)
            self.df.drop(self.df[self.df.GardenArea > self.df.SurfaceOfPlot].index,inplace=True)
            self.df.drop(self.df[self.df.PostalCode < 1000].index,inplace=True)
            self.df.drop(self.df[self.df.NumberOfFacades > 4].index,inplace=True)
            self.df.drop(self.df[self.df.Price > 15000000].index,inplace=True)
            self.df.drop(self.df[self.df.ToiletCount > 58].index,inplace=True)
            self.df.drop(self.df[self.df.ShowerCount > 58].index,inplace=True)
            self.df.drop(self.df[self.df.TypeOfSale == "annuity_monthly_amount"].index,inplace=True)
            self.df.drop(self.df[self.df.TypeOfSale == "annuity_without_lump_sum"].index,inplace=True)
            self.df.drop(self.df[self.df.TypeOfSale == "annuity_lump_sum"].index,inplace=True)

            return i and self.df.shape    

    filter_outlier()


    class Create_csv :


        def __init__(self):

            self.df = df

        def create_csv(self):

    





