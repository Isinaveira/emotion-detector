"""
Server module for Emotion Detector web application.

This module uses Flask to create a web server that can analyze the emotions
in a given text and return the results to the user.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Route to handle emotion detection requests.

    Retrieves the text to analyze from the request arguments, uses the
    emotion_detector function to analyze the text, and returns the results.

    Returns:
        str: A formatted string with the emotion analysis results.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    return (f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, "
            f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Route to render the index page.

    This function initiates the rendering of the main app page over the Flask channel.

    Returns:
        str: Rendered HTML of the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
