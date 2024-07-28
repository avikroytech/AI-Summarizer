from newspaper import Article

def get_main_content(url):
    article = Article(url)
    
    # Download and parse the article
    article.download()
    article.parse()
    
    # Get the main text content
    main_content = article.text
    
    return main_content

# Example usage
# url = 'https://www.nytimes.com/2024/01/19/business/stock-market-record.html'
# main_content = get_main_content(url)
# print(main_content)