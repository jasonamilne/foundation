from linear_regression import LinearRegression
import pytest

@pytest.fixture
def model():
    return LinearRegression()

def test_normal_case(model):
    model.fit(X = [[1], [2], [3], [4], [5]], y = [1, 2, 3, 4, 5])
    assert model.coef_ == 1.0
    assert model.intercept_ == 0.0
    assert model.predict(X_new = [6, 7, 8, 9, 10]) == [6.0, 7.0, 8.0, 9.0, 10.0]    
