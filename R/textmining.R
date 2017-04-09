#####   install textmining package
install.packages("tm")
install.packages("SnowballC")
#####    install wordcloud package
install.packages("wordcloud")

library(tm)
library(SnowballC)
library(wordcloud)

mydata = read.csv("C:\\Users\\sathyendrasaran\\Desktop\\Classes\\Summer sem Web and Social Analytics\\R\\Tweets\\fbextractcommentmsg.csv")

mydata<- as.data.frame(mydata)
# build a corpus, the source is character vectors
myCorpus <- Corpus(VectorSource(mydata$x))

# remove punctuation
myCorpus <- tm_map(myCorpus, removePunctuation)
# remove numbers
myCorpus <- tm_map(myCorpus, removeNumbers)
# remove whitespace
myCorpus <- tm_map(myCorpus, stripWhitespace, lazy=TRUE)
#convert to lower case
myCorpus <-tm_map(myCorpus, content_transformer(tolower))

# remove URLs
removeURL <- function(x) gsub("http[[:alnum:]]*", "", x)
myCorpus <- tm_map(myCorpus, removeURL)

# add two extra stop words: available and via
myStopwords <- c(stopwords("english"), "available", "via")
# remove r and big from stopwords
myStopwords <- setdiff(myStopwords, c("r", "big"))
# remove stopwords from corpus
myCorpus <- tm_map(myCorpus, removeWords, myStopwords)

# keep a copy of corpus to use later as a dictionary for stem completion
myCorpusCopy <- myCorpus


# stem words
myCorpus <- tm_map(myCorpus, stemDocument)
myCorpus<-tm_map(myCorpus, PlainTextDocument)

# generate a word cloud
wordcloud(myCorpus, scale=c(5,0.5), max.words=100, random.order=FALSE, rot.per=0.35, use.r.layout=FALSE, colors=brewer.pal(8, "Dark2"))

#####   note: if you use tm v0.6, it may give the error message 
##### Error: inherits(doc, "TextDocument") is not TRUE
#####   use the following code to solve the problem
#####   myCorpus<-tm_map(myCorpus, PlainTextDocument)

####Note: read a cvs file into R
####a <- read.cvs(“path of the csv file”, header=true/false, sep=”,”)
####b <- data.frame(a)
