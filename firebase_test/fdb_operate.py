from firebase import firebase
db_url 'https://cgenfust.firebaseio.com'
fdb = firebase.FirebaseApplication(db_url, None)

while True:
    inv_lotto = dict()
    inv_month = input('')