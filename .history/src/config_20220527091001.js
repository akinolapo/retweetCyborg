//config.js
/** TWITTER APP CONFIGURATION
 * consumer_key
 * consumer_secret
 * access_token
 * access_token_secret
 */


module.exports = {
    consumer_key: process.env.TWITTER_CONSUMER_KEY.toString(),  
    consumer_secret: process.env.TWITTER_CONSUMER_SECRET.toString(),
    access_token: process.env.TWITTER_ACCESS_TOKEN.toString(),  
    access_token_secret: process.env.TWITTER_ACCESS_TOKEN_SECRET
  }
