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

def add_member(names, ranks, divisions, id):
      new_name = input("enter name:")
      new_rank = input("enter rank:")
      new_divisions = input ("enter divison:")
      new_id =input("enter new Id number:")

      names.append(new_name)
      ranks.append(new_rank)
      divisions.append(new_divisions)
      id.append(new_id)
      
      print(f"{new_name} has been added to the database")

      return names, ranks, divisions, id

def main():
      n, r, d, i = init_database()
      user = input("provide your Full Name")
      while True:
            choice =display_menu(user)

            if choice == "1":
                  display_roster(n, r, d, i)
            elif choice == "2":
                n, r, d, i = add_member(n, r, d, i)

            if choice == "9":
                print("Goodbye, captain")
            break
def display_roster(names, ranks, divisions, id):
      print("DISPLAYING ROSTER")
      for n, r, d, i in zip(names, ranks, divisions, id):
            print(f"id: {i} | name: {n} | rank: {r} | divisions: {d}")

main()

