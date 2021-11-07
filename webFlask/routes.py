from webFlask import app, forms, api_methods
from flask import render_template, request


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/bestsellers', methods=["GET", "POST"])
def bestSellers():
    form = forms.BestSellersForm(request.form)
    if request.method == "POST":
        category = request.form["category"]
        timeFrame = request.form["timeFrame"]
        submission = api_methods.request_best_sellers(category, timeFrame)
        if submission["status"] == "ERROR":
            return render_template('error.html')
        else:
            best_list = []
            index = 0
            for i in submission["results"]["books"]:
                best_results = (i["title"], i["author"], i["book_image"])
                best_list.append(best_results)
                index += 1
                if index == 10:
                    break
            return render_template("best_post.html", response=best_list)
    return render_template("bestSellers.html", form=form)


@app.route('/bookreviews', methods=["GET", "POST"])
def bookReviews():
    form = forms.BookReviewsForm(request.form)
    if request.method == "POST":
        bookTitle = request.form["bookTitle"]
        submission = api_methods.request_book_reviews(bookTitle)
        summaries = []
        for i in submission["results"]:
            title_summary = (i["book_title"], i["summary"])
            summaries.append(title_summary)
        return render_template("reviews_post.html", response=summaries)
    return render_template("bookReviews.html", form=form)
