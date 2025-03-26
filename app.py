def convert_time():
    print("Laika pārveidotājs")
    choice = input("Ievadi, ko vēlies pārveidot (sekundes uz minūtēm, minūtes uz stundām): ").lower()
    
    if "sekundes" in choice:
        seconds = int(input("Ievadi sekundes: "))
        minutes = seconds / 60
        print(f"{seconds} sekundes ir aptuveni {minutes:.2f} minūtes.")
    elif "minūtes" in choice:
        minutes = int(input("Ievadi minūtes: "))
        hours = minutes / 60
        print(f"{minutes} minūtes ir aptuveni {hours:.2f} stundas.")
    else:
        print("Nezināma opcija. Lūdzu mēģini vēlreiz.")
        
convert_time()