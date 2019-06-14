# R - Clustering


############################################
#  			 WORK IN PROGRESS  			   #
############################################


# Packages
library(flexclust)

# 1. import the file 

########################################################
# 2. Basic analysis
########################################################
# MRI clustering	
healthyMatrix = as.matrix(healthy)
str(healthyMatrix)
# Plot image
image(healthyMatrix,axes=FALSE,col=grey(seq(0,1,length=256)))

# 3. Split the file in train and test


# 4. Correlations


# 5. Factorial Analysis

########################################################
# 6. Clusters
########################################################
# Hierarchial clustering
########################################################

# Compute distances
distances = dist(movies[2:20], method = "euclidean") # var 2-20


# Hierarchical clustering
clusterMovies = hclust(distances, method = "ward.D") 

# Plot the dendrogram
plot(clusterMovies)
rect.hclust(clusterMovies, k = 3, border = "red")
abline(h=400, col = "blue")

# Assign points to clusters
clusterGroups = cutree(clusterMovies, k = 10)
table(clusterGroups)

# Analize the results
tapply(movies$Action, clusterGroups, mean)
tapply(movies$Romance, clusterGroups, mean)

# Plot the image and the clusters - image clustering
dim(flowerClusters) = c(50,50)
image(flowerClusters, axes = FALSE)

###############################################
# As.vector - images
###############################################
flowerMatrix = as.matrix(flower)
str(flowerMatrix)
flowervector = as.vector(flowerMatrix)
str(flowervector)
flowervector2 = as.vector(flower)
str(flowervector2)

distance = dist(flowervector, method = "euclidean")
clusterIntensity = hclust(distance, method = "ward.D")
plot(clusterIntensity)
rect.hclust(clusterIntensity, k=3, border = "red")
flowerClusters = cutree(clusterIntensity, k=3)
flowerClusters
tapply(flowervector, flowerClusters, mean)
dim(flowerClusters) = c(50,50)
image(flowerClusters, axes=FALSE)
image(flowerMatrix, axes=FALSE, col = grey(seq(0,1,length=256)))


###############################################
# k-means
###############################################
# Specify number of clusters
k = 5

# Run k-means
set.seed(1)
KMC = kmeans(healthyVector, centers = k, iter.max = 1000)
str(KMC)
KMC$centers[2]
table(KMC$cluster)
table(cGroups, KMC$cluster)
#	cGroups - cutree(clusterGroups, k=...)
# Extract clusters
healthyClusters = KMC$cluster
KMC$centers[2]

# Plot the image with the clusters
dim(healthyClusters) = c(nrow(healthyMatrix), ncol(healthyMatrix))

image(healthyClusters, axes = FALSE, col=rainbow(k))



###############################################
# 7. Predict
###############################################

tumorMatrix = as.matrix(tumor)
tumorVector = as.vector(tumorMatrix)

# Apply clusters from before to new image, using the flexclust package
install.packages("flexclust")
library(flexclust)

KMC.kcca = as.kcca(KMC, healthyVector)
tumorClusters = predict(KMC.kcca, newdata = tumorVector)

# Visualize the clusters
dim(tumorClusters) = c(nrow(tumorMatrix), ncol(tumorMatrix))

image(tumorClusters, axes = FALSE, col=rainbow(k))

# Model Accuracy


 