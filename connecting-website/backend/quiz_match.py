from flask import Flask, request, jsonify
import numpy as np
import json

from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Feature Array Encoding: General categories and subcategories
feature_encoding = {
    "general_categories": {
        "Academic & Professional": 1,
        "Creative & Arts": 2,
        "Cultural & Identity": 3,
        "Community Service & Social Impact": 4,
        "Sports & Recreation": 5,
        "Technology & Innovation": 6,
        "Social & Special Interests": 7,
        "Political & Advocacy": 8,
        "Health & Wellness": 9,
        "STEM-Specific": 10,
        "Media & Communication": 11,
        "Environmental & Sustainability": 12,
    },
    "sub_categories": {
        "Academic & Professional": ["Business", "Science", "Pre-Med", "Pre-Law", "Engineering", "Finance", 
                                     "Entrepreneurship", "Consulting", "Marketing", "Communication", 
                                     "Journalism", "Accounting", "Economics", "Human Resources", "Internal Relations"],
        "Creative & Arts": ["Performing Arts", "Fine Arts", "Digital Arts", "Writing", "Architecture", 
                            "Fashion Design", "Music Production", "Literary Arts", "Film Studies"],
        "Cultural & Identity": ["Latino", "African American", "Asian American", "Native American/Indigenous", 
                                "Christian", "Muslim", "Hindu", "Buddhist", "Interfaith/Spiritual Groups", 
                                "LGBTQ+ Advocacy", "Gender Equality", "Language Exchange", "International Student"],
        "Community Service & Social Impact": ["Volunteering", "Environmental Sustainability", "Social Justice", 
                                              "Hunger and Poverty Alleviation", "Mental Health Advocacy", 
                                              "Health", "Community Outreach", "Nonprofit Fundraising", 
                                              "Community Development"],
        "Sports & Recreation": ["Team Sports", "Individual Sports", "Adventure Sports", "Fitness", "Water Sports", 
                                 "Dance", "Cycling", "Archery"],
        "Technology & Innovation": ["Robotics", "Artificial Intelligence", "App/Web Development", "Cybersecurity", 
                                     "Data Science", "Bioinformatics", "Machine Learning", "UX/UI Design"],
        "Social & Special Interests": ["Debate", "Public Speaking", "Gaming", "Travel", "Photography", 
                                        "Culinary Arts", "DIY & Crafting", "Film & TV Club", "Astronomy"],
        "Political & Advocacy": ["Voter Registration", "Climate Change Advocacy", "LGBTQ+ Rights", "Labor Rights", 
                                  "Civil Liberties", "Human Rights", "Political Campaigning", "Youth Advocacy", 
                                  "Immigration Rights"],
        "Health & Wellness": ["Mindfulness & Meditation", "Mental Health Awareness", "Fitness & Nutrition", 
                              "Peer Counseling", "Sexual Health Advocacy", "Holistic Health", "Outdoor Recreation", 
                              "Wellness Education", "Addiction Support"],
        "STEM-Specific": ["Engineering", "Biology", "Chemistry", "Physics", "Neuroscience", "Astronomy", 
                          "Geology", "Environmental Science", "Mathematics"],
        "Media & Communication": ["Journalism", "Podcasting", "Blogging", "Video Production", "Radio", 
                                   "Photography", "Graphic Design", "Social Media Management", "Broadcasting"],
        "Environmental & Sustainability": ["Renewable Energy", "Climate Action", "Urban Planning", 
                                            "Wildlife Conservation", "Marine Biology", "Environmental Policy", 
                                            "Ecology", "Green Technology", "Waste Reduction"],
    },
}

# Map subcategories to indices for encoding
def map_subcategories_to_indices():
    subcategory_mapping = {}
    for category, subcategories in feature_encoding["sub_categories"].items():
        subcategory_mapping[category] = {sub: i + 1 for i, sub in enumerate(subcategories)}
    return subcategory_mapping

subcategory_indices = map_subcategories_to_indices()

# Club Profiles (using Feature Array Encoding)
club_profiles = [
    {"club": "Robotics Club", "features": [
        feature_encoding["general_categories"]["Technology & Innovation"],
        subcategory_indices["Technology & Innovation"]["Robotics"]
    ]},
    {"club": "Data Science Club", "features": [
        feature_encoding["general_categories"]["Technology & Innovation"],
        subcategory_indices["Technology & Innovation"]["Data Science"]
    ]},
    {"club": "Basketball Club", "features": [
        feature_encoding["general_categories"]["Sports & Recreation"],
        subcategory_indices["Sports & Recreation"]["Team Sports"]
    ]},
    {"club": "Performing Arts Club", "features": [
        feature_encoding["general_categories"]["Creative & Arts"],
        subcategory_indices["Creative & Arts"]["Performing Arts"]
    ]},
    {"club": "Climate Action Club", "features": [
        feature_encoding["general_categories"]["Environmental & Sustainability"],
        subcategory_indices["Environmental & Sustainability"]["Climate Action"]
    ]},
]

# Calculate Euclidean distance
def euclidean_distance(user_vector, club_vector):
    return np.sqrt(np.sum((np.array(user_vector) - np.array(club_vector)) ** 2))

# KNN function to find the best match
def knn_match(user_answers, k=3):
    distances = []
    for club in club_profiles:
        dist = euclidean_distance(user_answers, club["features"])
        distances.append((dist, club["club"]))
    # Sort distances and get top k
    distances.sort(key=lambda x: x[0])
    top_k = distances[:k]
    
    # Find the most common club among the top k
    clubs = [club for _, club in top_k]
    best_match = max(set(clubs), key=clubs.count)
    return best_match

@app.route('/api/match', methods=['POST'])
def match_user():
    try:
        data = request.json.get("answers")
        user_answers = []

        for item in data:
            general_category = feature_encoding["general_categories"].get(item["generalCategory"])
            if not general_category:
                return jsonify({"error": f"Unknown general category: {item['generalCategory']}"}), 400
            
            subcategories = [
                subcategory_indices[item["generalCategory"]].get(sub)
                for sub in item["subcategories"]
                if sub in subcategory_indices[item["generalCategory"]]
            ]
            if not all(subcategories):
                return jsonify({"error": f"Invalid subcategories for {item['generalCategory']}"}), 400

            user_answers.append([general_category, *subcategories])

        flattened_answers = [value for sublist in user_answers for value in sublist]
        match = knn_match(flattened_answers)
        return jsonify({"match": match})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)