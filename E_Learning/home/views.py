from django.shortcuts import render,redirect
import pyrebase
from django.contrib import auth



config = {
    "apiKey": "AIzaSyAEue4ktaLv-1wqKQgtgkfWJ1Oj6NNW-8U",
    "authDomain": "e-learning-ccbd8.firebaseapp.com",
    "databaseURL": "https://e-learning-ccbd8.firebaseio.com",
    "projectId": "e-learning-ccbd8",
    "storageBucket": "e-learning-ccbd8.appspot.com",
    "messagingSenderId": "1053587965345",
    "appId": "1:1053587965345:web:b97bb311c911183b0d77e0",
    "measurementId": "G-K1YGG2H5VQ"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def dashboard(request):
    return render(request, "accounts/dashboard.html")


def checkin(request):
    if request.method == 'GET':
        return render(request, "accounts/checkin.html")
    else:
        course = request.POST.get('course')
        question = request.POST.get('question')
        data = {
            "course": course,
            "question": question,
        }
        try:
            idtoken = request.session["uid"]
            a = authe.get_account_info(idtoken)
            a = a['users']
            a = a[0]
            a = a['localId']
            database.child('users').child(a).child('Q&A').child('question').set(data,idtoken)
            ##########
            name = database.child("users").child(a).child("details").child("branch").get(idtoken).val()

            ###########
            return render(request, "accounts/homepage.html",{'name':name})
        except:
            return render(request, "accounts/login.html", {'error': 'oops login first'})


def add_notes(request, user):
    if request.method == 'GET':
        return render(request, "home/add_notes.html",{'user':user})

    else: pass

