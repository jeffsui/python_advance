import requests
from bs4 import BeautifulSoup
import os
import time

# 获取网页内容
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return response.text

# 获取分页内的书籍链接
def get_books_from_page(page_url):
    books = []
    html = get_html(page_url)
    soup = BeautifulSoup(html, 'html.parser')

    # 找到书籍的链接
    for book in soup.select('div.book-mid-info h4 a'):
        book_url = 'https:' + book['href']
        books.append(book_url)

    return books

# 获取书籍的所有章节链接
def get_chapter_links(book_url):
    chapters = []
    html = get_html(book_url)
    soup = BeautifulSoup(html, 'html.parser')

    # 找到目录页
    chapter_list_url = 'https:' + soup.select_one('a#j-catalogWrap')['href']
    html = get_html(chapter_list_url)
    soup = BeautifulSoup(html, 'html.parser')

    # 获取章节链接
    for chapter in soup.select('ul.cf li a'):
        chapter_url = 'https:' + chapter['href']
        chapters.append(chapter_url)

    return chapters

# 获取章节内容
def get_chapter_content(chapter_url):
    html = get_html(chapter_url)
    soup = BeautifulSoup(html, 'html.parser')

    # 获取章节标题
    title = soup.select_one('h3.j_chapterName').get_text()

    # 获取章节内容
    content = soup.select_one('div.read-content').get_text(separator='\n')

    return title, content

# 保存书籍到txt文件
def save_to_txt(book_title, chapters):
    filename = f'{book_title}.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        for title, content in chapters:
            f.write(f'{title}\n\n{content}\n\n')
    print(f'书籍 {book_title} 已保存到 {filename}')

# 主函数
def main():
    base_url = 'https://www.qidian.com/all?page='

    # 设置你要爬取的页数范围
    start_page = 1
    end_page = 5

    for page in range(start_page, end_page + 1):
        page_url = base_url + str(page)
        books = get_books_from_page(page_url)

        for book_url in books:
            # 获取书籍的章节链接
            chapter_links = get_chapter_links(book_url)

            book_title = book_url.split('/')[-1]  # 书籍名称
            chapters = []

            # 获取每个章节的内容
            for chapter_url in chapter_links:
                title, content = get_chapter_content(chapter_url)
                chapters.append((title, content))

                # 防止请求频繁被封
                time.sleep(2)

            # 保存书籍内容到txt
            save_to_txt(book_title, chapters)

if __name__ == '__main__':
    main()
