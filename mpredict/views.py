from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.staticfiles.views import serve
from django.views.decorators.csrf import csrf_exempt

from mpredict.functions.fileHandler import handle_uploaded_file
from mpredict.functions.linearRegression import dataAnalytics, graphData
from mpredict.functions.twoDRegressionTree import TDRT
from mpredict.functions.nDRegressionTree import NDRT
from mpredict.functions.randomForestRegressor import RFR

from mpredict.form import FileUpload1

# Create your views here.

def defaultPage(request):
    return render(request, "default.html")

def linearRegression(request):
    if(request.method == 'POST'):
        file_up = FileUpload1(request.POST, request.FILES)
        if file_up.is_valid():
            handle_uploaded_file(request.FILES['file'])
            d1=dataAnalytics()
            #return HttpResponse("File uploaded successfuly")
            l1=graphData()
            return render(request, "graph.html", {'data1':l1[0], 'data2':l1[1], 'data3':d1, 'data4':l1[2]})
    else:
        file_up = FileUpload1()
        return render(request, "linearRegression.html", {'form':file_up})

def twoDRegressionTree(request):
    if(request.method == 'POST'):
        file_up = FileUpload1(request.POST, request.FILES)
        if file_up.is_valid():
            handle_uploaded_file(request.FILES['file'])
            TDRT()
            #return HttpResponse("File uploaded successfuly")
            return render(request, "downloadFile.html")
    else:
        file_up = FileUpload1()
        return render(request, "twoDRegressionTree.html", {'form':file_up})

def nDRegressionTree(request):
    if(request.method == 'POST'):
        file_up = FileUpload1(request.POST, request.FILES)
        if file_up.is_valid():
            handle_uploaded_file(request.FILES['file'])
            NDRT()
            #return HttpResponse("File uploaded successfuly")
            return render(request, "downloadFile.html")
    else:
        file_up = FileUpload1()
        return render(request, "nDRegressionTree.html", {'form':file_up})

def randomForestRegressor(request):
    if(request.method == 'POST'):
        file_up = FileUpload1(request.POST, request.FILES)
        if file_up.is_valid():
            handle_uploaded_file(request.FILES['file'])
            RFR()
            #return HttpResponse("File uploaded successfuly")
            return render(request, "downloadFile.html")
    else:
        file_up = FileUpload1()
        return render(request, "randomForestRegressor.html", {'form':file_up})

def fileDownload(request):
    filepath= 'mpredict/static/upload/output.csv'
    fsock = open(filepath, "rb")
    #return HttpResponse(fsock, content_type="application/CSV")
    return HttpResponse(fsock, headers={'Content-Type': 'application/csv','Content-Disposition': 'attachment; filename="output.csv"',})
