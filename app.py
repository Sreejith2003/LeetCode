# from flask import Flask, request, jsonify
# # import openai 
# # from openai.error import RateLimitError
# # from functools import lru_cache

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello, Flask!"


# if __name__ == "__main__":
#     app.run(debug = True)

import asyncio

async def greet():
    await asyncio.sleep(2)
    print("Hi after 2 seconds!")

asyncio.run(greet())
