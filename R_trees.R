# R - Trees 

############################################
#  			 WORK IN PROGRESS  			   #
############################################

# Optimal Classification Trees - TBD
	# OCT - trees with parallel solits (1 var per split)
	# OCT-H - trees with hyperplane spliits (can use multiple variables per split if beneficial)
# XGBoost	
	
# yes response is always to the left 
# no response is always to the right.

# Packages
library(caTools)
library(rpart)
library(rpart.plot)
library(ROCR)
library(randomForest)
library(caret)
library(e1071)

# 1. import the file 


# 2. Basic analysis
#	


# 3. Split the file in train and test


# 4. Correlations


# 5. Factorial Analysis


 
# 6. Tree 

# Baseline method - same results as (n-1)
table(Test$bucket2009, Test$bucket2008)
(x1 + x2 + x3 + x4 + x5)/nrow(Test)


# rpart package - CART model
	# test with different minibucket values - number of data points in each subset.
stevenstree <- rpart(Reverse ~ Circuit + Issue + Petitioner + Respondent + LowerCourt + Unconst, data = trainset, method = "class", minbucket = 25)
prp(stevenstree)
summary(stevenstree)

	# cp value, no minibucket - cp = 0.00005 - result of a crossvalidation - see the first lecture to calculate it
stevenstree <- rpart(Reverse ~ Circuit + Issue + Petitioner + Respondent + LowerCourt + Unconst, data = trainset, method = "class", cp = 0.0005)
prp(stevenstree)
summary(stevenstree)


# random forest package - less interpretable but more accurate; ntree = 200 -> 200 trees will be created
stevensforest <- randomForest(Reverse ~ Circuit + Issue + Petitioner + Respondent + LowerCourt + Unconst, data = trainset, nodessize = 25, ntree = 200)
	# convert outcome to factor 
	Train$Reverse = as.factor(Train$Reverse)
	Test$Reverse = as.factor(Test$Reverse)
	# try again with factors
	stevensforest <- randomForest(Reverse ~ Circuit + Issue + Petitioner + Respondent + LowerCourt + Unconst, data = trainset, nodessize = 25, ntree = 200)


# caret + e1071 packages
numFolds <- trainControl(method = "cv", number = 10)  # cv=cross-validation
cpGrid <- expand.grid( .cp = seq(0.01, 0.5, 0.01))	# ex code:    cpGrid = expand.grid( .cp = (0:10)*0.001)
  # cp = complexity parameter; smaller cp -> bigger tree (might overfit)
	# cross-validation
tr = train(Reverse ~ Circuit + Issue + Petitioner + Respondent + LowerCourt + Unconst, data = train, method = "rpart", trControl = numFolds, tuneGrid = cpGrid)
tr
	# create the new CART model with the cp parameter found in cross-validation !!!!!!
	# extract tree
best.tree = tr$finalModel
prp(best.tree)


# penalty matrix
penaltymatrix = matrix(c(0,1,2,3,4,2,0,1,2,3,4,2,0,1,2,6,4,2,0,1,8,6,4,2,0),byrow=TRUE, nrow = 5)
penaltymatrix
	# penalty error of Baseline method
as.matrix(table(claimstest$bucket2009, claimstest$bucket2008))*penaltymatrix
sum(as.matrix(table(claimstest$bucket2009, claimstest$bucket2008))*penaltymatrix)/nrow(claimstest)


# new CART model with loss matrix - add parms = list... in order to force a different tree split
claimsTree = rpart(bucket2009 ~ age + alzheimers + arthritis + cancer + copd + depression + diabetes + heart.failure + ihd + kidney + osteoporosis + stroke + reimbursement2008 + bucket2008, data = claimstrain, method = "class", cp = 0.00005, parms = list(loss=penaltymatrix))
prp(claimsTree)

	
	
# 7. Prediction

# rpart package - CART model
predictcart <- predict(stevenstree, newdata = testset, type = "class")
table(testset$Reverse, predictcart)
(41+71)/(41+22+36+71)


# ROCR package
predictROC <- predict(stevenstree, newdata = testset)
predictROC
pred = prediction(predictROC[,2], Test$Reverse)
	# tpr = true positive rate
	# fpr = false positive rate
perf = performance(pred, "tpr", "fpr")
plot(perf)


# with penalty error
as.matrix(table(claimstest$bucket2009, predicttest))*penaltymatrix
sum(as.matrix(table(claimstest$bucket2009, predicttest))*penaltymatrix)/nrow(claimstest)


# ROCR package
pred <- prediction(predictROC[,2], testset$Reverse)
perf <- performance(pred, "tpr", "fpr")
plot(perf)
	# AUC
as.numeric(performance(pred, "auc")@y.values)


# randomForest package - as.factor on dependent variable
predictforest <- predict(stevensforest, newdata = testset)
table(testset$Reverse, predictforest)
	# accuracy
(34+82)/(34+43+11+82)


# Predictions with penalty error - add parms = list... in order to force a different tree split
	# normal predict
predicttest = predict(claimsTree, newdata = claimstest, type = "class")
table(claimstest$bucket2009, predicttest)
(94310+18942+4692+636+2)/nrow(claimstest)
	# with penalty
sum(as.matrix(table(claimstest$bucket2009, predicttest))*penaltymatrix)/nrow(claimstest)

(114141+18409+8027+3099+351)/nrow(claimstest)

(94310+7176+3590+1304+135)/nrow(claimstest) # with loss parameter


# Predictions - caret et 21071 (tree crossvalidation)
best.tree.pred = predict(best.tree, newdata = test1, type = "class")
table(test$reverse, best.tree.pred)
	# accuracy
best.tree.sse = sum((best.tree.pred - test1$MEDV)^2)
best.tree.sse