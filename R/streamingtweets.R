##########################streaming tweets#################################################################
#### 1. Install packages & Executing library

install.packages("bit")
install.packages("bitops")  
install.packages("twitteR")
install.packages("ROAuth")
install.packages("evaluate")
install.packages("streamR")   

library(twitteR)
library(ROAuth)
library(RCurl)
library(streamR)  
#### 2. gaining OAuth; for this step, you need to obtain Twitter Account and Auth,  ##

## Download the curl Cert and save it at your default R folder
download.file(url="http://curl.haxx.se/ca/cacert.pem", destfile="cacert.pem")

##Set constant requestURL
requestURL <- "https://api.twitter.com/oauth/request_token"
## Set constant accessURL
accessURL <- "https://api.twitter.com/oauth/access_token"
##Set constant authURL
authURL <- "https://api.twitter.com/oauth/authorize"

###Replace with your own keys from twitter developer account
consumerKey="uaznukMbZ0Y5EWcidxQw5Ma0e"
consumerSecret="lNy21Hx3ZlRfZHQdTSFu7RmFI4ujjlyE9YqPuCa4on6c6Hvl6E"
accesstoken="155263055-SWSxRXvfdOjVugMuis0Hk9QsliG7qnfKqlsJtoF0"
accesstokensecret="	9B0Op4wx0pZ7zI3E4CrmOC7vU1pqwqANz3h93its1Q6et"
setup_twitter_oauth(consumerKey, consumerSecret, accesstoken, accesstokensecret)

##Creating the authorization object by calling function OAuthFactory
twitCred <- OAuthFactory$new(consumerKey=consumerKey,
                             consumerSecret=consumerSecret,
                             requestURL=requestURL,
                             accessURL=accessURL,
                             authURL=authURL)

### Asking for access - handshake
twitCred$handshake(cainfo="cacert.pem")

#streaming election tweets
filterStream(file="tweets_election.json",
             track="#orlando", timeout=100, oauth=twitCred )
electionTweets.df <- parseTweets("tweets_election.json", simplify = TRUE)
View(electionTweets.df)

#dim(electionTweets.df)
write.csv(electionTweets.df, file="C:\\Users\\sathyendrasaran\\Desktop\\Classes\\Summer sem Web and Social Analytics\\R\\Tweets\\streamtweets.df.csv", row.names=F)



filterStream(file="tweets_rstats.json",
             track="rstats", timeout=10, oauth=twitCred )
rstatsTweets.df <- parseTweets("tweets_rstats.json", simplify = TRUE)