from email import header
from operator import index
from flask import Flask, request, render_template, jsonify
from model import SentimentRecommenderModel


app = Flask(__name__)

sentiment_model = SentimentRecommenderModel()


@app.route('/')
def home():
    # Home page
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def prediction():
    # Recommendation for the user
    user = request.form['userName']
    user = user.lower()
    items = sentiment_model.getSentimentRecommendations(user)

    if(not(items is None)):
        print(f"retrieving items....{len(items)}")
        print(items)
        return render_template("index.html", column_names=items.columns.values, row_data=list(items.values.tolist()), zip=zip)
    else:
        return render_template("index.html", message="User doesn't exists, No product recommendations possible at this point of time!")


@app.route('/predictSentiment', methods=['POST'])
def predict_sentiment():
    # User text prediction
    review_text = request.form["reviewText"]
    print(review_text)
    pred_sentiment = sentiment_model.classify_sentiment(review_text)
    print(pred_sentiment)
    return render_template("index.html", sentiment=pred_sentiment)


if __name__ == '__main__':
    app.run()
