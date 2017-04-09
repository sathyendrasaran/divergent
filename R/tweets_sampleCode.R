#### 1. Install packages & Executing library

install.packages("bit")
install.packages("bitops")  
install.packages("twitteR")
install.packages("ROAuth")
install.packages("evaluate")
install.packages('base64enc')


library(twitteR)
library(ROAuth)
library(RCurl)

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
consumerKey="t4iKAWvOVXVebZPvP5EbgJMom"
consumerSecret="CZJZrByCSc26UHVU80ULXsYvcNUiGZJdiBTvKQWKx8Fe63baTf"
accesstoken="155263055-Aa9M93hyCIGzwSnBLPTGdpOhoTwoeAQ7Fw0NY2Qo"
accesstokensecret="yGFO0iXIYMxeuj5Gl5v5jBSgQdQHxZt4jaZOcVyoDm2XK"
setup_twitter_oauth(consumerKey, consumerSecret, accesstoken, accesstokensecret)

##Creating the authorization object by calling function OAuthFactory
twitCred <- OAuthFactory$new(consumerKey=consumerKey,
                             consumerSecret=consumerSecret,
                             requestURL=requestURL,
                             accessURL=accessURL,
                             authURL=authURL)

### Asking for access - handshake
twitCred$handshake(cainfo="cacert.pem")
  
  ### 2.2 You can get an oauth_token after doing above code
  #### 2.3 copy that token and paste it on web-browser (e.g..https://api.twitter.com/oauth/authorize?oauth_token=wWQ3zeRrSdCx3Y65m6SDyCYMPpMW68gvg9qP8jPP0)
  #### 2.4 and then Twitter answer you with No. code (e.g.. 1235467) 
  #### 2.5 Keyin that code on R.studio waiting your feedback
  #### 2.6 You finaly obtain OAuth to collect tweets
  
  #### 3. Setting repository after OAuth
  save(list="twitCred", file="twitteR_credentials")
  load("twitteR_credentials")
  #registerTwitterOAuth(twitCred)
  
  #### 4. gaining OAuth; start Function Test for Movie tweets gethering  =====
  s<-searchTwitter("#tmobiletuesdays", n=10000) 
  
  #### 5. transform from List to DataFrame =====
  s.df=twListToDF(s)
  
  #### 6. view DataFrame =====
  View(s.df)
  
  #### 7. down load as csv file  =====
  write.csv(s.df, file="C:\\Users\\sathyendrasaran\\Desktop\\Classes\\Summer sem Web and Social Analytics\\R\\Tweets\\tweetspro.df.csv", row.names=F)
  
  #### 8. save R.Data  =====
  save.image("C:\\Users\\sathyendrasaran\\Desktop\\Classes\\Summer sem Web and Social Analytics\\R\\Tweets\\windowsTweetstmob.RData") 


