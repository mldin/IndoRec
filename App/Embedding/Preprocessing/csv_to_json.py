import pandas as pd
import json
import sys
import os

sys.path.append(os.path.abspath('../../../Libs'))

from Preprocessing import RemoveEmojiAndWhiteSpace

DATASET_PATH = '../../../Dataset/PergiKuliner/CSV/'
OUTPUT_FILE = '../Output/dataset.json'

def imRestaurant():
    restaurant = pd.read_csv(DATASET_PATH + 'restaurant.csv')

    return restaurant

def imFacility():
    facility = pd.read_csv(DATASET_PATH + 'facility.csv')
    
    return facility

def imPayment():
    payment = pd.read_csv(DATASET_PATH + 'payment.csv')
    # clean data
    payment = payment.loc[~payment['id'].isin([744, 1962, 1230, 2332, 662])]

    return payment

def imReview():
    review = pd.read_csv(DATASET_PATH + 'review.csv')

    return review

def forNested(dfRestaurant, dfFacility, dfPayment, dfReview):
    result = []

    for i, r in dfRestaurant.iterrows():
        facility = dfFacility[dfFacility['restaurant_id'] == r['id']]['facility'].tolist()
        payment = dfPayment[dfPayment['restaurant_id'] == r['id']]['method'].tolist()
        review = dfReview[dfReview['restaurant_id'] == r['id']]['review'].tolist()

    for i in range(len(facility)):
        facility[i] = RemoveEmojiAndWhiteSpace(facility[i])

    for i in range(len(payment)):
        payment[i] = RemoveEmojiAndWhiteSpace(payment[i])

    for i in range(len(review)):
        review[i] = RemoveEmojiAndWhiteSpace(review[i])

        tmp = {
            'id': r['id'],
            'name': RemoveEmojiAndWhiteSpace(r['name']),
            'category': RemoveEmojiAndWhiteSpace(r['category']),
            'price_min': r['price_min'],
            'price_max': r['price_max'],
            'address': RemoveEmojiAndWhiteSpace(r['address']),
            'facility': facility,
            'payment': payment,
            'review': review
        }
        result.append(tmp)
    
    return result

if __name__ == "__main__":
    nested = forNested(imRestaurant(), imFacility(), imPayment(), imReview())
    
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    with open(OUTPUT_FILE, "w") as file:
        json.dump(nested, file)

