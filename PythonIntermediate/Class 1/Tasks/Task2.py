import requests
import csv

def fetch_all_people():
    base_url = "https://swapi.dev/api/people"
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


def get_film_title(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['title']
    else:
        return "Unknown"


def get_vehicle_name(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['name']
    else:
        return "Unknown"


def process_people_data(people):
    for person in people:
        # Replace film URLs with film titles
        films = person['films']
        person['films'] = [get_film_title(film_url) for film_url in films]

        # Replace vehicle URLs with vehicle names
        vehicles = person['vehicles']
        person['vehicles'] = [get_vehicle_name(vehicle_url) for vehicle_url in vehicles]

    return people


def write_to_csv(people):
    if not people:
        print("No data to write.")
        return

    with open('../swapi_people.csv', mode='w', newline='') as file:
        fieldnames = people[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(people)
    print("Data written to swapi_people.csv")


if __name__ == "__main__":
    all_people = fetch_all_people()
    if all_people:
        processed_people = process_people_data(all_people)
        write_to_csv(processed_people)
