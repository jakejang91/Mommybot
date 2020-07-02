from sklearn.ensemble import RandomForestRegressor
import pickle
import pandas as pd
## TODO: Prediction Model Loading

class TimePredictor():
    
    def __init__(self):
        self.model_1, self.model_2 = self.loadTimePredictionModel()
        print(self.model_1)
        print(self.model_2)
    
    
    def loadTimePredictionModel(self):
        data = []
        with open("timemodel1.pickle","rb") as fr:
            data = pickle.load(fr)
        model1 = data
        
        with open("timemodel2.pickle","rb") as fr:
            data = pickle.load(fr)
        model2 = data
        
        
        return model1, model2
    
    
    def getPredictedTime(self, data = [], variable = ""):
        
        if variable == "t1-2":
            print("now predict t1-2")
            try:
                print("the input data is :" +str(data))
                temp = pd.DataFrame(columns = ['t1-1', 't2-1', 't2-2', 't3'])
                temp.loc[0] = data
                print(temp.head())
                pred_y = self.model_1.predict(temp)
                return pred_y
            except:
                print("Predict Error")
        elif variable == "t1-3":
            print("now predict t1-3")
            try:
                print("the input data is :" +str(data))
                temp = pd.DataFrame(columns = ['t1-1','t1-2', 't2-1', 't2-2', 't3'])
                temp.loc[0] = data
                print(temp.head())
                pred_y = self.model_2.predict(temp)
                return pred_y
            except:
                print("Predict Error")
        
        pred_y = "Error"
        return pred_y
        
    
    
    
print("Module Loaded : time predictor")