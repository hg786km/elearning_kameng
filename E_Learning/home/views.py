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

#
# def checkin(request):
#     if request.method == 'GET':
#         return render(request, "accounts/checkin.html")
#     else:
#         course = request.POST.get('course')
#         question = request.POST.get('question')
#         data = {
#             "course": course,
#             "question": question,
#         }
#         try:
#             idtoken = request.session["uid"]
#             a = authe.get_account_info(idtoken)
#             a = a['users']
#             a = a[0]
#             a = a['localId']
#             database.child('users').child(a).child('Q&A').child('question').set(data,idtoken)
#             ##########
#             name = database.child("users").child(a).child("details").child("branch").get(idtoken).val()
#
#             ###########
#             return render(request, "accounts/homepage.html",{'name':name})
#         except:
#             return render(request, "accounts/login.html", {'error': 'oops login first'})


def add_notes(request):
    if request.method == 'GET':
        return render(request, "home/temp.html")

    else:
        notes_name = request.POST.get('notes_name')
        tags = request.POST.get('tags')
        url = request.POST.get('url')
        print(url)


        try:
            idtoken = request.session['uid']
            a = authe.get_account_info(idtoken)
            a = a['users']
            a = a[0]
            a = a['localId']
            # a contains local id
        except:
            return render(request, "accounts/login.html")

        storage = firebase.storage()
        url = str(url)
        # data1 = {
        #     "url": url,
        # }
        storage.child("images"+url).put(url)



def add_notes(request):
    if request.method == 'GET':
        return render(request, "home/add_notes.html")

    else:
        print("falak")
        notes_name = request.POST.get('notes_name')
        tags = request.POST.get('tags')
        url = request.POST.get('url')
        print(url)
        upload=request.FILES.get('url')
        print(upload)


        try:
            idtoken = request.session['uid']
            a = authe.get_account_info(idtoken)
            a = a['users']
            a = a[0]
            a = a['localId']
            # a contains local id
        except:
            return render(request, "accounts/login.html")

        storage = firebase.storage()
        
        storage_path = "images/"+notes_name
        storage.child(storage_path).put(upload,idtoken)
        url = storage.child(storage_path).get_url(idtoken)

        username = database.child("users").child(a).child("details").child("username").get(idtoken).val()
        #print(username)
        data = {
            "tags": tags,
            "url": url,
            "username": username,
        }

        database.child('Notes').child(notes_name).set(data, idtoken)
        return render(request, "home/homepage.html")


def view_notes(request):
    notes = database.child('Notes').shallow().get().val()
    print(notes)
    list_notes = [*notes]
    print(list_notes)
    tags = []
    urls = []
    usernames = []
    for i in list_notes:
        tag = database.child('Notes').child(i).child('tags').get().val()
        tags.append(tag)
        url = database.child('Notes').child(i).child('url').get().val()
        urls.append(url)
        username = database.child('Notes').child(i).child('username').get().val()
        usernames.append(username)

    print(tags)
    print(urls)
    print(usernames)
    combine_list = zip(list_notes,tags,usernames,urls)
    return render(request, "home/display_notes.html", {'combine_list':combine_list})

def addbook(request):
    if request.method =='GET':
        return render(request,"home/addbook.html")
    else:
        bookname=request.POST.get('book_name')
        tags=request.POST.get("tags")
        try:
            idtoken=request.session['uid']
            a = authe.get_account_info(idtoken)
            a = a['users']
            a=a[0]
            a=a['localId']
        except:
            return render(request,"accounts/signup.html")
        username = database.child("users").child(a).child("details").child("username").get(idtoken).val()
        data={
            "tags":tags,
            "username":username,
            "status": "1",
        }
        database.child("books").child(bookname).set(data,idtoken)
        return render(request,"home/homepage.html")






