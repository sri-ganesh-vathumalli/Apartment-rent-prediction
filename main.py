import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
datasets={'Brooklyn':'brooklyn.csv','Queens':'queens.csv','Manhattan':'manhattan.csv'}
class Model:
    def __init__(self):
        self.mlr=LinearRegression()
        self.rfr=RandomForestRegressor(n_estimators = 10, random_state = 0)
    def train_model(self,city):
        self.dataset=datasets[city]
        self.df=pd.read_csv(self.dataset)
        self.X=self.df[['bedrooms', 'bathrooms',
       'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee',
       'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator',
       'has_dishwasher', 'has_patio', 'has_gym']]
        self.Y=self.df[['rent']]
        x=self.X.values
        y=self.Y.values
        x_train,x_test,y_train,y_test=train_test_split(self.X,self.Y,train_size=0.9,test_size=0.1,random_state=6)
        x1,x2,y1,y2=train_test_split(x,y,train_size=0.9,random_state=6)
        self.rfr.fit(x1,y1.reshape(-1,1))
        self.mlr.fit(x_train,y_train)
        return self.mlr.score(x_train,y_train),self.rfr.score(x1,y1.reshape(-1,1))

    def predict(self,options):
        pred1=self.mlr.predict([options])
        pred2=self.rfr.predict([options])
        return pred1[0],pred2[0]




    
