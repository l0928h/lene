#

import pyrebase,time
config = {
    "apiKey": "",
    "authDomain": "mooji-app.firebaseapp.com",
    "databaseURL": "https://mooji-app.firebaseio.com",
    "projectId": "mooji-app",
    "storageBucket": "mooji-app.appspot.com",
    "messagingSenderId": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("email", "password")

db = firebase.database()

new_users = [
    {'name': 'len'},
    {'name': 'raymond'},
    {'name': 'hiew'},
    {'name': ''}
]

for user in new_users:
    print("store the data", u)
    db.child('user').push(u, user['idToken'])
    time.sleep(3)