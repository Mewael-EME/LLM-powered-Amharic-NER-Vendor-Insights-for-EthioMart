import datetime
from collections import defaultdict
import statistics
import pandas as pd

def parse_post(post):
    """
    Expects a dictionary with keys: 'vendor', 'text', 'views', 'timestamp', 'entities'
    where 'entities' is a list of tuples like [("PRODUCT", "Soap"), ("PRICE", 25)]
    """
    vendor = post.get("vendor")
    views = post.get("views", 0)
    timestamp = post.get("timestamp")
    entities = post.get("entities", [])
    prices = [float(value) for label, value in entities if label == "PRICE"]
    return vendor, views, timestamp, prices, post["text"]

def calculate_vendor_metrics(posts_by_vendor):
    """
    Computes metrics per vendor
    """
    scorecard = []
    for vendor, posts in posts_by_vendor.items():
        if not posts:
            continue

        all_views = []
        all_prices = []
        all_dates = []
        top_post = {"views": 0, "text": "", "price": None}

        for post in posts:
            vendor_name, views, timestamp, prices, text = parse_post(post)
            all_views.append(views)
            all_prices.extend(prices)

            if views > top_post["views"]:
                top_post.update({"views": views, "text": text})
                if prices:
                    top_post["price"] = prices[0]

            if timestamp:
                post_date = datetime.datetime.fromisoformat(timestamp)
                all_dates.append(post_date)

        # Compute posting frequency
        if all_dates:
            date_span = (max(all_dates) - min(all_dates)).days + 1
            weeks = max(1, date_span / 7)
            posts_per_week = round(len(posts) / weeks, 2)
        else:
            posts_per_week = 0

        avg_views = round(statistics.mean(all_views), 2) if all_views else 0
        avg_price = round(statistics.mean(all_prices), 2) if all_prices else 0

        # Example lending score
        lending_score = round((avg_views * 0.5) + (posts_per_week * 10 * 0.5), 2)

        scorecard.append({
            "Vendor": vendor,
            "Avg. Views/Post": avg_views,
            "Posts/Week": posts_per_week,
            "Avg. Price (ETB)": avg_price,
            "Top Post Views": top_post["views"],
            "Top Post Price": top_post["price"],
            "Top Post Text": top_post["text"][:100],
            "Lending Score": lending_score
        })

    return pd.DataFrame(scorecard).sort_values(by="Lending Score", ascending=False)

# Example usage
if __name__ == "__main__":
    import json

    # Example data loading
    with open("data/all_vendor_posts.json", "r", encoding="utf-8") as f:
        posts = json.load(f)

    posts_by_vendor = defaultdict(list)
    for post in posts:
        posts_by_vendor[post["vendor"]].append(post)

    df_scorecard = calculate_vendor_metrics(posts_by_vendor)
    print(df_scorecard)
    df_scorecard.to_csv("outputs/vendor_scorecard.csv", index=False)
