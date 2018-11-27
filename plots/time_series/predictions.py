import matplotlib.pyplot as plt
import numpy as np

def plot_prediction_train_vs_test(window_size, df, feature, train_predict, test_predict):  
    '''
        Plots the results of the predictions (on train and on test) of a model (UNIVARIATE) for time series.
        Assuming that the source data comes from a Pandas dataframe.

        Attributes:
            - window_size: (int) dimension of the window used for prediction
            - df: (Pandas.DataFrame) original dataframe
            - feature: (string) column of the dataframe on which the model has been trained
            - train_predict: (array[float]) predictions on train set
            - test_predict: (array[float]) predictions on test set
    '''

    # Start with training predictions.
    train_predict_plot = np.empty_like(df.filter([feature]))
    train_predict_plot[:, :] = np.nan
    train_predict_plot[window_size:window_size + len(train_predict), :] = train_predict

    # Add test predictions.
    test_predict_plot = np.empty_like(df.filter([feature]))
    test_predict_plot[:, :] = np.nan
    test_predict_plot[window_size + len(train_predict):df.shape[0], :] = test_predict

    # Create the plot.
    plt.plot(df[feature].values, label = 'True value', alpha=0.4)
    plt.plot(train_predict_plot, label = 'Training set prediction')
    plt.plot(test_predict_plot, label = 'Test set prediction')
    plt.xlabel('')
    plt.ylabel('Values')
    plt.title('Comparison true vs. predicted training / test')
    plt.legend()
    plt.show()