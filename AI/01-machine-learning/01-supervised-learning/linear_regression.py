
class LinearRegression():
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None

    def fit(self, X, y):
        """
        Fit linear model.

        Pseudocode:
        1. Calculate the mean of X and y
        2. Calculate the coefficients using the formula:
            coef_ = (sum((xi - x_mean) * (yi - y_mean))) / (sum((xi - x_mean)^2))
        3. Calculate the intercept using the formula:
            intercept_ = y_mean - coef_ * x_mean

        Time complexity: O(n * m) # n is the number of samples, m is the number of features
        Space complexity: O(m) # m is the number of features
        Algorithm: Ordinary Least Squares (OLS) for simple linear regression

        Args:
            X : array-like of shape (n_samples, n_features)
            Training data
            y : array-like of shape (n_samples,)
            Target 

        Returns:
            LinearRegression: The fitted model instance.

        Examples:
        >>> model = LinearRegression()
        >>> model.fit(X = [[1], [2], [3], [4], [5]], y = [2, 4, 5, 4, 5])
        >>> model.coef_
        >>> model.intercept_
        >>> model.predict(X_new = [6, 7, 8, 9, 10])
        """
        n_samples, n_features = len(X), len(X[0])

        # Calculate the mean of X and y
        x_mean = [sum(X[i][j] for i in range(n_samples)) / n_samples for j in range(n_features)]
        y_mean = sum(y) / n_samples

        # Calculate the coefficients using the formula:
        # coef_ = (sum((xi - x_mean) * (yi - y_mean))) / (sum((xi - x_mean)^2))
        numerator = sum([(X[i][j] - x_mean[j]) * (y[i] - y_mean) for i in range(n_samples) for j in range(n_features)])
        denominator = sum([(X[i][j] - x_mean[j]) ** 2 for i in range(n_samples) for j in range(n_features)])
        self.coef_ = numerator / denominator

        # Calculate the intercept using the formula:
        # intercept_ = y_mean - coef_ * x_mean
        self.intercept_ = y_mean - self.coef_ * sum(x_mean) / len(x_mean)

        return self
    
    def predict(self, X_new):
        # Ensure X is an array
        return [self.intercept_ + self.coef_ * x for x in X_new]
        # return [self.intercept_ + self.coef_ * x[0] for x in X_new]
        # X_new = [[6], [7], [8], [9], [10]]
