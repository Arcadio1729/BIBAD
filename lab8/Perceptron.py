#Train() - trenowanie na danych
#predict_y - przewidywanie wyniku na podstawie wag w wytrenowanym perceptronie

import numpy as np

class Perceptron:

    def __init__(self, learning_rate, X, y, weights, n_iters):  # dobrze by było dodać wartości domyślne dla wszystkiego oprócz X i y
        self.learning_rate = learning_rate
        self.activation_function = self._Heaviside_step_function
        self.X = np.matrix(X)
        self.y = np.matrix(y).transpose()
        self.weights = np.matrix(weights)
        self.n_iters = n_iters

    def _Heaviside_step_function(self, in_arg):
        if in_arg > 0:
            return 1
        else:
            return 0

    def predict_y(self, X_vector):
        return float(self.activation_function(X_vector * self.weights.transpose())) # przydałby się bias

    def _find_weights(self, X_vector, y_difference):
        return self.weights + self.learning_rate * y_difference * X_vector

    def train(self,show_error=False):
        for k in range(self.n_iters):
            for i in range(self.X.shape[0]):
                current_vector = self.X[i]
                current_result = float(self.y[i])
                current_prediction = self._predict_y(current_vector)
                current_difference = current_result - current_prediction
                self.weights = self._find_weights(current_vector, current_difference)
                if show_error:
                    print(current_difference)   # błąd się wyświetla per epoka, nie per przykład treningowy
