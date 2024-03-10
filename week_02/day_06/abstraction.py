from abc import ABC, abstractmethod

class BankingApp(ABC):

    def database(self):
        print(f"Connect to database successfully.")

    @abstractmethod
    def security(self):
        pass

    @abstractmethod
    def notification(self):
        pass

class MobileApp(BankingApp):

    def login_app(self):
        print("Login to Mobile App Successfully.")

    def security(self):
        print("Your Mobile is secure.")

    def notification(self):
        print("Login successfull.")


if __name__ == "__main__":
    app = MobileApp()
    app.security()
    app.notification()
