class Phone():
    def __init__(self, phone_number):
        self.number = phone_number

    def call(self, other_number):
        print("Calling {} from {}".format(other_number, self.number))
        # print(f"Calling {other_number} from {self.number}")

    def text(self, other_number, msg):
        print("Sending text to {} from {}".format(other_number, self.number))
        print(msg)

    def open_app(self, app_name):
        print("Opening {} on device".format(app_name))

class IPhone(Phone):
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.fingerprint = None

    def set_fingerprint(self, new_fingerprint):
        self.fingerprint = new_fingerprint
    
    def unlock(self, fingerprint=None):
        if (fingerprint == None and self.fingerprint == None):
            print("Phone is unlocked because no fingerprint is currently set")

        if (fingerprint == self.fingerprint):
            print("Phone is unlocked")
        else:
            print("Phone locked. Fingerprint does not match")

martin_iphone = IPhone(8889990000)
print("Martin's number is {}".format(martin_iphone.number))

martin_iphone.set_fingerprint("password")

print(martin_iphone.fingerprint)

martin_iphone.unlock("password123")
martin_iphone.call(8596990933)
martin_iphone.open_app("Tik Tok")

class Android(Phone):
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.keyboard = "Default"
    
    def __str__(self):
        return "This phone is owned by {}".format(self.number)

    
    def set_keyboard(self, new_keyboard):
        self.keyboard = new_keyboard

Android.ORIGIN = Android("")

josh_phone = Android(5557130099)

josh_phone.set_keyboard("Dvorak")
josh_phone.call(8596990933)

josh_phone.open_app("Google Play Store")

print(josh_phone)

# rome_android = Android(8596990933)

# rome_android.set_fingerprint("password")
# print(rome_android.fingerprint)

# rome_android.call(911)

# # make one class 
# # make another class with no relation to the first class
# # try passing in both to a class and see if you have access to methods and variables