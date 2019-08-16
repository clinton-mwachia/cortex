import numpy as np

labels = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]


def pre_inference(sample, metadata):
    return [
        sample["sepal_length"],
        sample["sepal_width"],
        sample["petal_length"],
        sample["petal_width"],
    ]


def post_inference(prediction, metadata):
    predicted_class_id = prediction[0][0]
    return {"class_label": labels[predicted_class_id], "class_index": predicted_class_id}
