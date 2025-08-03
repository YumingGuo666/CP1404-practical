
import wikipedia


def main():
    print("Welcome to the Wikipedia viewer!")
    while True:
        user_input = input("Enter page title: ").strip()
        if user_input == "":
            print("Thank you.")
            break

        try:
            page = wikipedia.page(user_input)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print('Page id "{}" does not match any pages. Try another id!'.format(user_input))
        except Exception as e:
            print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()



