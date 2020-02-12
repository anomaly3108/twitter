from flask import Flask, render_template, request
import tweepy_streamer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    return render_template('output.html')

@app.route('/output', methods=['GET','POST'])
def getvalue():
    if request.method =='POST':
        user1,user2 = request.form['yo'].split(",")
        user1 = '@'+user1
        user2 = '@'+user2
        alikes,aretweets,rlikes,rretweets,adrf3 = tweepy_streamer.TweetAnalyzer.parth(user1,user2)

        # alikes,aretweets,rlikes,rretweets,adrf3 = 1,2,3,4,'Source Sentiment_Reliance Sentiment_Airtel 0 Mobile Web (M2) 1 1 1 TweetDeck 3 -1 2 Twidere for Android #8 1 1 3 Twitter Web App -7 2 4 Twitter Web Client -3 2 5 Twitter for Android -124 -84 6 Twitter for iPad 1 -1 7 Twitter for iPhone -8 -13'
    return render_template('output.html', u1 = user1, u2 = user2, a=alikes, b = aretweets,c= rlikes,d= rretweets, e = adrf3)

if __name__ == '__main__':
    app.run(debug=True)
