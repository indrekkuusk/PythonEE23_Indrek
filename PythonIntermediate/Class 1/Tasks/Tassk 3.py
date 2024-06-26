import requests
import csv


def fetch_all_people():
    base_url = "https://swapi.dev/api/people/"
    all_people = []

    while base_url:
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            all_people.extend(data['results'])
            base_url = data['next']  # Get the URL for the next page
        else:
            print("Error fetching data:", response.status_code)
            return None

    return all_people


def write_to_csv(people):
    if not people:
        print("No data to write.")
        return

    with open('swapi_people.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = list(people[0].keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(people)
    print("Data written to swapi_people.csv")


if __name__ == "__main__":
    all_people = fetch_all_people()
    if all_people:
        write_to_csv(all_people)

print(all_people)        