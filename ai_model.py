mport tensorflow as tf
import numpy as np

categories = ["Food", "Transport", "Bills", "Shopping"]

def predict_category(description):
	return np.random.choice(categories)  # Replace with an actual ML model

print(predict_category("Uber Ride"))
