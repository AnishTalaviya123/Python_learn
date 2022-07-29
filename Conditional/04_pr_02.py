spamword = ['buy now','subscribe now', 'click now']
email = "this is a nice stock.you need to click this and buy now "

if('buy now'in email):
    spam = True

if('subscribe now'in email):
    spam = True
    
if('Click now'in email):
    spam = True

print("Spam is", spam)