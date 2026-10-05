def memenuhi_syarat(formulir, nilai, kehadiran, sanksi):
    if not formulir:
        return "Tidak dapat mengikuti praktikum: formulir belum diisi"
    elif nilai <= 60:
        return "Tidak dapat mengikuti praktikum: nilai kurang dari 60"
    elif kehadiran < 75:
        return "Tidak dapat mengikuti praktikum: kehadiran kurang dari 75"
    elif sanksi:
        return "Tidak dapat mengikuti praktikum: mahasiswa memiliki sanksi"
    else:
        return "Dapat mengikuti praktikum"

data = (True, 70, 85,True)
print(memenuhi_syarat(*data))