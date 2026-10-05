print("study kasus 1")
username_benar = True
password_benar = True
akun_aktif = True

login = username_benar and password_benar and akun_aktif

print("Status login:", login)

print("study kasus 2")
username_benar = True
password_benar = True
akun_aktif = False

login = username_benar and password_benar and akun_aktif

print("Status login:", login) 

print("study kasus 3")
username_benar = True
password_benar = False
akun_aktif = True

login = username_benar and password_benar and akun_aktif

print("Status login:", login)

print("study kasus 4")
username_benar = False
password_benar = True
akun_aktif = True

login = username_benar and password_benar and akun_aktif

print("Status login:", login)