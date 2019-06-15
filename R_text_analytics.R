# Text Analytics with R

# data: statedata.csv
# libraries:
# 	tm
# 	SnowballC	
#	+ Trees libraries - rpart
#					  - rpart.plot
#					  - randomForest
#					  - ROCR
#	+ caTools
################################################################
# 1. import the file 
################################################################

statedata = read.csv("statedata.csv",  header = TRUE)


################################################################
# 2. Basic analysis
################################################################
str(tweets)
tweets$negative <- as.factor(tweets$Avg <= -1)
table(tweets$negative == "TRUE")	








################################################################ 
# 3. Text Analysis
################################################################

# Create corpus
corpus = VCorpus(VectorSource(emails$email))
corpus[[1]]$content

# Pre-process data
corpus = tm_map(corpus, content_transformer(tolower))   	# convert to lower case
corpus = tm_map(corpus, removePunctuation)					# remove punctuation
corpus = tm_map(corpus, removeWords, stopwords("english"))  # stop words 
corpus = tm_map(corpus, stemDocument)						# stem document

#####
stopwords("english")[1:10]
stopwords("french")[1:10]
stopwords("romanian")[1:10]
#####

# Look at first email
corpus[[1]]$content

# Create matrix
dtm = DocumentTermMatrix(corpus)
dtm

# Remove sparse terms										# remove sparse terms
inspect(dtm[1000:1005,505:515])
findFreqTerms(dtm, lowfreq=20)

dtm = removeSparseTerms(dtm, 0.97)
dtm

# Convert to data frame										# do this part all the time you do text analysis
labeledTerms = as.data.frame(as.matrix(dtm))

# Make all variable names R-friendly						# do this part all the time you do text analysis
colnames(labeledTerms) = make.names(colnames(labeledTerms))

# Add in the outcome variable								# do this part all the time you do text analysis
labeledTerms$responsive = emails$responsive
str(labeledTerms)

# Split the data - library(caTools)
set.seed(144)
spl = sample.split(labeledTerms$responsive, 0.7)

train = subset(labeledTerms, spl == TRUE)
test = subset(labeledTerms, spl == FALSE)

# Build a CART model
library(rpart)
library(rpart.plot)
emailCART = rpart(responsive~., data=train, method="class")
prp(emailCART)

# Random forest model
library(randomForest)
set.seed(123)

tweetRF = randomForest(Negative ~ ., data=trainSparse)


 
################################################################
# 4. Prediction - see Tree code for details
################################################################
pred = predict(emailCART, newdata=test)
pred[1:10,]
pred.prob = pred[,2]
# Compute accuracy
table(test$responsive, pred.prob >= 0.5)
# Baseline model accuracy
table(test$responsive)

######################################################
# ROC curve

library(ROCR)
predROCR = prediction(pred.prob, test$responsive)
perfROCR = performance(predROCR, "tpr", "fpr")
plot(perfROCR, colorize=TRUE)
# Compute AUC
performance(predROCR, "auc")@y.values

######################################################
# RandomForest

predictRF = predict(tweetRF, newdata=testSparse)
table(testSparse$Negative, predictRF)
# Accuracy:


