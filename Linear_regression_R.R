# Linear_Regression with R

# data: statedata.csv
# libraries:
#	psych
#	

# 1. import the file 
statedata = read.csv("statedata.csv")

# 2. Basic analysis
str(statedata)
summary(statedata)
max(statedata$varDep)
names(statedata)
tapply(statedata$varDep, statedata$var!, mean)
sort(statedata$var1)
sort(abs(statedata$var1))
which.min(statedata$va1, statedata$var2)
summary(statedata$var1, statedata$var2)
table(statedata$var1, statedata$var2)

# graphs
plot(statedata$varDep, statedata$var1)
hist(statedata$varDep)
boxplot(statedata$varDep ~ var4)

# remove missing data
statedata <- na.omit(statedata)

# calculated variables
statedata$newVar <- statedata$var1 + statedata$var2

statedata$var1 <- relevel(statedata$var1, "White")

# Time Series Model - ex. var (n-2)
var1lag2 <- lag(zoo(dataTest$var1), -2, na.pad = TRUE
dataTest$var1lag2 <- coredata(var1lag2)

# As Factor
statedata$month1 <- as.factor(statedata$month)



# 3. Split the file in train and test
dataTrain = subset(statedata, statedata$var1 <= 2005)
dataTest = subset(statedata, statedata$var1 > 2005)

dataTrain = subset(statedata, statedata$var1 == max(statedata$var1))
dataTest = subset(statedata, statedata$var1 != max(statedata$var1))

dataTrain = subset(statedata, statedata$var5 == "ABC"))

str(dataTrain)
str(dataTest)

# 4. Correlations
cor(statedata)
cor(statedata$varDep, statedata$var1)

cor(dataTrain, use = "everything")

# 5. Factorial Analysis


 
# 6. Regression Model
modelA <- lm(varDep ~ V1 + V2 + V3 + V4, data = dataTrain)
#	modelA <- lm(varDep ~ ., data = dataTrain)
#	ex - monthly data - month as factor
#		modelB <- lm(varDep ~ v1 + v2 + v3 + v4 + month1, data = dataTrain)
summary(modelA)

modelA$residuals
sort(abs(residuals)
# the best model - min SSE - sum of squered errors - but depends on N
SSE = sum(modelA$residuals^2)
SSE
# Root-Mean-Square-Error
RMSE = sqrt(SSE/nrow(statedata))
RMSE
# Automatically Building the Model 
stepmodel <- step(modelA)
# AIC - to be done
 
# 7. Prediction
predTest <-predict(modelA, newdata = dataTest)
predTest
sort(predTest)
str(predTest)
summary(predTest)
SSE = sum((dataTest$varDep - predTest)^2)
SSE
SST = sum((dataTest$varDep - mean(statedata$varDep))^2)
SST
# R2 - captures the value added from using a model
R2 = 1-SSE/SST
R2
RMSE = sqrt(SSE/nrow(dataTest))
RMSE

predTest2 <-predict(stepmodel, newdata = dataTest)
SSE = sum((predTest2 - dataTest$varDep)^2)
SSE
SST = sum((mean(dataTrain$varDep)-dataTest$varDep)^2)
R2 = 1-SSE/SST
R2






