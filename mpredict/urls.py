from django.urls import path
from .views import fileDownload, defaultPage, linearRegression, twoDRegressionTree, nDRegressionTree, randomForestRegressor

urlpatterns = [
    path("", defaultPage, name="defaultPage"),
    path("linearRegression", linearRegression, name="linearRegression"),
    path("twoDRegressionTree", twoDRegressionTree, name="twoDRegressionTree"),
    path("nDRegressionTree", nDRegressionTree, name="nDRegressionTree"),
    path("randomForestRegressor", randomForestRegressor, name="randomForestRegressor"),
    path("download", fileDownload, name="downloadFile"),
]