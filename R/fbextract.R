
# Packages to extract data from fb 
# I dont think all packages are required - need to check for necesary packages

install.packages("devtools")
install_version("httr", version = "1.1.0", repos = "http://cran.us.r-project.org")
install.packages("httr")
install.packages("withr")
install.packages('RCurl')
install.packages('Rcpp')
install.packages('iterators')
install.packages("tm")

library(iterators)
library(devtools)

install_github("Rfacebook", "pablobarbera", subdir="Rfacebook")
require("Rfacebook")
##############################################################################


# acces token to access fb data from your account
getusertoken="EAACEdEose0cBAKUidw04VhlNXvsvCBZCYX3MbcPicUvemuZCBw3Lpp6gwZABK4KntSPynKqiR322vPXH7Yx3XVoNHYmoiLuW37Lv8XsA1LIKJZAPV4RSR47kdgpGufhbZCcRHGdrXKZBZBuaCPW16TKcrouAeJEiQQZAUj4hjZCr2IecsfZB9OWOtbWtT1jssQ85QZD"

############# Oldd code to get access token not working ###############
fb_oauth <- fbOAuth(app_id="484800651644491", app_secret="899db2e31f5d9b120e07ac00601e9727",extended_permissions = TRUE)
save(fb_oauth, file="fb_oauth")
load("fb_oauth")
##########################################3


# Extracts Posts from particular page with page name
pageName<-"T-Mobile"
today<-Sys.Date();
startdate<-as.Date(c("2016-01-01"))
pagepost<-getPage(pageName, getusertoken, n = 100000, since = startdate, until = today, feed = FALSE)
write.table(pagepost, "C:\\Users\\sathyendrasaran\\Desktop\\Classes\\Summer sem Web and Social Analytics\\R\\Tweets\\fbextractcsv.txt", sep=";")


# importing data from csv
mydata = read.csv("C:\\Users\\sathyendrasaran\\Desktop\\Classes\\Summer sem Web and Social Analytics\\R\\Tweets\\Tmobilejan1toJul2.csv")

mydata<- as.data.frame(mydata)


postId<-""
commentMessage<-""
endTag<-"!@!"
postComments<-""
postComments<-data.frame(postId,commentMessage,endTag);
i<-1

for (postId in mydata$id){
  #while(i<4){  
  print(postId)
   # print(i)
    
    tryCatch({
    com<-getPost(postId, getusertoken, n = 50000, comments = TRUE, likes = FALSE)
    print("after post")
    comDataFrame<-as.data.frame(com)
    
    commentMessage<-""
    
    for(message in comDataFrame$comments.message){
    #print(message)
      
      
      # remove punctuation
     # message <- tm_map(message, removePunctuation)
      # remove numbers
      #message <- tm_map(message, removeNumbers)
      # remove whitespace
      #message <- tm_map(message, stripWhitespace, lazy=TRUE)
      #convert to lower case
      #message <-tm_map(message, content_transformer(tolower))
      
      # remove URLs
    #  removeURL <- function(x) gsub("http[[:alnum:]]*", "", x)
    #  message <- tm_map(message, removeURL)
      
    
      
      commentMessage<-paste(commentMessage,message)
    }
    
    postComments<-rbind(postComments,data.frame(postId,commentMessage,endTag))
    i<-i+1    
    }, error=function(e){})
    }
write.table(postComments,sep = "#@#", file="C:\\Users\\sathyendrasaran\\Desktop\\xyz.txt", row.names=FALSE)
write.table(postComments,sep = "#@#", file="C:\\Users\\sathyendrasaran\\Desktop\\Classes\\Summer sem Web and Social Analytics\\R\\Tweets\\Postandcommentscopy.txt", row.names=FALSE)
write.table(postComments,sep = "#@#", file="C:\\Users\\sathyendrasaran\\Desktop\\Classes\\Summer sem Web and Social Analytics\\R\\Tweets\\Postandcomments.txt", row.names=FALSE)
write.table(postComments$commentMessage,sep = ";", file="C:\\Users\\sathyendrasaran\\Desktop\\Classes\\Summer sem Web and Social Analytics\\R\\Tweets\\comments.txt", row.names=FALSE)
write.table(postComments$postId,sep = ";", file="C:\\Users\\sathyendrasaran\\Desktop\\Classes\\Summer sem Web and Social Analytics\\R\\Tweets\\postid.txt", row.names=FALSE)






myCorpus <- tm_map(myCorpus, remove)








#### 7. down load as csv file  =====
write.csv(pagepost.df, file="C:\\Users\\sathyendrasaran\\Desktop\\Classes\\Summer sem Web and Social Analytics\\R\\Tweets\\fbextract.df.csv", row.names=F)

me <- getUsers("me",token=getusertoken)



my_likes <- getLikes(user="me", token=getusertoken)

