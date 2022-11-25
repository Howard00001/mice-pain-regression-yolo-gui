import numpy as np
import scipy.spatial.distance as dist
from sklearn import preprocessing
import os

def go(filepath, normtype, diveye, distype, getfiles = 0):
    if getfiles == 0:
        test_loc = get_raw(filepath)
    else:    
        test_loc = np.zeros([5,0,2])
        if getfiles == 1:
            sample = "health_base"
        elif getfiles == 2:
            sample = "pain_base"
        elif getfiles == 3:
            sample = "1hr"
        elif getfiles == 4:
            sample = "2hr"
        else:
            sample = "3hr"
        for fp in filepath:
            for file in os.listdir(fp):
                if not (file.find(sample) == -1):
                    csvfile = fp + file
            tmp = get_raw(csvfile)
            test_loc = np.concatenate([test_loc,tmp],1)
    
    # count distances
    test = []
    
    if distype == 0:### mahalanobis
        for i in range(5):
            for j in range(i + 1, 5):
                a = []
                X = np.vstack([test_loc[i],test_loc[j]])
                V = np.cov(X.T)
                VI = np.linalg.inv(V)
                # health sample
                for k in range(test_loc.shape[1]):
                    a.append(dist.mahalanobis(test_loc[i][k].T,test_loc[j][k].T,VI))
                test.append(a)
        test = np.array(test).T

    if distype == 1:### euclidean
        for i in range(5):
            for j in range(i+1, 5):
                a = []
                for k in range(test_loc.shape[1]):
                    a.append(dist.euclidean(test_loc[i][k],test_loc[j][k]))
                test.append(a)
        test = np.array(test).T

    # normalize
    if diveye == 1:## divide eye
        test[:,:10] = test[:,:10] / test[:,0,None]
    ## min max
    min_max_scale = preprocessing.MinMaxScaler()
    if normtype == 0:### col
        test = min_max_scale.fit_transform(test)
    if normtype == 1:### row
        test = min_max_scale.fit_transform(test.T).T
    if normtype == 2:##self defined normalize
        test = norm1(test, 10, 0)
    
    return test

def get_raw(filepath):
    test_raw = np.loadtxt(filepath, delimiter=',', skiprows=1, dtype='int_')
    test_loc = np.array([np.vstack([test_raw[:,0],test_raw[:,1]]).T, np.vstack([test_raw[:,2],test_raw[:,3]]).T,
                        np.vstack([test_raw[:,4],test_raw[:,5]]).T, np.vstack([test_raw[:,6],test_raw[:,7]]).T,
                        np.vstack([test_raw[:,8],test_raw[:,9]]).T])
    return test_loc

def norm1(test,ds,ag): # min max keep shape 
    if ds!=0:
        dsAll = test[:,:ds]
        dsmin = np.min(dsAll)
        dsmax = np.max(dsAll)
        test[:,:ds] = (dsAll) /dsmax
    if ag!=0:
        agAll = test[:,ds:ds+ag]
        agmin = np.min(agAll)
        agmax = np.max(agAll)
        test[:,ds:ds+ag] = (agAll)/agmax
    return test

def scoreCFA(health, pain, test):
    # health-pain distance
    effect1 = abs(np.median(health) - np.median(pain))
    # variance
    # effect2 = np.var(health)+np.var(pain)
    # for i in range(len(test)):
    #     effect2 += np.var(test[i])
    # effect2 = 1/(0.1+effect2)
    # tendency
    effect3 = np.median(test[0])-np.median(test[1])+np.median(test[0])-np.median(test[2])
    # sum
    print("1: "+ str(effect1))
    # print("2: "+ str(effect2))
    print("3: "+ str(effect3))
    return effect1 + effect3

# def scoreCFA0(health, pain, test):
#     # health-pain
#     effect1 = abs(np.median(health) - np.median(pain))/(0.1+np.var(health)+np.var(pain))
#     # test variance
#     effect2 = 0
#     for i in range(len(test)):
#         effect2 += np.var(test[i])
#     effect2 = 1/(0.1+effect2)
#     # tendency
#     effect3 = np.median(test[0])-np.median(test[1])+np.median(test[1])-np.median(test[2])
#     # sum
#     print("1: "+ str(effect1))
#     print("2: "+ str(effect2))
#     print("3: "+ str(effect3))
#     return effect1 + effect3/effect2

# def score(health,pain,test,painIndex=[], healthIndex=[]):
#     effect1 = abs(np.median(health) - np.median(pain))/(0.1+np.var(health)*np.var(pain))
#     effect2 = 0
#     for i in range(len(test)):
#         effect2 += 1/(np.var(test[i])+0.1)
#     return effect1+effect2

# def score(health,pain,test,painIndex=[], healthIndex=[]):
#     effect3 = 0
#     for i in range(len(painIndex)):
#         effect3 -= abs(-1-np.median(test[painIndex[i]]))
#     effect4 = (np.median(health)-1) + (-1-np.median(pain))
#     effect1 = (effect3+effect4)/(0.1+np.var(health)*np.var(pain))
#     effect2 = 0
#     for i in range(len(test)):
#         effect2 += 1/(np.var(test[i])+0.1)
#     return effect1+effect2

# def score(health, pain, test, painIndex=[], healthIndex=[]):
#     pm = np.median(pain)
#     effect1 = np.median(health) - 1
#     if effect1 > 0:
#         effect1 = 0
#     effect2 = -1 - pm
#     if effect2 > 0:
#         effect2 = 0
#     effect3 = 0
#     for i in range(len(painIndex)):
#         add = -np.median(test[painIndex[i]])
#         if add > 0:
#             add = 0
#         effect3 += add
#     return effect1+effect2+effect3