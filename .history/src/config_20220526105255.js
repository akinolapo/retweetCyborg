//config.js
/** TWITTER APP CONFIGURATION
 * consumer_key
 * consumer_secret
 * access_token
 * access_token_secret
 */
module.exports = {
    consumer_key: '5UuPH4liyQ9OZAxiRa6a7h1nv',  
    consumer_secret: 'q69tLFX6QY6IqD073EXCnxu1ett28BjcHQrDnQP5bw8qZzfNNW',
    access_token: '1287921782545092610-1osstYxj6aRWH1zV8yoY7SKjDIkoF4',  
    access_token_secret: '9Tw1otrr4TgQaJGqHscJtAsN7mFfzFn0CbEpf3PteZYXT'
  }


  module.exports = {
    consumer_key: process.env.TWITTER_CONSUMER_KEY,  
    consumer_secret: process.env.TWITTER_CONSUMER_SECRET,
    access_token: process.env.TWITTER_ACCESS_TOKEN,  
    access_token_secret: process.env.TWITTER_ACCESS_TOKEN_SECRET
  }
