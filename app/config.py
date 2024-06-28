import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    MONGO_URI = 'mongodb+srv://admin:admin%40mongoDB@recruitmenteteam.lt2yva1.mongodb.net/DBRecruitment'
    FACEBOOK_CLIENT_ID = '838407737791767'  # Your Facebook App ID
    FACEBOOK_CLIENT_SECRET = '2457453fbcb20061fef6412b08411f3f'  # Your Facebook App Secret
    LINKEDIN_CLIENT_ID = '77kp7jekseai2f'  # Your LinkedIn Client ID
    LINKEDIN_CLIENT_SECRET = 'iNg6AmESMeyaDpCa'  # Your LinkedIn Client Secret
