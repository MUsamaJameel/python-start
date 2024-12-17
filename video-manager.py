
import json


def load_data():
    try:
        with open('youtube.text', 'r') as file:
            test = json.load(file)
            # print(type(test))
            return(test)
    except FileNotFoundError:
            return[]

def save_data_helper(videos):
    with open('youtube.text', 'w') as file:
        json.dump(videos, file)
    

def list_all_videos(videos):
    print('\n')
    print("*" * 70)
    
    for index, video in enumerate(videos, start=1):
       
        print(f"{index}.{video['name']}, Duration:{video['time']}")
    print('\n')
    print("*" * 70)

def add_video(videos):
    name = input('Enter Video Name: ')
    time = input('Enter Video Time: ')
    videos.append({"name": name , "time": time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Input video number to Update: "))
    if  1 <= index <= len(videos):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        videos[index-1] = {'name' :name, 'time' :time}
        save_data_helper(videos)
    else:
        print("Invalid Video number selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video number selected")



def main():
    videos = load_data()

    while True:
        print("\n Youtube Video Manager | Choose your option")
        print("1. List My videos.")
        print("2. Add the video.")
        print("3. Update the video.")
        print("4. Delete the video.")
        print("5. Exit the app.")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice | Choose from the given options")

if __name__ == "__main__":
    main()
