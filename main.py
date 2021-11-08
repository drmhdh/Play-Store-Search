import play_scraper


def main():
    query = input('Enter app name :- ')
    results = play_scraper.search(query)
    answers = []
    for result in results:
        details = 'Title: {}'.format(result['title']) + '\n' \
        'Description: {}'.format(result['description']) + '\n' \
        'App ID: {}'.format(result['app_id']) + '\n' \
        'Developer: {}'.format(result['developer']) + '\n' \
        'Developer ID: {}'.format(result['developer_id']) + '\n' \
        'Score: {}'.format(result['score']) + '\n' \
        'Price: {}'.format(result['price']) + '\n' \
        'Full Price: {}'.format(result['full_price']) + '\n' \
        'Free: {}'.format(result['free'])
        answers.append(details)
    for answer in answers:
        print(answer + '\n\n')


main()