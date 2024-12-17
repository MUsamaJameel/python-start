import json



def load_list():
    try:
        with open('kit.text', 'r') as file:
            test = json.load(file)

            return(test)
    except FileNotFoundError:
        return[]

def save_file(list):
    with open('kit.text', 'w') as file:
        json.dump(list, file)


def kit_list(list):
    print('\n')
    print("*" * 70)

    for index, list_item in enumerate(list, start=1):

        print(f"{index}.Item Name: {list_item['name']}, Quantity: {list_item['quantity']} ")
    print('\n')
    print("*" * 70)

def add_item(list):
    
    name = input('Enter Item Name: ')
    quentity = input('Enter Item Quantity: ')
    list.append({"name":name, "quantity":quentity})
    save_file(list)

def update_item(list):
    kit_list(list)
    index = int(input("Enter Item number to Update: "))
    if 1 <= index <= len(list):
        name = input('Enter new Item Name')
        quantity = input('Enter new Item Quentity')
        list[index-1] = {'name' :name , 'quantity' :quantity}
        save_file(list)

    else:
        print("Invalid Item number selected")

def delete_item(list):
    kit_list(list)
    index = int(input("Enter Item number to delete: "))
    if 1<= index <= len(list):
        del list[index-1]
        save_file(list)

    else:
          
        print("Invalid list Number Selected")
    



def main():
    while True:
        list = load_list()
        print("\n My Kit List")
        print("1. Show my kit list")
        print("2. Add Item in my kit list")
        print("3. Update Item in my kit list")
        print("4. Delete Item from my kit list")
        print("5. Exit my kit list")

        choice = input("Enter your option: ")
        # print(list)


        match choice:
            case '1':
                kit_list(list)
            case '2':
                add_item(list)
            case '3':
                update_item(list)
            case '4':
                delete_item(list)
            case '5':
                break
                
            case _:
                print("Invalid Choice")

        
if __name__ == "__main__" :
    main()
