import requests 
import json

def emotion_detector(text_to_analyze):
    # URL - Emotion detection service
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Headers of request to detection service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # request body/prompt to analyze
    input_json = { "raw_document": { "text": text_to_analyze } }

    try: 
        # Make a POST request to the Emotion Detection Service
        response = requests.post(URL, headers=headers, json=input_json)

        #Check if the request was succesfull OK 200
        if response.status_code == 200:
            #Parse to a better format
            response_json = response.json()
            
            #Extracting relevant info
            emotions = response_json.get('emotionPredictions', {})[0].get('emotion')
            print(emotions)
            emotion_scores = {
                'anger': emotions.get('anger'),
                'disgust': emotions.get('disgust'),
                'fear': emotions.get('fear'),
                'joy': emotions.get('joy'),
                'sadness': emotions.get('sadness'),
            }
            print(emotion_scores)

            #Output, all of the containing dic of emotion_scores plus 'dominant_emotion'
            output = {
                **emotion_scores,
                'dominant_emotion': max(emotions, key=emotions.get)
            }

            print(output) 


    except Exception as e: 
        print(f"An error occured - {e}")
        return None