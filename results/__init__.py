import math
from sklearn.metrics import mean_squared_error

def predict_and_score(scaler, model, X, Y):
    '''
        Starting from a model it predicts the values and returns the score (RMSE)

        Attributes:
            - scaler: instance of the scaler, if None no de-scaling will be applied
            - model: the instance of the model
            - X: input
            - Y: output
    '''

    # Make predictions on the original scale of the data.
    if scaler is None:
        pred = model.predict(X)
        orig_data = [Y]
    else:
        pred = scaler.inverse_transform(model.predict(X))
        # Prepare Y data to also be on the original scale for interpretability.
        orig_data = scaler.inverse_transform([Y])
    
    # Calculate RMSE.
    score = math.sqrt(mean_squared_error(orig_data[0], pred[:, 0]))
    return(score, pred)