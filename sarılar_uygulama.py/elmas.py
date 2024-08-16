import datetime

def main_menu():
    print("***** YAŞ HESAPLAMA PROGRAMI *****")
    print("1. Kaç yaşındayım?")
    print("2. Kaç aydır yaşıyorum?")
    print("3. Kaç gündür yaşıyorum?")
    print("4. Kaç saattir yaşıyorum?")
    print("5. Çıkış")
    print()

def yas_hesaplama(dogum_tarihi):
    bugun = datetime.date.today()
    age = bugun.year - dogum_tarihi.year - ((bugun.month, bugun.day) < (dogum_tarihi.month, dogum_tarihi.day))
    return age

def calculate_months_lived(birth_date):
    today = datetime.date.today()
    months = (today.year - birth_date.year) * 12 + today.month - birth_date.month
    return months

def calculate_days_lived(birth_date):
    today = datetime.date.today()
    days_lived = (today - birth_date).days
    return days_lived

def calculate_hours_lived(birth_date):
    now = datetime.datetime.now()
    birth_datetime = datetime.datetime.combine(birth_date, datetime.time())
    hours_lived = (now - birth_datetime).total_seconds() / 3600
    return hours_lived

def get_birth_date():
    while True:
        try:
            year = int(input("Doğum yılınızı girin (örn. 1990): "))
            month = int(input("Doğum ayınızı girin (1-12 arası): "))
            day = int(input("Doğum gününüzü girin (1-31 arası): "))
            birth_date = datetime.date(year, month, day)
            break
        except ValueError:
            print("Geçersiz tarih, lütfen tekrar girin.")
    return birth_date

def main():
    while True:
        main_menu()
        choice = input("Seçiminizi yapın (1-5): ")

        if choice == '1':
            birth_date = get_birth_date()
            age = calculate_age(birth_date)
            print(f"Yaşınız: {age} yaşında")

        elif choice == '2':
            birth_date = get_birth_date()
            months_lived = calculate_months_lived(birth_date)
            print(f"Kaç aydır yaşıyorsunuz: {months_lived} ay")

        elif choice == '3':
            birth_date = get_birth_date()
            days_lived = calculate_days_lived(birth_date)
            print(f"Kaç gündür yaşıyorsunuz: {days_lived} gün")

        elif choice == '4':
            birth_date = get_birth_date()
            hours_lived = calculate_hours_lived(birth_date)
            print(f"Kaç saattir yaşıyorsunuz: {hours_lived:.2f} saat")

        elif choice == '5':
            print("Programdan çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()
