from django.shortcuts import render, redirect
from .forms import AdminLoginForm
from users.models import UserRegistrationModel
from django.core.paginator import Paginator
from django.contrib import messages


# Create your views here.
def admin_login(request):
    print('REQ', request)
    context = {
        'form': AdminLoginForm()
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == 'admin' and password == 'admin':
            return render(request, 'admins/admin_home.html')
        else:
            messages.error(request, 'Incorrect username or password')
            return render(request, 'admin_login.html', context)

    return render(request, 'admin_login.html', context)


def admin_home(request):
    return render(request, 'admins/admin_home.html')


def users_list(request):
    users_list = UserRegistrationModel.objects.all()

    paginator = Paginator(users_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        # 'users': UserRegistrationModel.objects.all(),
        'users_list': page_obj,
    }
    return render(request, 'admins/users_list.html', context)


def activate_user(request, id):
    user = UserRegistrationModel.objects.get(id=id)
    # print("STATUS:", user.status)

    if user.status == 'waiting':
        user.status = 'activated'
        user.save()
    else:
        user.status = 'waiting'
        user.save()
    return redirect('admins_:admin_home')


def admin_results(request):
    from users.algorithms import AlgorithmUtility
    lg_accuracy, lg_precision, lg_recall, lg_f1score = AlgorithmUtility.calc_logistic_regression()
    dt_accuracy, dt_precision, dt_recall, dt_f1score = AlgorithmUtility.calc_decision_tree()
    rf_accuracy, rf_precision, rf_recall, rf_f1score = AlgorithmUtility.calc_random_forest()
    svm_accuracy, svm_precision, svm_recall, svm_f1score = AlgorithmUtility.calc_support_vector_classifier()
    nb_accuracy, nb_precision, nb_recall, nb_f1score = AlgorithmUtility.calc_naive_bayes_classifier()
    knn_accuracy, knn_precision, knn_recall, knn_f1score = AlgorithmUtility.calc_k_nearest_neighbour_classifier()
    # ann_accuracy, ann_precision, ann_recall, ann_f1score = AlgorithmUtility.calculate_ann_results()

    lg = {"lg_accuracy": lg_accuracy, "lg_precision": lg_precision, "lg_recall": lg_recall, "lg_f1score": lg_f1score}
    dt = {"dt_accuracy": dt_accuracy,"dt_precision": dt_precision,"dt_recall":dt_recall,"dt_f1score": dt_f1score}
    rf = {"rf_accuracy": rf_accuracy, "rf_precision": rf_precision, "rf_recall": rf_recall, "rf_f1score": rf_f1score}
    svm = {"svm_accuracy": svm_accuracy, "svm_precision": svm_precision, "svm_recall": svm_recall, "svm_f1score": svm_f1score}
    nb = {"nb_accuracy": nb_accuracy, "nb_precision": nb_precision, "nb_recall": nb_recall, "nb_f1score": nb_f1score}
    knn = {"knn_accuracy": knn_accuracy, "knn_precision": knn_precision, "knn_recall": knn_recall, "knn_f1score": knn_f1score}
    # ann = {"ann_accuracy": ann_accuracy, "ann_precision": ann_precision, "ann_recall": ann_recall,
    #        "ann_f1score": ann_f1score}
    return render(request, "admins/admin_results.html", {"lg": lg, "dt": dt, "rf": rf, "svm": svm, "nb": nb, "knn": knn})
