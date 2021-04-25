class KnnClassification:
  def __init__(self,path, TargetAtLast):
    self.path = path
    self.TargetAtLast = TargetAtLast
        
  def loadToList(self):
    from numpy import genfromtxt
    dataset = genfromtxt(self.path, delimiter=',')
    DataList = dataset.tolist()
    import random
    random.shuffle(DataList)
    return DataList
  def list_split(self, DataList):
    Train_set=[]
    Val_set=[]
    Test_set=[]
    from random import random
    for x in DataList:
      R = random()
      if R >= 0 and R <= 0.7:
        Train_set.append(x)
      elif R >= 0.7 and R <= 0.85:
        Val_set.append(x)
      else:
        Test_set.append(x)
    return Train_set, Val_set, Test_set
  def knn(self, Val_set, Train_set, k):
    from scipy.spatial import distance
    import operator
    correct = 0
    for s in Val_set:
      ValueDict = {}
      for v in Train_set:
        if self.TargetAtLast :
              ed = distance.euclidean(s[:(len(s)-1)], v[:(len(v)-1)])
        else:
              ed = distance.euclidean(s[1:], v[1:])
        ValueDict[ed] = v
      sorted_L = sorted(ValueDict.keys())
      count = 1
      ClassDict = {}
      for x in sorted_L:
        if self.TargetAtLast :
          if int(ValueDict[x][-1]) in ClassDict.keys(): 
            ClassDict[int(ValueDict[x][-1])] = ClassDict[int(ValueDict[x][-1])]+1
          else:
            ClassDict[int(ValueDict[x][-1])] = 0
            ClassDict[int(ValueDict[x][-1])] = ClassDict[int(ValueDict[x][-1])]+1
          count = count + 1
          if(count > k):
            break
        else:
          if int(ValueDict[x][0]) in ClassDict.keys(): 
            ClassDict[int(ValueDict[x][0])] = ClassDict[int(ValueDict[x][0])]+1
          else:
            ClassDict[int(ValueDict[x][0])] = 0
            ClassDict[int(ValueDict[x][0])] = ClassDict[int(ValueDict[x][0])]+1
          count = count + 1
          if(count > k):
            break
      val = max(ClassDict.items(), key=operator.itemgetter(1))[0]
      if self.TargetAtLast:
        if(int(s[-1]) == val):
          correct = correct + 1
      else:
        if(int(s[0]) == val):
          correct = correct + 1
    accuracy = (correct/len(Val_set))*100
    return accuracy
