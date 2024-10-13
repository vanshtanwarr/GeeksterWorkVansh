import requests
from bs4 import BeautifulSoup
url = 'https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time-in-python'
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
question_title = soup.find('a', class_='question-hyperlink').get_text()
question_body = soup.find('div', class_='s-prose js-post-body').get_text()
answers = soup.find_all('div', class_='answer')
print(f"Question: {question_title}")
print(f"Question Details: {question_body}\n")
for idx, answer in enumerate(answers):
    answer_body = answer.find('div', class_='s-prose js-post-body').get_text()
    print(f"Answer {idx}: {answer_body}\n")
