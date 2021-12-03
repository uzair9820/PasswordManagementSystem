from django.shortcuts import render,HttpResponse
from .pgenerator import gen
import pyrebase
from .encode import encode_decode

g = gen()
d = encode_decode()

#Firebase Project Config
config={
    "apiKey" : "AIzaSyAGxztji_cdW9KEWV_OW6qCagIRXiFnnh4",
    "authDomain": "pythonprojectsem4.firebaseapp.com",
    "databaseURL": "https://pythonprojectsem4-default-rtdb.firebaseio.com",
    "projectId": "pythonprojectsem4",
    "storageBucket": "pythonprojectsem4.appspot.com",
    "messagingSenderId": "925003264368",
    "appId": "1:925003264368:web:b5f9228b3b269c63e51fb5",
    "serviceAccount": "F:\Python\Mini Project\PythonMiniProject\pythonprojectsem4-firebase-adminsdk-aw002-d26c031d2b.json",
}

#Intializing Firebase, Firebase Authentication, Firebase Database
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()

# Create your views here.
def home(request):
    return render(request,"index.html")

def index(request):
    return render(request,"index.html")

def signin(request):
    return render(request,"signin.html")

def postsignin(request):
    email=request.POST.get('email')
    pasw=request.POST.get('password')
    try:
        user = auth.sign_in_with_email_and_password(email,pasw)
        request.session['uid'] = user['localId']
        request.session['Email'] = user['email']
        Email = user['email'] 
    except:
        message="Invalid Credentials!"
        return render(request,"signin.html",{"message":message})
    return render(request,"generator.html",{'Email':Email})

def signup(request):
    return render(request,"signup.html")

def postsignup(request):
    email = request.POST.get("email")
    passs = request.POST.get("password")
    name = request.POST.get("name")
    message="Sign Up Unsuccessful!"
    try:
        #creating a user with the given email and password
        user = auth.create_user_with_email_and_password(email,passs)
        details = {'Name':name , 'Email':email}
        uid = user['localId']
        database.child("Users/"+uid).set(details)
    except:
        return render(request, "signup.html",{"message":message})
    return render(request,"signin.html")

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"signin.html")

def generator(request):
    Email = request.session['Email']
    return render(request,"generator.html",{'Email':Email})

def manager(request):
    Email = request.session['Email']
    return render(request,"manager.html",{'Email':Email})

def generate(request):
    length = int(request.POST["length"])
    radio = request.POST["flexRadioDefault"]
    password = g.generatepass(length,radio)
    Email = request.session['Email']
    return render(request,"generator.html",{'password':password,'Email':Email})

def copy(request):
    password = request.POST.get("password")
    g.copy1(password)
    Email = request.session['Email']
    return render(request,"generator.html",{'Email':Email})

def add(request):
    web = request.POST.get("website")
    uname = request.POST.get("username")
    pasw = request.POST.get("pass")
    message="Operation Failed!"
    Email = request.session['Email']
    try:
        uid = request.session['uid']
        data = {'Website':web,'Username':uname,'EncodedPass':d.encodepass(pasw)}
        database.child("Users/"+uid+"/Manager").push(data)
    except:
        return render(request,"manager.html",{'message':message})
    return render(request,"manager.html",{'Email':Email})

def showsaveddata(request):
    uid = request.session['uid'] 
    message = "No Saved Data"
    b = 1
    Email = request.session['Email']
    try:
        if uid!=None:
            passdata = database.child("Users/"+uid+"/Manager").order_by_key().get()
            key = []
            srno = []
            web = []
            uname = []
            pasw = []
            a = 1
            for data in passdata.each():
                key.append(data.key())
                web.append(data.val()["Website"])
                uname.append(data.val()["Username"])
                pasw.append(d.decodepass(data.val()["EncodedPass"]))
                srno.append(a)
                a = a + 1
        final = zip(key,srno,web,uname,pasw)
    except:
        return render(request,"manager.html",{'message':message,'Email':Email})
    return render(request,"manager.html",{'final': final,'b':b,'Email':Email})

def hidesaveddata(request):
    Email = request.session['Email']
    return render(request,'manager.html',{'Email':Email})

def delete(request):
    uid = request.session['uid']
    key = request.POST.get('key')
    database.child("Users/"+uid+"/Manager").child(key).remove()
    Email = request.session['Email']
    return render(request,'manager.html',{'Email':Email})