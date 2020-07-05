import numpy as np
from math import sqrt
from sklearn.metrics import mean_squared_error
from tqdm import tqdm


MIN_USER_RATINGS = 35
DELETE_RATING_COUNT = 15

def train_test_split(ratings):

    validation = np.zeros(ratings.shape)
    train = ratings.copy()

    for user in np.arange(ratings.shape[0]):
        if len(ratings[user,:].nonzero()[0]) >= MIN_USER_RATINGS:
            val_ratings = np.random.choice(
                ratings[user, :].nonzero()[0],
                size=DELETE_RATING_COUNT,
                replace=False
            )
            train[user, val_ratings] = 0
            validation[user, val_ratings] = ratings[user, val_ratings]
    return train, validation


class Recommender:

  def __init__(self, n_epochs=200, n_latent_features=20, lmbda=0.1, learning_rate=0.001):
    self.n_epochs = n_epochs
    self.n_latent_features = n_latent_features
    self.lmbda = lmbda
    self.learning_rate = learning_rate
  def predictions(self, P, Q):
    return np.dot(P.T, Q)

  def fit(self, X_train, X_val):
    self.X_train = X_train
    m, n = X_train.shape

    self.P = 3 * np.random.rand(self.n_latent_features, m)
    self.Q = 3 * np.random.rand(self.n_latent_features, n)

    self.val_error = []

    users, items = X_train.nonzero()
    print('Starting training....')
    for epoch in tqdm(range(self.n_epochs)):
        for u, i in zip(users, items):
            error = X_train[u, i] - self.predictions(self.P[:,u], self.Q[:,i])
            self.P[:, u] += self.learning_rate * (error * self.Q[:, i] - self.lmbda * self.P[:, u])
            self.Q[:, i] += self.learning_rate * (error * self.P[:, u] - self.lmbda * self.Q[:, i])

    return self

  def predict(self, user_index):
    y_hat = self.predictions(self.P, self.Q)
    predictions_index = np.where(self.X_train[user_index, :] == 0)[0]
    return y_hat[user_index, predictions_index].flatten()
