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
        alikes,aretweets,rlikes,rretweets = tweepy_streamer.TweetAnalyzer.parth(user1,user2)
    return render_template('output.html', u1 = user1, u2 = user2, a=alikes, b = aretweets,c= rlikes,d= rretweets)

if __name__ == '__main__':
    app.run(debug=True)
