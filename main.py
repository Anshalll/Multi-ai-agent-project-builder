from src.Developeragent import Developeragent
from src.Tester import tester


if __name__ == "__main__":
    def runagent():
        while True:
            user_prompt = str(input("Enter what to do! "))
            if user_prompt == "q":
                break

            Developeragent.generate_code(user_prompt)
            tester.checkCode(Developeragent.code)

    runagent()
  