def main():
    anime = {
        "Demon Slayer": {
            "Temporada 1": [
                {
                    "cap": 1,
                    "name": "Crueldad",
                    "duration": "23:39"
                },
                {
                    "cap": 4,
                    "name": "Selección final",
                    "duration": "23:40"
                },
                {
                    "cap": 19,
                    "name": "Dios del fuego",
                    "duration": "23:40"
                },
                {
                    "cap": 25,
                    "name": "Una nueva misión",
                    "duration": "24:10"
                }
            ],
            "Temporada 2": [
                {
                    "cap": 26,
                    "name": "Un sueño profundo",
                    "duration": "22:55"
                },
                {
                    "cap": 43,
                    "name": "¡No me rendiré!",
                    "duration": "23:40"
                }
            ]
        },
        "Spy × Family": {
        
            "Temporada 1":[
                {
                    "cap": 4,
                    "name": "Objetivo: pasar la entrevista",
                    "duration": "24:10"
                },
                {
                    "cap": 7,
                    "name": "El segundo hijo del objetivo",
                    "duration": "24:10"
                }
            ]
        },
        "Attack on Titan": {
            "Temporada 3": [
                {
                    "cap": 46,
                    "name": "La reina de la muralla",
                    "duration": "23:55"
                },
                {
                    "cap": 54,
                    "name": "Héroe",
                    "duration": "23:55"
                }
            ],
            "Temporada 4":[
                {
                    "cap": 60,
                    "name": "Al otro lado del mar",
                    "duration": "23:55"
                },
                {
                    "cap": 72,
                    "name": "Los hijos del bosque",
                    "duration": "23:55"
                }
            ]
        }
    }
    history = []
    while True:
        option_menu = int(input("Please enter a valid option:\n1- Select a serie\n2-Display history\n3-Exit\n->"))
        if option_menu == 1:
            for index,serie in enumerate(anime.keys()):
                print(f"{index+1} - {serie}")

            option_serie = int(input("Please enter a serie to watch:"))
            chapter_selected = None
            if option_serie == 1:
                for season,chapters in anime.get("Demon Slayer").items():
                    print(season)
                    for chapter in chapters:
                        print("Chapter:",chapter.get("cap"))
                chapter_index = int(input("Please enter the chapter that you want to watch\n-->"))
                for season,chapters in anime.get("Demon Slayer").items():
                    for chapter in chapters:
                        if chapter.get("cap") == chapter_index:
                            chapter_selected = chapter
            elif option_serie == 2:
                for season,chapters in anime.get("Spy × Family").items():
                    print(season)
                    for chapter in chapters:
                        print("Chapter:",chapter.get("cap"))
                chapter_index = int(input("Please enter the chapter that you want to watch\n-->"))
                for season,chapters in anime.get("Spy × Family").items():
                    for chapter in chapters:
                        if chapter.get("cap") == chapter_index:
                            chapter_selected = chapter
            elif option_serie == 3:
                for season,chapters in anime.get("Attack on Titan").items():
                    print(season)
                    for chapter in chapters:
                        print("Chapter:",chapter.get("cap"))
                chapter_index = int(input("Please enter the chapter that you want to watch\n-->"))
                for season,chapters in anime.get("Attack on Titan").items():
                    for chapter in chapters:
                        if chapter.get("cap") == chapter_index:
                            chapter_selected = chapter

            print("*** CHAPTER SELECTED ***")
            print("Number:",chapter_selected.get("cap"))
            print("Name:",chapter_selected.get("name"))
            print("Duration:",chapter_selected.get("duration"))
            history.append(chapter_selected)
        elif option_menu == 2:
            print("*** HISTORY ***")
            print(f"You have seen {len(history)} chapters")
            for index,story in enumerate(history):
                print(f"Chapter {index +1}")
                print("Number:",story.get("cap"))
                print("Name:",story.get("name"))
                print("Duration:",story.get("duration"))
        elif option_menu == 3:
            break
        else:
            continue




main()
