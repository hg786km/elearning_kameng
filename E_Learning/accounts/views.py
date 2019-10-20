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

def signup(request):
    if request.method == 'GET':
        print(1)
        return render(request, "accounts/signup.html")

    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        year = request.POST.get('year')
        branch = request.POST.get('branch')
        try:
            user = authe.create_user_with_email_and_password(email,password)
        except:
            return render(request, "accounts/signup.html", {'error': 'try again'})
        uid = user['localId']
        idtoken = user['idToken']
        data = {"username": username,
                "year": year,
                "branch":branch,
                "detail":"1",
                }
        database.child("users").child(uid).child("details").set(data)
        return redirect('accounts:login')


def login(request):

    if request.method == 'GET':
        print(2)
        return render(request, "accounts/login.html")

    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = authe.sign_in_with_email_and_password(email, password)
        except :
            return render(request, "accounts/login.html", {'error':'invalid credentials'})


        session_id = user['idToken'] # use localId also
        # uid is name of session
        request.session['uid'] = str(session_id)

        localid = user['localId']
        print(localid)
        # print( database.child("users").get().val(),1)
        user1 = database.child("users").child(localid).get().val()
        print(user1)
        # user1 = user1.username
        # user = user['username']

        return render(request, "home/homepage.html",{"user":user1})

def logout(request):
    try:
        del request.session['uid']
    except :
        pass
    return redirect('accounts:login')

