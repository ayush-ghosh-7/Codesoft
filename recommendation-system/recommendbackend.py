from flask import Flask, render_template, request, jsonify
import numpy as np
from collections import defaultdict
import random

app = Flask(__name__, template_folder='templates')

# Enhanced movie database with weighted genres (1-5)
movies_db = {
    # Action
    "The Dark Knight": {
        "genres": {"Action": 5, "Drama": 4, "Crime": 5},
        "poster": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg",
        "year": 2008,
        "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham..."
    },
    "Mad Max: Fury Road": {
        "genres": {"Action": 5, "Adventure": 5, "Sci-Fi": 4},
        "poster": "https://m.media-amazon.com/images/M/MV5BN2EwM2I5OWMtMGQyMi00Zjg1LWJkNTctZTdjYTA4OGUwZjMyXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
        "year": 2015,
        "description": "In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler..."
    },
    "John Wick": {
        "genres": {"Action": 5, "Thriller": 4},
        "poster": "https://m.media-amazon.com/images/M/MV5BMTU2NjA1ODgzMF5BMl5BanBnXkFtZTgwMTM2MTI4MjE@._V1_.jpg",
        "year": 2014,
        "description": "An ex-hitman comes out of retirement to track down the gangsters who killed his dog..."
    },
    
    # Comedy
    "Superbad": {
        "genres": {"Comedy": 5, "Drama": 3},
        "poster": "https://m.media-amazon.com/images/M/MV5BMTc0NjIyMjA2OF5BMl5BanBnXkFtZTcwMzIxNDE1MQ@@._V1_.jpg",
        "year": 2007,
        "description": "Two co-dependent high school seniors are forced to deal with separation anxiety..."
    },
    "Bridesmaids": {
        "genres": {"Comedy": 5, "Romance": 3},
        "poster": "https://m.media-amazon.com/images/M/MV5BMjAyOTMyMzUxNl5BMl5BanBnXkFtZTcwODI4MzE0NA@@._V1_.jpg",
        "year": 2011,
        "description": "Competition between the maid of honor and a bridesmaid threatens to upend the life of an out-of-work pastry chef..."
    },
    "The Hangover": {
        "genres": {"Comedy": 5},
        "poster": "https://m.media-amazon.com/images/M/MV5BNGQwZjg5YmYtY2VkNC00NzliLTljYTctNzI5ZDhlY2E2NzE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
        "year": 2009,
        "description": "Three buddies wake up from a bachelor party in Las Vegas with no memory of the night before and the bachelor missing..."
    },
    
    # Drama
    "The Shawshank Redemption": {
        "genres": {"Drama": 5},
        "poster": "https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_.jpg",
        "year": 1994,
        "description": "Two imprisoned men bond over a number of years..."
    },
    "Forrest Gump": {
        "genres": {"Drama": 5, "Romance": 4},
        "poster": "https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
        "year": 1994,
        "description": "The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate, and other history unfold through the perspective of an Alabama man with an IQ of 75..."
    },
    
    # Sci-Fi
    "Inception": {
        "genres": {"Sci-Fi": 5, "Action": 5, "Thriller": 4},
        "poster": "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_.jpg",
        "year": 2010,
        "description": "A thief who steals corporate secrets through dream-sharing technology..."
    },
    "The Matrix": {
        "genres": {"Sci-Fi": 5, "Action": 5},
        "poster": "https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",
        "year": 1999,
        "description": "A computer hacker learns about the true nature of reality..."
    },
    "Interstellar": {
        "genres": {"Sci-Fi": 5, "Adventure": 4, "Drama": 4},
        "poster": "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
        "year": 2014,
        "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival..."
    },
    
    # Horror
    "Get Out": {
        "genres": {"Horror": 5, "Mystery": 4, "Thriller": 5},
        "poster": "https://m.media-amazon.com/images/M/MV5BMjUxMDQwNjcyNl5BMl5BanBnXkFtZTgwNzcwMzc0MTI@._V1_.jpg",
        "year": 2017,
        "description": "A young African-American visits his white girlfriend's parents..."
    },
    "The Conjuring": {
        "genres": {"Horror": 5, "Mystery": 4, "Thriller": 4},
        "poster": "https://m.media-amazon.com/images/M/MV5BMTM3NjA1NDMxMV5BMl5BanBnXkFtZTcwMDQzNDMzOQ@@._V1_.jpg",
        "year": 2013,
        "description": "Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse..."
    },
    
    # Romance
    "The Notebook": {
        "genres": {"Romance": 5, "Drama": 4},
        "poster": "https://m.media-amazon.com/images/M/MV5BMTk3OTM5Njg5M15BMl5BanBnXkFtZTYwMzA0ODI3._V1_.jpg",
        "year": 2004,
        "description": "A poor yet passionate young man falls in love with a rich young woman..."
    },
    "La La Land": {
        "genres": {"Romance": 5, "Drama": 4, "Musical": 5},
        "poster": "https://m.media-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_.jpg",
        "year": 2016,
        "description": "While navigating their careers in Los Angeles, a pianist and an actress fall in love while attempting to reconcile their aspirations for the future..."
    }
}

# Update genres list if you added new genres
genres = ["Action", "Comedy", "Drama", "Sci-Fi", "Horror", "Romance", "Animation", "Thriller"]

def get_recommendations(user_ratings):
    """Improved recommendation algorithm with proper weighting"""
    scores = []
    
    # Normalize user ratings to 0-1 scale
    max_user_rating = max(user_ratings.values()) if user_ratings else 1
    user_normalized = {k: v/max_user_rating for k, v in user_ratings.items()}
    
    for title, movie in movies_db.items():
        score = 0
        # Calculate weighted score
        for genre, user_score in user_normalized.items():
            if genre in movie["genres"]:
                # Multiply user preference by movie's genre strength
                score += user_score * (movie["genres"][genre]/5)
        
        if score > 0:
            scores.append({
                "title": title,
                "score": score,
                "poster": movie["poster"],
                "year": movie["year"],
                "description": movie["description"],
                "genres": list(movie["genres"].keys())
            })
    
    # Sort by score and return top 5
    return sorted(scores, key=lambda x: x["score"], reverse=True)[:5]

@app.route('/')
def home():
    return render_template('index.html', genres=genres)

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json()
        user_ratings = {k: int(v) for k, v in data['ratings'].items()}
        
        print("Received ratings:", user_ratings)  # Debug log
        
        recommendations = get_recommendations(user_ratings)
        
        print("Generated recommendations:", recommendations)  # Debug log
        
        return jsonify({
            'status': 'success',
            'recommendations': recommendations
        })
        
    except Exception as e:
        print("Error:", str(e))  # Debug log
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)