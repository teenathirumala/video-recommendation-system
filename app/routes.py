from flask import Blueprint, request, jsonify
from .models import fetch_data
from .preprocess import DataPreprocessor
from .recommender import Recommender

bp = Blueprint('routes', __name__)
FLIC_TOKEN = "flic_6e2d8d25dc29a4ddd382c2383a903cf4a688d1a117f6eb43b35a1e7fadbb84b8"

@bp.route('/feed', methods=['GET'])
def feed():
    username = request.args.get('username')
    category_id = request.args.get('category_id')
    mood = request.args.get('mood')

    user_data = fetch_data('https://api.socialverseapp.com/users/get_all?page=1&page_size=1000', FLIC_TOKEN)
    video_data = fetch_data('https://api.socialverseapp.com/posts/summary/get?page=1&page_size=1000', FLIC_TOKEN)

    if user_data and video_data:
        preprocessor = DataPreprocessor()
        clean_videos = preprocessor.clean_data(video_data)
        recommender = Recommender(user_data, clean_videos)
        recommendations = recommender.recommend(username, category_id, mood)
        return jsonify(recommendations)
    return jsonify({"error": "Failed to fetch data"}), 500