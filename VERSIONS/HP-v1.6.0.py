# HP™ Programming language | 2026 - 1405 © | Developed by Hossein P. & Mr. CG. | Powered by Python

# imports
import os
import sys
import math
import json
import re
import platform
import datetime
import random

VERSION = "1.6.0"
GMAIL_SUPPORT = ("HP.SUPPORT.2026@gmail.com")

# ساخت پوشه ذخیره پروژه‌ها
PROJECT_FOLDER = "HP_Projects"
VARIABLE_FILE = "hp_variables.json"
if not os.path.exists(PROJECT_FOLDER):
    os.mkdir(PROJECT_FOLDER)

def safe_name(name):
    """
    جلوگیری از اسم‌های خطرناک فایل
    """
    name = name.strip()
    if name == "":
        i = 1
        while True:
            filename = f"Code_{i}.hp"
            if not os.path.exists(os.path.join(PROJECT_FOLDER, filename)):
                return filename
            i += 1
    if name.endswith(".hp"):
        name = name[:-3]
    name = re.sub(r'[^a-zA-Z0-9_\u0600-\u06FF]', '_', name)
    return name + ".hp"
    
def project_path(name):
    return os.path.join(PROJECT_FOLDER, safe_name(name))

# صفحه اصلی | منو
print("▪︎ اپلیکیشن زبان برنامه‌نویسی HP ▪︎")

# خطاها
khata_1 = "• خطا! مشکلی در کُد شما وجود داره...!"
khata_2 = "• خطا! مشکلی در اپلیکیشن وجود داره...!"
khata_3 = "• خطا! مشکلی ناشناخته وجود داره...!"
khata_voroudi_adad = "- لطفا یک عدد وارد نمایید!"

# متغیرها
dastour_kod = "کدنویسی"
dastour_chap = "چاپ"
dastour_chap_2 = "نمایش"
dastour_khorouj = "خروج"
dastour_ettelaat = "اطلاعات"
dastour_poshtibani = "پشتیبانی"
dastour_zakhire = "ذخیره"
dastour_list_zakhire = "لیست ذخیره"
dastour_etelaat_zakhire = "اطلاعات ذخیره"
dastour_taghir_nam_zakhire = "تغییر نام ذخیره"
dastour_ejra_zakhire = "اجرا ذخیره"
dastour_virayesh_zakhire = "ویرایش ذخیره"
dastour_hazf_zakhire = "حذف ذخیره"
dastour_menu_zakhire = "مدیریت ذخیره"
dastour_help = "راهنما"
dastour_sistem = "سیستم"
dastour_tarikh = "تاریخ"
dastour_zaman = "زمان"
dastour_sakhtan_moteghayyer = "متغیر"
dastour_namayesh_moteghayyer = "نمایش متغیر"
dastour_mosavi = "=="
dastour_namosavi = "!="
dastour_bozorgtar = ">"
dastour_koochaktar = "<"
dastour_bozorgtar_mosavi = ">="
dastour_koochaktar_mosavi = "<="
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
def code_writer():
    print("""
▪︎ کد خود را وارد کنید
▪︎ برای پایان نوشتن END; را وارد کنید
""")
    lines = []
    while True:
        line = input()
        if line == "END;":
            break
        lines.append(line)
    code = "\n".join(lines)
    execute_hp(code)
    
def chap():
    print()
    matn = input("• متن مورد نظر خود را وارد نمایید: ")
    print("▪︎ نتیجه: " , matn)

def khorouj():
    print()
    print("▪︎ نتیجه: ", "• پایان؛ خدانگهدار تا دفعه بعد...!")
    
def ettelaat():
    print()
    print("▪︎ HP™ Programming language VERSION", VERSION, "| 2026 - 1405 © | Developed by Hossein P. & Mr. CG. | Powered by Python ▪︎")
    
def moghayeseh(noe):
    print()
    try:
        adad_1 = float(input("عدد اول را وارد نمایید: "))
        adad_2 = float(input("عدد دوم را وارد نمایید: "))
        if noe == "==":
            natijeh = adad_1 == adad_2
        elif noe == "!=":
            natijeh = adad_1 != adad_2
        elif noe == ">":
            natijeh = adad_1 > adad_2
        elif noe == "<":
            natijeh = adad_1 < adad_2
        elif noe == ">=":
            natijeh = adad_1 >= adad_2
        elif noe == "<=":
            natijeh = adad_1 <= adad_2
        else:
            print(khata_1)
            print("- نوع مقایسه نامعتبر است!")
            return
        if natijeh:
            print("▪︎ نتیجه: درست")
        else:
            print("▪︎ نتیجه: نادرست")
    except:
        print(khata_1)
        print(khata_voroudi_adad)
    
def zakhireh():
    print()
    esm = input("نام پروژه: ")
    print("""
▪︎ کد پروژه را وارد کنید
▪︎ برای پایان نوشتن کلمه END; را وارد کنید
""")
    lines = []
    while True:
        line = input()
        if line == "END;":
            break
        lines.append(line)
    code = "\n".join(lines)
    file = project_path(esm)
    data = {
        "name": os.path.splitext(os.path.basename(file))[0],
        "version": VERSION,
        "created": str(datetime.datetime.now()),
        "code": code
    }
    with open(file, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )
    print("▪︎ پروژه با موفقیت ذخیره شد!")

def etelaat_zakhire():
    esm = input("نام پروژه: ")
    file = project_path(esm)
    if os.path.exists(file):
        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:
            data = json.load(f)
        print("""
▪︎ اطلاعات پروژه

نام:
""", data["name"])
        print(
            "نسخه:",
            data["version"]
        )
        print(
            "ساخته شده:",
            data["created"]
        )
        print(
            "حجم کد:",
            len(data["code"]),
            "کاراکتر"
        )
    else:
        print("پروژه پیدا نشد!")

def execute_hp(code):
    """
    اجرای کدهای زبان HP
    """
    lines = code.split("\n")
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        if line.startswith("..."):
            continue
        if line == dastour_chap or line == dastour_chap_2:
            chap()
        elif line == dastour_khorouj:
            khorouj()
            return
        elif line == dastour_mosavi:
            moghayeseh("==")
        elif line == dastour_namosavi:
            moghayeseh("!=")
        elif line == dastour_bozorgtar:
            moghayeseh(">")
        elif line == dastour_koochaktar:
            moghayeseh("<")
        elif line == dastour_bozorgtar_mosavi:
            moghayeseh(">=")
        elif line == dastour_koochaktar_mosavi:
            moghayeseh("<=")
        elif line == dastour_poshtibani:
            poshtibani()
        elif line == dastour_jam:
            jam()
        elif line == dastour_tafrigh:
            tafrigh()
        elif line == dastour_zarb:
            zarb()
        elif line == dastour_taghsim:
            taghsim()
        elif line == dastour_tavan:
            tavan()
        elif line == dastour_baghimandeh:
            baghimandeh()
        elif line == dastour_rendom:
            rendom()
        elif line == dastour_jazr:
            jazr()
        elif line == dastour_gerdkardan_be_bala:
            gerdkardan_be_bala()
        elif line == dastour_gerdkardan_be_payin:
            gerdkardan_be_payin()
        elif line == dastour_hazf_ashar:
            hazf_ashar()
        elif line == dastour_ghadr_motlagh:
            ghadr_motlagh()
        elif line == dastour_faktoriyel:
            faktoriyel()
        elif line == dastour_b_m_m or line == dastour_b_m_m_2:
            b_m_m()
        elif line == dastour_k_m_m or line == dastour_k_m_m_2:
            k_m_m()
        elif line == dastour_sin:
            sin()
        elif line == dastour_cos:
            cos()
        elif line == dastour_tan:
            tan()
        elif line == dastour_asin:
            asin()
        elif line == dastour_acos:
            acos()
        elif line == dastour_atan:
            atan()
        elif line == dastour_atan2:
            atan2()
        elif line == dastour_radiyan_be_darjeh:
            radiyan_be_darjeh()
        elif line == dastour_darjeh_be_radiyan:
            darjeh_be_radiyan()
        elif line == dastour_legaritm_tabiei:
            legaritm_tabiei()
        elif line == dastour_legaritm_ba_payeh_delkhah:
            legaritm_ba_payeh_delkhah()
        elif line == dastour_legaritm_payeh_10:
            legaritm_payeh_10()
        elif line == dastour_legaritm_payeh_2:
            legaritm_payeh_2()
        elif line == dastour_tarkib:
            tarkib()
        elif line == dastour_jaygasht:
            jaygasht()
        elif line == dastour_chap_adad_pi:
            chap_adad_pi()
        elif line == dastour_chap_adad_e:
            chap_adad_e()
        elif line == dastour_chap_2pi:
            chap_2pi()
        elif line == dastour_chap_binahayat:
            chap_binahayat()
        elif line == dastour_chap_adad_nan:
            chap_adad_nan()
        elif line == dastour_ettelaat:
            ettelaat()
        elif line == dastour_sistem:
            sistem()
        elif line == dastour_tarikh:
            tarikh()
        elif line == dastour_zaman:
            zaman()
        elif line == dastour_namayesh_moteghayyer:
            namayesh_moteghayyer()
        elif line == dastour_sakhtan_moteghayyer:
            moteghayyer()
        else:
            print(
                "دستور ذخیره شده ناشناخته است:",
                line
            )
            
def ejra_zakhire():
    esm=input(
        "نام پروژه: "
    )
    file=project_path(esm)
    if os.path.exists(file):
        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:
            data=json.load(f)
        code=data["code"]
        print(
            "▪︎ اجرای پروژه..."
        )
        execute_hp(code)
    else:
        print(
            "پروژه پیدا نشد!"
        )
def virayesh_zakhire():
    esm = input("نام پروژه: ")
    file = project_path(esm)
    if os.path.exists(file):
        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:
            data = json.load(f)
        print("\n▪︎ کد قبلی:")
        print("----------------")
        print(data["code"])
        print("----------------")
        print("""
▪︎ کد جدید را وارد کنید
▪︎ برای پایان ویرایش کلمه END; را وارد کنید
""")
        lines = []
        while True:
            line = input()
            if line == "END;":
                break
            lines.append(line)
        code = "\n".join(lines)
        data["code"] = code
        data["edited"] = str(datetime.datetime.now())
        with open(
            file,
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )
        print("▪︎ پروژه با موفقیت ویرایش شد!")
    else:
        print("پروژه پیدا نشد!")
        
def hazf_zakhire():
    esm=input("نام پروژه: ")
    file=project_path(esm)
    if os.path.exists(file):
        confirm=input(
            "آیا مطمئن هستید؟ (بله/خیر): "
        )
        if confirm=="بله":
            os.remove(file)
            print("پروژه حذف شد.")
        else:
            print("لغو شد.")
    else:
        print("پروژه پیدا نشد!")

def load_variables():
    if os.path.exists(VARIABLE_FILE):
        with open(
            VARIABLE_FILE,
            "r",
            encoding="utf-8"
        ) as f:
            return json.load(f)
    return {}
def save_variables(data):
    with open(
        VARIABLE_FILE,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )
variables = load_variables()

def menu_zakhire():
    while True:
        print("""
▪︎ مدیریت ذخیره

1- لیست پروژه‌ها
2- اطلاعات پروژه
3- تغییر نام
4- حذف پروژه
5- خروج
""")
        entekhab=input("> ")
        if entekhab=="1":
            list_zakhire()
        elif entekhab=="2":
            etelaat_zakhire()
        elif entekhab=="3":
            taghir_nam_zakhire()
        elif entekhab=="4":
            hazf_zakhire()
        elif entekhab=="5":
            break
        else:
            print(
                "گزینه اشتباه!"
            )
            
def taghir_nam_zakhire():
    old = input("نام فعلی: ")
    new = input("نام جدید: ")

    old_file = project_path(old)
    new_file = project_path(new)
    if not os.path.exists(old_file):
        print("پروژه پیدا نشد!")
        return
    if os.path.exists(new_file):
        print("این نام قبلاً وجود دارد!")
        return
    with open(old_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    data["name"] = os.path.splitext(os.path.basename(new_file))[0]
    with open(new_file, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )
    os.remove(old_file)
    print("▪︎ نام پروژه با موفقیت تغییر کرد!")

def list_zakhire():
    print("\n▪︎ پروژه‌های ذخیره شده:\n")
    files = os.listdir(PROJECT_FOLDER)
    if len(files)==0:
        print("هیچ پروژه‌ای وجود ندارد.")
        return
    for i,file in enumerate(files,1):
        print(
            i,
            "-",
            file
        )
        
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
    
def poshtibani():
    print()
    print("• در صورت مواجهه با هرگونه ایراد و اشکال در کارکرد زبان برنامه‌نویسی، و یا داشتن هرگونه نظر، پیشنهاد، انتقاد و یا هرصحبتی در رابطه با این مسائل، حتما به جیمیل پشتیبانی ما، به آدرس زیر ایمیل بزنید:")
    print("▪︎", GMAIL_SUPPORT, "▪︎")
            
def moteghayyer():
    esm = input("نام متغیر: ")
    meghdar = input(
        "مقدار متغیر: "
    )
    variables[esm] = meghdar
    save_variables(variables)
    print(
        "متغیر ذخیره شد."
    )

def namayesh_moteghayyer():
    esm=input(
        "نام متغیر: "
    )
    if esm in variables:
        print(
            "▪︎ مقدار:",
            variables[esm]
        )
    else:
        print(
            "متغیر پیدا نشد!"
        )

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
    if voroudi == dastour_kod:
        code_writer()
    elif voroudi == dastour_chap or voroudi == dastour_chap_2:
        chap()
    elif voroudi == dastour_khorouj:
        khorouj()
        break
    elif voroudi == dastour_ettelaat:
        ettelaat()
    elif voroudi == dastour_poshtibani:
        poshtibani()
    elif voroudi == dastour_zakhire:
        zakhireh()
    elif voroudi == dastour_list_zakhire:
        list_zakhire()
    elif voroudi == dastour_etelaat_zakhire:
        etelaat_zakhire()
    elif voroudi == dastour_taghir_nam_zakhire:
        taghir_nam_zakhire()
    elif voroudi == dastour_ejra_zakhire:
        ejra_zakhire()
    elif voroudi == dastour_virayesh_zakhire:
        virayesh_zakhire()
    elif voroudi == dastour_hazf_zakhire:
        hazf_zakhire()
    elif voroudi == dastour_menu_zakhire:
        menu_zakhire()
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
    elif voroudi == dastour_mosavi:
        moghayeseh("==")
    elif voroudi == dastour_namosavi:
        moghayeseh("!=")
    elif voroudi == dastour_bozorgtar:
        moghayeseh(">")
    elif voroudi == dastour_koochaktar:
        moghayeseh("<")
    elif voroudi == dastour_bozorgtar_mosavi:
        moghayeseh(">=")
    elif voroudi == dastour_koochaktar_mosavi:
        moghayeseh("<=")
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
