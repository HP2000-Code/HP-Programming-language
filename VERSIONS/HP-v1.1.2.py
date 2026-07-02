# HP™ Programming language | 2026 - 1405 © | Developed by Hossein P. & Mr. CG. | Powered by Python

# imports
import os
import sys
import math
import platform
import datetime
import random

v = "1.1.2" # نسخه

# حافظه متغیرها
moteghayyer_esm_1 = ""
moteghayyer_meghdar_1 = ""
moteghayyer_esm_2 = ""
moteghayyer_meghdar_2 = ""
moteghayyer_esm_3 = ""
moteghayyer_meghdar_3 = ""
moteghayyer_esm_4 = ""
moteghayyer_meghdar_4 = ""
moteghayyer_esm_5 = ""
moteghayyer_meghdar_5 = ""
moteghayyer_esm_6 = ""
moteghayyer_meghdar_6 = ""
moteghayyer_esm_7 = ""
moteghayyer_meghdar_7 = ""
moteghayyer_esm_8 = ""
moteghayyer_meghdar_8 = ""
moteghayyer_esm_9 = ""
moteghayyer_meghdar_9 = ""
moteghayyer_esm_10 = ""
moteghayyer_meghdar_10 = ""
moteghayyer_esm_11 = ""
moteghayyer_meghdar_11 = ""
moteghayyer_esm_12 = ""
moteghayyer_meghdar_12 = ""
moteghayyer_esm_13 = ""
moteghayyer_meghdar_13 = ""
moteghayyer_esm_14 = ""
moteghayyer_meghdar_14 = ""
moteghayyer_esm_15 = ""
moteghayyer_meghdar_15 = ""
moteghayyer_esm_16 = ""
moteghayyer_meghdar_16 = ""
moteghayyer_esm_17 = ""
moteghayyer_meghdar_17 = ""
moteghayyer_esm_18 = ""
moteghayyer_meghdar_18 = ""
moteghayyer_esm_19 = ""
moteghayyer_meghdar_19 = ""
moteghayyer_esm_20 = ""
moteghayyer_meghdar_20 = ""
moteghayyer_esm_21 = ""
moteghayyer_meghdar_21 = ""
moteghayyer_esm_22 = ""
moteghayyer_meghdar_22 = ""
moteghayyer_esm_23 = ""
moteghayyer_meghdar_23 = ""
moteghayyer_esm_24 = ""
moteghayyer_meghdar_24 = ""
moteghayyer_esm_25 = ""
moteghayyer_meghdar_25 = ""
moteghayyer_esm_26 = ""
moteghayyer_meghdar_26 = ""
moteghayyer_esm_27 = ""
moteghayyer_meghdar_27 = ""
moteghayyer_esm_28 = ""
moteghayyer_meghdar_28 = ""
moteghayyer_esm_29 = ""
moteghayyer_meghdar_29 = ""
moteghayyer_esm_30 = ""
moteghayyer_meghdar_30 = ""
moteghayyer_esm_31 = ""
moteghayyer_meghdar_31 = ""
moteghayyer_esm_32 = ""
moteghayyer_meghdar_32 = ""
moteghayyer_esm_33 = ""
moteghayyer_meghdar_33 = ""
moteghayyer_esm_34 = ""
moteghayyer_meghdar_34 = ""
moteghayyer_esm_35 = ""
moteghayyer_meghdar_35 = ""
moteghayyer_esm_36 = ""
moteghayyer_meghdar_36 = ""
moteghayyer_esm_37 = ""
moteghayyer_meghdar_37 = ""
moteghayyer_esm_38 = ""
moteghayyer_meghdar_38 = ""
moteghayyer_esm_39 = ""
moteghayyer_meghdar_39 = ""
moteghayyer_esm_40 = ""
moteghayyer_meghdar_40 = ""
moteghayyer_esm_41 = ""
moteghayyer_meghdar_41 = ""
moteghayyer_esm_42 = ""
moteghayyer_meghdar_42 = ""
moteghayyer_esm_43 = ""
moteghayyer_meghdar_43 = ""
moteghayyer_esm_44 = ""
moteghayyer_meghdar_44 = ""
moteghayyer_esm_45 = ""
moteghayyer_meghdar_45 = ""
moteghayyer_esm_46 = ""
moteghayyer_meghdar_46 = ""
moteghayyer_esm_47 = ""
moteghayyer_meghdar_47 = ""
moteghayyer_esm_48 = ""
moteghayyer_meghdar_48 = ""
moteghayyer_esm_49 = ""
moteghayyer_meghdar_49 = ""
moteghayyer_esm_50 = ""
moteghayyer_meghdar_50 = ""
moteghayyer_esm_51 = ""
moteghayyer_meghdar_51 = ""
moteghayyer_esm_52 = ""
moteghayyer_meghdar_52 = ""
moteghayyer_esm_53 = ""
moteghayyer_meghdar_53 = ""
moteghayyer_esm_54 = ""
moteghayyer_meghdar_54 = ""
moteghayyer_esm_55 = ""
moteghayyer_meghdar_55 = ""
moteghayyer_esm_56 = ""
moteghayyer_meghdar_56 = ""
moteghayyer_esm_57 = ""
moteghayyer_meghdar_57 = ""
moteghayyer_esm_58 = ""
moteghayyer_meghdar_58 = ""
moteghayyer_esm_59 = ""
moteghayyer_meghdar_59 = ""
moteghayyer_esm_60 = ""
moteghayyer_meghdar_60 = ""
moteghayyer_esm_61 = ""
moteghayyer_meghdar_61 = ""
moteghayyer_esm_62 = ""
moteghayyer_meghdar_62 = ""
moteghayyer_esm_63 = ""
moteghayyer_meghdar_63 = ""
moteghayyer_esm_64 = ""
moteghayyer_meghdar_64 = ""
moteghayyer_esm_65 = ""
moteghayyer_meghdar_65 = ""
moteghayyer_esm_66 = ""
moteghayyer_meghdar_66 = ""
moteghayyer_esm_67 = ""
moteghayyer_meghdar_67 = ""
moteghayyer_esm_68 = ""
moteghayyer_meghdar_68 = ""
moteghayyer_esm_69 = ""
moteghayyer_meghdar_69 = ""
moteghayyer_esm_70 = ""
moteghayyer_meghdar_70 = ""
moteghayyer_esm_71 = ""
moteghayyer_meghdar_71 = ""
moteghayyer_esm_72 = ""
moteghayyer_meghdar_72 = ""
moteghayyer_esm_73 = ""
moteghayyer_meghdar_73 = ""
moteghayyer_esm_74 = ""
moteghayyer_meghdar_74 = ""
moteghayyer_esm_75 = ""
moteghayyer_meghdar_75 = ""
moteghayyer_esm_76 = ""
moteghayyer_meghdar_76 = ""
moteghayyer_esm_77 = ""
moteghayyer_meghdar_77 = ""
moteghayyer_esm_78 = ""
moteghayyer_meghdar_78 = ""
moteghayyer_esm_79 = ""
moteghayyer_meghdar_79 = ""
moteghayyer_esm_80 = ""
moteghayyer_meghdar_80 = ""
moteghayyer_esm_81 = ""
moteghayyer_meghdar_81 = ""
moteghayyer_esm_82 = ""
moteghayyer_meghdar_82 = ""
moteghayyer_esm_83 = ""
moteghayyer_meghdar_83 = ""
moteghayyer_esm_84 = ""
moteghayyer_meghdar_84 = ""
moteghayyer_esm_85 = ""
moteghayyer_meghdar_85 = ""
moteghayyer_esm_86 = ""
moteghayyer_meghdar_86 = ""
moteghayyer_esm_87 = ""
moteghayyer_meghdar_87 = ""
moteghayyer_esm_88 = ""
moteghayyer_meghdar_88 = ""
moteghayyer_esm_89 = ""
moteghayyer_meghdar_89 = ""
moteghayyer_esm_90 = ""
moteghayyer_meghdar_90 = ""
moteghayyer_esm_91 = ""
moteghayyer_meghdar_91 = ""
moteghayyer_esm_92 = ""
moteghayyer_meghdar_92 = ""
moteghayyer_esm_93 = ""
moteghayyer_meghdar_93 = ""
moteghayyer_esm_94 = ""
moteghayyer_meghdar_94 = ""
moteghayyer_esm_95 = ""
moteghayyer_meghdar_95 = ""
moteghayyer_esm_96 = ""
moteghayyer_meghdar_96 = ""
moteghayyer_esm_97 = ""
moteghayyer_meghdar_97 = ""
moteghayyer_esm_98 = ""
moteghayyer_meghdar_98 = ""
moteghayyer_esm_99 = ""
moteghayyer_meghdar_99 = ""
moteghayyer_esm_100 = ""
moteghayyer_meghdar_100 = ""

# صفحه اصلی | منو
print("▪︎ اپلیکیشن زبان برنامه‌نویسی HP ▪︎")

# خطاها
khata_1 = "• خطا! مشکلی در کُد شما وجود داره...!"
khata_2 = "• خطا! مشکلی در اپلیکیشن وجود داره...!"
khata_3 = "• خطا! مشکلی ناشناخته وجود داره...!"
khata_voroudi_adad = "- لطفا یک عدد وارد نمایید!"

# متغیرها
dastour_chap = "چاپ"
dastour_chap_2 = "نمایش"
dastour_khorouj = "خروج"
dastour_ettelaat = "اطلاعات"
dastour_help = "راهنما"
dastour_sistem = "سیستم"
dastour_tarikh = "تاریخ"
dastour_zaman = "زمان"
dastour_sakhtan_moteghayyer = "متغیر"
dastour_namayesh_moteghayyer = "نمایش متغیر"
dastour_jam = "جمع"
dastour_tafrigh = "تفریق"
dastour_zarb = "ضرب"
dastour_taghsim = "تقسیم"
dastour_tavan = "توان"
dastour_baghimandeh = "باقی مانده"
dastour_rendom = "رندوم"
dastour_jazr = "جذر"
dastour_gerdkardan_be_bala = "گرد کردن به بالا"
dastour_gerdkardan_be_payin = "گرد کردن به پایین"
dastour_hazf_ashar = "حذف اعشار"
dastour_ghadr_motlagh = "قدر مطلق"
dastour_faktoriyel = "فاکتوریل"
dastour_b_m_m = "ب.م.م"
dastour_b_m_m_2 = "بزرگ ترین مقسوم علیه مشترک"
dastour_k_m_m = "ک.م.م"
dastour_k_m_m_2 = "کوچک ترین مضرب مشترک"
dastour_sin = "سینوس"
dastour_cos = "کسینوس"
dastour_tan = "تانژانت"
dastour_asin = "معکوس سینوس"
dastour_acos = "معکوس کسینوس"
dastour_atan = "معکوس تانژانت"
dastour_atan2 = "زاویه از ۲ مقدار"
dastour_radiyan_be_darjeh = "رادیان به درجه"
dastour_darjeh_be_radiyan = "درجه به رادیان"
dastour_legaritm_tabiei = "لگاریتم طبیعی"
dastour_legaritm_ba_payeh_delkhah = "لگاریتم با پایه دلخواه"
dastour_legaritm_payeh_10 = "لگاریتم پایه ۱۰"
dastour_legaritm_payeh_2 = "لگاریتم پایه ۲"
dastour_tarkib = "ترکیب"
dastour_jaygasht = "جایگشت"
dastour_chap_adad_pi = "چاپ عدد پی"
dastour_chap_adad_e = "چاپ عدد اویلر"
dastour_chap_2pi = "چاپ ۲ برابر عدد پی"
dastour_chap_binahayat = "چاپ بی نهایت"
dastour_chap_adad_nan = "چاپ عدد نامعتبر"

# defs
def chap():
    print()
    matn = input("• متن مورد نظر خود را وارد نمایید: ")
    print("▪︎ نتیجه: " , matn)

def khorouj():
    print()
    print("▪︎ نتیجه: ", "• پایان؛ خدانگهدار تا دفعه بعد...!")
    
def ettelaat():
    print()
    print("▪︎ HP™ Programming language V", v, "| 2026 - 1405 © | Developed by Hossein P. & Mr. CG. | Powered by Python ▪︎")

def help():
    print()
    print("ابتدا در قسمت کُد دستور مورد نظر خود را وارد نمایید و سپس به درخواست دستور پاسخ بدهید تا نتیجه را دریافت نمایید")
    
def sistem():
    print()
    print("▪︎ سیستم عامل: ", platform.system())
    print("▪︎ نسخه سیستم: ", platform.release())
    print("▪︎ نسخه پایتون: ", sys.version.split()[0])
    
def tarikh():
    print()
    natijeh = datetime.datetime.now().date()
    print("▪︎ نتیجه: ", natijeh)

def zaman():
    print()
    natijeh = datetime.datetime.now().time()
    print("▪︎ نتیجه: ", natijeh)
    
def moteghayyer():
    global moteghayyer_esm_1, moteghayyer_meghdar_1
    global moteghayyer_esm_2, moteghayyer_meghdar_2
    global moteghayyer_esm_3, moteghayyer_meghdar_3
    global moteghayyer_esm_4, moteghayyer_meghdar_4
    global moteghayyer_esm_5, moteghayyer_meghdar_5
    global moteghayyer_esm_6, moteghayyer_meghdar_6
    global moteghayyer_esm_7, moteghayyer_meghdar_7
    global moteghayyer_esm_8, moteghayyer_meghdar_8
    global moteghayyer_esm_9, moteghayyer_meghdar_9
    global moteghayyer_esm_10, moteghayyer_meghdar_10

    esm = input("نام متغیر: ")
    meghdar = input("مقدار متغیر: ")

    if esm == moteghayyer_esm_1:
        moteghayyer_meghdar_1 = meghdar
    elif esm == moteghayyer_esm_2:
        moteghayyer_meghdar_2 = meghdar
    elif esm == moteghayyer_esm_3:
        moteghayyer_meghdar_3 = meghdar
    elif esm == moteghayyer_esm_4:
        moteghayyer_meghdar_4 = meghdar
    elif esm == moteghayyer_esm_5:
        moteghayyer_meghdar_5 = meghdar
    elif esm == moteghayyer_esm_6:
        moteghayyer_meghdar_6 = meghdar
    elif esm == moteghayyer_esm_7:
        moteghayyer_meghdar_7 = meghdar
    elif esm == moteghayyer_esm_8:
        moteghayyer_meghdar_8 = meghdar
    elif esm == moteghayyer_esm_9:
        moteghayyer_meghdar_9 = meghdar
    elif esm == moteghayyer_esm_10:
        moteghayyer_meghdar_10 = meghdar

    elif moteghayyer_esm_1 == "":
        moteghayyer_esm_1 = esm
        moteghayyer_meghdar_1 = meghdar
    elif moteghayyer_esm_2 == "":
        moteghayyer_esm_2 = esm
        moteghayyer_meghdar_2 = meghdar
    elif moteghayyer_esm_3 == "":
        moteghayyer_esm_3 = esm
        moteghayyer_meghdar_3 = meghdar
    elif moteghayyer_esm_4 == "":
        moteghayyer_esm_4 = esm
        moteghayyer_meghdar_4 = meghdar
    elif moteghayyer_esm_5 == "":
        moteghayyer_esm_5 = esm
        moteghayyer_meghdar_5 = meghdar
    elif moteghayyer_esm_6 == "":
        moteghayyer_esm_6 = esm
        moteghayyer_meghdar_6 = meghdar
    elif moteghayyer_esm_7 == "":
        moteghayyer_esm_7 = esm
        moteghayyer_meghdar_7 = meghdar
    elif moteghayyer_esm_8 == "":
        moteghayyer_esm_8 = esm
        moteghayyer_meghdar_8 = meghdar
    elif moteghayyer_esm_9 == "":
        moteghayyer_esm_9 = esm
        moteghayyer_meghdar_9 = meghdar
    elif moteghayyer_esm_10 == "":
        moteghayyer_esm_10 = esm
        moteghayyer_meghdar_10 = meghdar
    else:
        print("متاسفانه حافظه متغیرها پر شده است!")

def namayesh_moteghayyer():
    esm = input("نام متغیر: ")

    if esm == moteghayyer_esm_1:
        print(moteghayyer_meghdar_1)
    elif esm == moteghayyer_esm_2:
        print(moteghayyer_meghdar_2)
    elif esm == moteghayyer_esm_3:
        print(moteghayyer_meghdar_3)
    elif esm == moteghayyer_esm_4:
        print(moteghayyer_meghdar_4)
    elif esm == moteghayyer_esm_5:
        print(moteghayyer_meghdar_5)
    elif esm == moteghayyer_esm_6:
        print(moteghayyer_meghdar_6)
    elif esm == moteghayyer_esm_7:
        print(moteghayyer_meghdar_7)
    elif esm == moteghayyer_esm_8:
        print(moteghayyer_meghdar_8)
    elif esm == moteghayyer_esm_9:
        print(moteghayyer_meghdar_9)
    elif esm == moteghayyer_esm_10:
        print(moteghayyer_meghdar_10)

    else:
        print("متاسفانه متغیر پیدا نشد!")

def gereftan_adad():
    adad_1 = int(input("عدد اول را وارد نمایید: "))
    adad_2 = int(input("عدد دوم را وارد نمایید: "))
    return adad_1, adad_2
    
def jam():
    print()
    try:
        adad_1, adad_2 = gereftan_adad()
        natijeh = adad_1 + adad_2
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)
        
def tafrigh():
    print()
    try:  
        adad_1, adad_2 = gereftan_adad()
        natijeh = adad_1 - adad_2
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)    
        print(khata_voroudi_adad)

def zarb():
    print()
    try:  
        adad_1, adad_2 = gereftan_adad()
        natijeh = adad_1 * adad_2
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)    
        print(khata_voroudi_adad)
        
def taghsim():
    print()
    try:
        adad_1, adad_2 = gereftan_adad()
        if adad_2 == 0:
            print(khata_1)
            print("- تقسیم بر صفر امکان‌پذیر نیست!")
        else:
            natijeh = adad_1 / adad_2
            print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def tavan():
    print()
    try:
        adad_1, adad_2 = gereftan_adad()
        natijeh = adad_1 ** adad_2
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)
        
def baghimandeh():
    print()
    try:
        adad_1, adad_2 = gereftan_adad()
        if adad_2 == 0:
            print(khata_1)
            print("- باقی‌مانده با عدد صفر امکان‌پذیر نیست!")
        else:
            natijeh = adad_1 % adad_2
            print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)
        
def rendom():
    print()
    try:
        adad_1 = int(input("شروع بازه: "))
        adad_2 = int(input("پایان بازه: "))
        natijeh = random.randint(adad_1, adad_2)
        print("▪︎ نتیجه:", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)
        
def jazr():
    print()
    try:
        adad_1 = int(input("عدد را وارد نمایید: "))
        natijeh = math.sqrt(adad_1)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)
        
def gerdkardan_be_bala():
    print()
    try:
        adad = float(input("عدد را وارد نمایید: "))
        natijeh = math.ceil(adad)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def gerdkardan_be_payin():
    print()
    try:
        adad = float(input("عدد را وارد نمایید: "))
        natijeh = math.floor(adad)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def hazf_ashar():
    print()
    try:
        adad = float(input("عدد را وارد نمایید: "))
        natijeh = math.trunc(adad)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def ghadr_motlagh():
    print()
    try:
        adad = float(input("عدد را وارد نمایید: "))
        natijeh = abs(adad)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def faktoriyel():
    print()
    try:
        adad = int(input("عدد را وارد نمایید: "))
        if adad < 0:
            print(khata_1)
            print("- فاکتوریل عدد منفی وجود ندارد!")
        else:
            natijeh = math.factorial(adad)
            print("▪︎ نتیجه: ", natijeh)

    except:
        print(khata_1)
        print(khata_voroudi_adad)

def b_m_m():
    print()
    try:
        adad_1, adad_2 = gereftan_adad()
        natijeh = math.gcd(adad_1, adad_2)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def k_m_m():
    print()
    try:
        adad_1, adad_2 = gereftan_adad()
        natijeh = abs(adad_1 * adad_2) // math.gcd(adad_1, adad_2)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)
        
def sin():
    print()
    try:
        adad = float(input("زاویه را وارد نمایید (رادیان): "))
        natijeh = math.sin(adad)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def cos():
    print()
    try:
        adad = float(input("زاویه را وارد نمایید (رادیان): "))
        natijeh = math.cos(adad)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def tan():
    print()
    try:
        adad = float(input("زاویه را وارد نمایید (رادیان): "))
        natijeh = math.tan(adad)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def asin():
    print()
    try:
        adad = float(input("عدد را وارد نمایید: "))
        natijeh = math.asin(adad)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def acos():
    print()
    try:
        adad = float(input("عدد را وارد نمایید: "))
        natijeh = math.acos(adad)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def atan():
    print()
    try:
        adad = float(input("عدد را وارد نمایید: "))
        natijeh = math.atan(adad)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def atan2():
    print()
    try:
        adad_1, adad_2 = gereftan_adad()
        natijeh = math.atan2(adad_1, adad_2)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def radiyan_be_darjeh():
    print()
    try:
        adad = float(input("زاویه رادیانی را وارد نمایید: "))
        natijeh = math.degrees(adad)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def darjeh_be_radiyan():
    print()
    try:
        adad = float(input("زاویه درجه‌ای را وارد نمایید: "))
        natijeh = math.radians(adad)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)
        
def legaritm_tabiei():
    print()
    try:
        adad = float(input("عدد را وارد نمایید: "))
        natijeh = math.log(adad)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def legaritm_ba_payeh_delkhah():
    print()
    try:
        adad = float(input("عدد را وارد نمایید: "))
        payeh = float(input("پایه لگاریتم را وارد نمایید: "))
        natijeh = math.log(adad, payeh)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def legaritm_payeh_10():
    print()
    try:
        adad = float(input("عدد را وارد نمایید: "))
        natijeh = math.log10(adad)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def legaritm_payeh_2():
    print()
    try:
        adad = float(input("عدد را وارد نمایید: "))
        natijeh = math.log2(adad)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def tarkib():
    print()
    try:
        n = int(input("تعداد کل | n را وارد نمایید: "))
        r = int(input("تعداد انتخاب | r را وارد نمایید: "))
        natijeh = math.comb(n, r)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def jaygasht():
    print()
    try:
        n = int(input("تعداد کل | n را وارد نمایید: "))
        r = int(input("تعداد انتخاب | r را وارد نمایید: "))
        natijeh = math.perm(n, r)
        print("▪︎ نتیجه: ", natijeh)
    except:
        print(khata_1)
        print(khata_voroudi_adad)

def chap_adad_pi():
    print()
    print("▪︎ نتیجه: ", math.pi)

def chap_adad_e():
    print()
    print("▪︎ نتیجه: ", math.e)

def chap_2pi():
    print()
    print("▪︎ نتیجه: ", 2 * math.pi)

def chap_binahayat():
    print()
    print("▪︎ نتیجه: ", math.inf)

def chap_adad_nan():
    print()
    print("▪︎ نتیجه: ", math.nan)

# صفحه اصلی | قسمت کُدنویسی
while True:
    print()
    voroudi = input("▪︎ کُد: ")
    if voroudi == dastour_chap or voroudi == dastour_chap_2:
        chap()
    elif voroudi == dastour_khorouj:
        khorouj()
        break
    elif voroudi == dastour_ettelaat:
        ettelaat()
    elif voroudi == dastour_help:
        help()
    elif voroudi == dastour_sistem:
        sistem()
    elif voroudi == dastour_tarikh:
        tarikh()
    elif voroudi == dastour_zaman:
        zaman()
    elif voroudi == dastour_sakhtan_moteghayyer:
        moteghayyer()
    elif voroudi == dastour_namayesh_moteghayyer:
        namayesh_moteghayyer()
    elif voroudi == dastour_jam:
        jam()
    elif voroudi == dastour_tafrigh:
        tafrigh()
    elif voroudi == dastour_zarb:
        zarb()
    elif voroudi == dastour_taghsim:
        taghsim()
    elif voroudi == dastour_tavan:
        tavan()
    elif voroudi == dastour_baghimandeh:
        baghimandeh()
    elif voroudi == dastour_rendom:
        rendom()
    elif voroudi == dastour_jazr:
        jazr()
    elif voroudi == dastour_gerdkardan_be_bala:
        gerdkardan_be_bala()
    elif voroudi == dastour_gerdkardan_be_payin:
        gerdkardan_be_payin()
    elif voroudi == dastour_hazf_ashar:
        hazf_ashar()
    elif voroudi == dastour_ghadr_motlagh:
        ghadr_motlagh()
    elif voroudi == dastour_faktoriyel:
        faktoriyel()
    elif voroudi == dastour_b_m_m:
        b_m_m()
    elif voroudi == dastour_b_m_m_2:
        b_m_m()
    elif voroudi == dastour_k_m_m:
        k_m_m()
    elif voroudi == dastour_k_m_m_2:
        k_m_m()
    elif voroudi == dastour_sin:
        sin()
    elif voroudi == dastour_cos:
        cos()
    elif voroudi == dastour_tan:
        tan()
    elif voroudi == dastour_asin:
        asin()
    elif voroudi == dastour_acos:
        acos()
    elif voroudi == dastour_atan:
        atan()
    elif voroudi == dastour_atan2:
        atan2()
    elif voroudi == dastour_radiyan_be_darjeh:
        radiyan_be_darjeh()
    elif voroudi == dastour_darjeh_be_radiyan:
        darjeh_be_radiyan()
    elif voroudi == dastour_legaritm_tabiei:
        legaritm_tabiei()
    elif voroudi == dastour_legaritm_ba_payeh_delkhah:
        legaritm_ba_payeh_delkhah()
    elif voroudi == dastour_legaritm_payeh_10:
        legaritm_payeh_10()
    elif voroudi == dastour_legaritm_payeh_2:
        legaritm_payeh_2()
    elif voroudi == dastour_tarkib:
        tarkib()
    elif voroudi == dastour_jaygasht:
        jaygasht()
    elif voroudi == dastour_chap_adad_pi:
        chap_adad_pi()
    elif voroudi == dastour_chap_adad_e:
        chap_adad_e()
    elif voroudi == dastour_chap_2pi:
        chap_2pi()
    elif voroudi == dastour_chap_binahayat:
        chap_binahayat()
    elif voroudi == dastour_chap_adad_nan:
        chap_adad_nan()
    else:
        print()
        print(khata_1)
        print("- دستور", voroudi, "هنوز ناشناخته است!")
