import keras
import sys
import numpy as np
import json

class DoppelgangerModel(object):
    def __init__(self):
        print("\n** LOADING MODEL from pairwise_top_25.json **")
        with open('pairwise_top_25.json') as fp:
            self.model = json.load(fp) 
        print("\n** LOADED MODEL from pairwise_top_25.json **")

    def predict(self, X, feature_names, **kwargs):
        convert_image_to_width = 299
        convert_image_to_height = 299

# TODO:  Change this logic to retrieve the 25 similar images accordingly

        profile_pic = './images/%s_0.png' % str(int(X[0]))
        similar_image_arr = self.model[str(int(X[0]))]
        return similar_image_arr

if __name__== "__main__":
    model = DoppelgangerModel()
    print(model.predict([0], ['member_id']))
