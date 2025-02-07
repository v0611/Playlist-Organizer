from models import Playlist


def view_all_playlists():
    print('>>>>> View All Current Playlists <<<<<\n')
    playlists = Playlist.get_all()

    if playlists:
        for p in playlists:
            print(p['name'])

        choice = input("\nType the name of a playlist to delete it, or press ENTER to return: ").strip()
        if choice:
            confirm = input(
                f"Are you sure you want to delete '{choice}'? This action cannot be undone. (Y/N): ").strip().upper()
            if confirm == 'Y' and Playlist.delete_playlist(choice):
                print(f"Playlist '{choice}' deleted successfully.\n")
            else:
                print("Deletion canceled or playlist not found.\n")
    else:
        print("No playlists available.")

    print("--- END OF LIST ---\n")
    back_to_menu_or_help()


def create_a_playlist():
    name = input("Enter playlist name: ").strip()
    if name:
        playlist = Playlist(name)
        playlist.save()
        print(f"\nPlaylist '{name}' created successfully!\n")
    else:
        print("\nPlaylist name cannot be empty.\n")
    back_to_menu_or_help()


def delete_playlist():
    name = input("Enter the name of the playlist to delete: ").strip()
    if name:
        confirm = input(
            f"Are you sure you want to delete '{name}'? This action cannot be undone. (Y/N): ").strip().upper()
        if confirm == 'Y' and Playlist.delete_playlist(name):
            print(f"Playlist '{name}' deleted successfully.\n")
        else:
            print(f"Playlist '{name}' not found or deletion canceled.\n")
    else:
        print("\nPlaylist name cannot be empty.\n")

    back_to_menu_or_help()


def display_help():
    print("\n>>>>> HELP MENU <<<<<\n")
    print("Welcome to the Digital Playlist Organizer!")
    print("This application helps you organize your music collection into playlists.")
    print("\n**MAIN MENU OPTIONS:**")
    print("1 - View all playlists: Display a list of all available playlists.")
    print("2 - Create a playlist: Enter a name to create a new playlist.")
    print("3 - Delete a playlist: Remove a playlist PERMANENTLY (CONFIRMATION REQUIRED).")
    print("\n**NAVIGATION & SHORTCUTS:**")
    print("B - Return to the Main Menu.")
    print("H - Open this Help Menu anytime.")
    print("\n**IMPORTANT NOTES:**")
    print("- Deleting a playlist is **PERMANENT** and cannot be undone.")
    print("- The Help Menu is **always accessible** by pressing 'H' on any screen.")
    print("- If you encounter issues, return to the Main Menu and retry the action.")
    print("\n--- END OF HELP MENU ---\n")
    back_to_menu_or_help()


def back_to_menu_or_help():
    while True:
        user_input = input('B - Back to Main Menu\nH - Help Info\n').strip().upper()
        if user_input == 'B':
            display_menu()
            handle_user_input()
            break
        elif user_input == 'H':
            display_help()
            break
        else:
            print("Invalid Input. Please try again.")


menu = {
    1: {"name": "View all playlists", "action": view_all_playlists},
    2: {"name": "Create a playlist", "action": create_a_playlist},
    3: {"name": "Delete a playlist", "action": delete_playlist},
    'H': {"name": "Helpful Info", "action": display_help}
}


def display_menu():
    print('--------------->>>>>DIGITAL PLAYLIST MAIN MENU<<<<<-----------')
    print('Effortlessly Organize Your Music – Create, Manage, and Enjoy Your Playlists with Ease!\n')
    print("Select an option:")
    for key, item in menu.items():
        print(f"{key} - {item['name']}")
    print("X - Exit")


def handle_user_input():
    while True:
        user_input = input("Select an option: ").strip().upper()

        if user_input == 'X':
            print("Exiting program...")
            break
        elif user_input in menu:
            menu[user_input]["action"]()
        else:
            try:
                option = int(user_input)
                if option in menu:
                    menu[option]["action"]()
                else:
                    print("Invalid option, please try again.")
            except ValueError:
                print("Invalid input, please try again.")


if __name__ == "__main__":
    display_menu()
    handle_user_input()
