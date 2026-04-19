from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from .forms import (UserLoginForm, UserRegistrationForm)
from .models import UserRegistrationModel
import pandas as pd


# Create your views here.
def user_login(request):
    context = {'form': UserLoginForm()}
    if request.method == 'POST':
        print('=000=' * 40, request.POST)
        form = UserLoginForm(request.POST)
        print('VALID:', form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print('UserName:', username)
            print('Password:', password)
            try:
                user = UserRegistrationModel.objects.get(username=username, password=password)
                status = user.status
                if status == 'activated':
                    request.session['username'] = user.username
                    request.session['password'] = user.password
                    return render(request, 'users/user_home.html')
                else:
                    messages.success(request, 'Your A/C is not activated yet.')
                    return render(request, 'user_login.html', context)
            except Exception as e:
                pass
            messages.error(request, 'Invalid username or password.')
    context = {'form': UserLoginForm()}
    return render(request, 'user_login.html', context)


def user_register_action(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been submitted, Admin will get back to you soon.')

    context = {
        'form': UserRegistrationForm()
    }
    return render(request, 'register.html', context)


def user_data_view(request):
    import pandas as pd
    from django.conf import settings
    import os
    path = os.path.join(settings.MEDIA_ROOT, 'cars.csv')
    df = pd.read_csv(path)
    df = df.to_html
    path = os.path.join(settings.MEDIA_ROOT, 'Automobile_data.csv')
    auto_df = pd.read_csv(path)
    auto_df = auto_df.to_html
    return render(request, 'users/data.html', {'data': df, "auto": auto_df})


def linear_regression(request):
    from .algorithms import AlgorithmUtility
    accuracy, precision, recall, f1score = AlgorithmUtility.calc_logistic_regression()
    return render(request, 'users/lg.html',
                  {'accuracy': accuracy, "precision": precision, "recall": recall, "f1score": f1score})


def decision_tree(request):
    from .algorithms import AlgorithmUtility
    accuracy, precision, recall, f1score = AlgorithmUtility.calc_decision_tree()
    return render(request, 'users/dt.html',
                  {'accuracy': accuracy, "precision": precision, "recall": recall, "f1score": f1score})


def random_forest(request):
    from .algorithms import AlgorithmUtility
    accuracy, precision, recall, f1score = AlgorithmUtility.calc_random_forest()
    return render(request, 'users/rf.html',
                  {'accuracy': accuracy, "precision": precision, "recall": recall, "f1score": f1score})


def support_vector_classifier(request):
    from .algorithms import AlgorithmUtility
    accuracy, precision, recall, f1score = AlgorithmUtility.calc_support_vector_classifier()
    return render(request, 'users/svm.html',
                  {'accuracy': accuracy, "precision": precision, "recall": recall, "f1score": f1score})


def naive_bayes(request):
    from .algorithms import AlgorithmUtility
    accuracy, precision, recall, f1score = AlgorithmUtility.calc_naive_bayes_classifier()
    return render(request, 'users/nv.html',
                  {'accuracy': accuracy, "precision": precision, "recall": recall, "f1score": f1score})


def k_nearest_neighbour(request):
    from .algorithms import AlgorithmUtility
    accuracy, precision, recall, f1score = AlgorithmUtility.calc_k_nearest_neighbour_classifier()
    return render(request, 'users/knn.html',
                  {'accuracy': accuracy, "precision": precision, "recall": recall, "f1score": f1score})


def ann_results(request):
    from .algorithms import AlgorithmUtility
    accuracy, precision, recall, f1score = AlgorithmUtility.calculate_ann_results()
    return render(request, 'users/ann.html',
                  {'accuracy': accuracy, "precision": precision, "recall": recall, "f1score": f1score})


def user_prediction(request):
    if request.method == "POST":
        price = int(request.POST.get("price"))
        SpareParts = int(request.POST.get("SpareParts"))
        CylinderVolume = int(request.POST.get("CylinderVolume"))
        ResalePrice = int(request.POST.get("ResalePrice"))
        CarssReview = int(request.POST.get("CarssReview"))
        test = [price, SpareParts, CylinderVolume, ResalePrice, CarssReview]
        from .algorithms import AlgorithmUtility
        rslt = AlgorithmUtility.test_user_date(test)
        if rslt[0] == 1:
            msg = "you Can Buy"
        else:
            msg = "Dont buy"
        return render(request, "users/Prediction_form.html", {"msg": msg, "features": test})
    else:
        return render(request, "users/Prediction_form.html", {})
