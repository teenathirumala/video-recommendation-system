import pandas as pd

class Recommender:
    def __init__(self, user_data, video_data):
        self.user_data = pd.DataFrame(user_data)
        self.video_data = pd.DataFrame(video_data)

    def recommend(self, username, category_id=None, mood=None):
        recommendations = self.video_data
        if category_id:
            recommendations = recommendations[recommendations['category_id'] == category_id]
        if mood:
            recommendations = recommendations[recommendations['mood'] == mood]
        return recommendations.head(10).to_dict(orient='records')
