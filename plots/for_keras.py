import matplotlib.pyplot as plt

def plot_loss_history(history):
    '''
        This functions plots the training vs test loss of a Keras model 

        Attributes:
            - history (keras.callbacks.History): the history of a trained Keras model
    '''

    # Get training and test loss histories
    training_loss = history.history['loss']
    test_loss = history.history['val_loss']

    # Create count of the number of epochs
    epoch_count = range(1, len(training_loss) + 1)

    # Visualize loss history
    plt.plot(epoch_count, training_loss, 'r--')
    plt.plot(epoch_count, test_loss, 'b-')
    plt.legend(['Training Loss', 'Test Loss'])
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.show()