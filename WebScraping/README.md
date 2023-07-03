# Web Scraping Job Positions
This Python script demonstrates how to scrape job positions from a website using Selenium and BeautifulSoup. It extracts the URLs of job positions, cleans them, and retrieves details for a sample set of positions.

## Prerequisites
Python 3.x

webdriver_manager library

requests library

bs4 (BeautifulSoup) library

selenium library

pandas library

## Installation
Install the required libraries by running the following command:

pip install webdriver_manager

## Usage
### Import the required libraries:

![image](https://github.com/BrunoDataSci/Web_Scraping/assets/136373623/346e8b64-b14f-4d8f-bafc-f7995faf764f)


## Set the URL of the Vagas.com.br careers page:
![image](https://github.com/BrunoDataSci/Web_Scraping/assets/136373623/784004ae-d39a-4cfe-b0d3-0be6dbe59d31)


## Send a request to the URL and parse the HTML using BeautifulSoup:
reqs = requests.get(url)

soup = BeautifulSoup(reqs.text, 'html.parser')

## Extract the URLs of the job positions from the page:
![image](https://github.com/BrunoDataSci/Web_Scraping/assets/136373623/0c5ef526-6177-4daa-8d98-9717b67b00de)


## Select a sample set of positions to retrieve details:
positions_example = positions[190:200]

## Initialize the Chrome web driver using webdriver_manager:
driver = webdriver.Chrome(ChromeDriverManager().install())

## Scrape the details for each position in the sample set:
![image](https://github.com/BrunoDataSci/Web_Scraping/assets/136373623/dbaa869b-efe5-4201-8175-e4e452a8a95d)


## Create a DataFrame to store the position details:

df = pd.DataFrame(details_positions_examples)

![image](https://github.com/BrunoDataSci/Web_Scraping/assets/136373623/fea2fc38-f4ec-404b-8341-3a5bf5b2b9d5)


## License
This code is licensed under the MIT License.
