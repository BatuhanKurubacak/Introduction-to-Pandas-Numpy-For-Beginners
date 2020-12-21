import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor 




#Random Forest Regression
data=pd.read_csv('positions.csv')

level_rand=data.iloc[:,1:2].values.reshape(-1,1)
salary_rand=data.iloc[:,2].values.reshape(-1,1)

regression=RandomForestRegressor(n_estimators=10,random_state=0)
regression.fit(level_rand,salary_rand)

tahmin=regression.predict(np.array([[8.5]]))
plt.scatter(level_rand,salary_rand,color='red')
x=np.arange(min(level_rand),max(level_rand),0.01).reshape(-1,1)
plt.plot(x,regression.predict(x),color='green')
plt.xlabel('Level')

plt.title('Random Forest Regressor')
plt.show()


