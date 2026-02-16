def init_database():
    names = ["picard", "spock", "data", "kirk", "worf"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "ensign"]
    divisions = ["Command", "Command", "Operations", "Security", "research"]
    id = ["1234" , "5678", "9101112", "13141516", "17181920"]

    return names, ranks, divisions, id

def display_menu(Full_Name):
        print("fleet manager menu")
        print(f"currently logged in: {Full_Name}")
        print("1.display roster")
        print("2. add member")
        print("3.remove member")
        print("4.update rank")
        print("5.search crew")
        print("6.filter by division")
        print("7.calculate payroll")
        print("8.count officers")
        print("9.exit")
        choice = input ("select option:")
        return choice

def main():
      n, r, d, i = init_database()
      user = input("provide your Full Name")
      while True:
            choice =display_menu(user)

            if choice == "9":
                print("Goodbye, captain")
            break