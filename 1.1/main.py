from Classes.mail import MailScr
from Classes.phone import PhoneScr
from Classes.skype import SkypeScr

m = MailScr("M14ur1nAK@yandex.ru")
print(m.screening())

ph = PhoneScr("+7 906 932   5561", 5)
print(ph.screening())

s1 = SkypeScr("skype:michurin")
s2 = SkypeScr('<a href="skype:michurin?call">Hey!</a>')

print(s1.screening())
print(s2.screening())
