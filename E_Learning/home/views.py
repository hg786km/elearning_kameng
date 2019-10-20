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

def addcourse(request):
    if request.method == 'GET':
        return render(request, "home/addcourse.html")

    else:
        print("falak")
        course_name = request.POST.get('course_name')
        video_name = request.POST.get('video_name')
        tags = request.POST.get('tags')
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
        
        storage_path = "videos/"+course_name+"/"+video_name+".mp4"
        storage.child(storage_path).put(upload,idtoken)
        url = storage.child(storage_path).get_url(idtoken)

        username = database.child("users").child(a).child("details").child("username").get(idtoken).val()
        #print(username)
        data = {
            "tags": tags,
            "url": url,
            "username": username,
        }

        database.child('course').child(course_name).child(video_name).set(data, idtoken)
        return render(request, "home/addcourse.html")

def course_list(request):
    courses = database.child('course').shallow().get().val()
    print(courses)
    list_courses = [*courses]
    print(list_courses)
    link_lists = []
    for i in list_courses:
        videos = database.child('course').child(i).shallow().get().val()
        videos1=[*videos]
        link = "/stuff/"+i+"/"+videos1[0]
        link_lists.append(link)
    print(link_lists)
    combine_list = zip(list_courses,link_lists)
    return render(request, "home/display_courses.html", {'combine_list':combine_list})

def viewcourse(request,coursename,videoname):
    try:
        idtoken = request.session['uid']
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        # a contains local id
    except:
        return render(request, "accounts/login.html")
    videos = database.child('course').child(coursename).shallow().get(idtoken).val()
    videos1=[*videos]
    link_list=[]
    for i in videos1:
        link = "/stuff"+"/"+coursename+"/"+i
        link_list.append(link)

    url= database.child('course').child(coursename).child(videoname).child('url').get(idtoken).val()

    combine_list = zip(videos1,link_list)
    return render(request, "home/video_page.html", {'combine_list':combine_list,"coursetitle":coursename,"videotitle":videoname,"url":url})

def addexternalcourse(request):
    if request.method == 'GET':
        return render(request, "home/addexternalcourses.html")

    else:
        print("falak")
        course_name = request.POST.get('course_name')
        link = request.POST.get('link')
        tags = request.POST.get('tags')


        try:
            idtoken = request.session['uid']
            a = authe.get_account_info(idtoken)
            a = a['users']
            a = a[0]
            a = a['localId']
            # a contains local id
        except:
            return render(request, "accounts/login.html")

        username = database.child("users").child(a).child("details").child("username").get(idtoken).val()
        #print(username)
        data = {
            "tags": tags,
            "link": link,
            "username": username,
        }

        database.child('externalcourses').child(course_name).set(data, idtoken)
        return render(request, "home/addexternalcourses.html")

def external_course_list(request):

    try:
        idtoken = request.session['uid']
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        # a contains local id
    except:
        return render(request, "accounts/login.html")
    courses = database.child('externalcourses').shallow().get(idtoken).val()
    print(courses)
    list_courses = [*courses]
    print(list_courses)
    link_lists = []
    
    for i in list_courses:
        link = database.child('externalcourses').child(i).child('link').get(idtoken).val()
        link_lists.append(link)
    print(link_lists)
    combine_list = zip(list_courses,link_lists)
    return render(request, "home/externalcourses.html", {'combine_list':combine_list})