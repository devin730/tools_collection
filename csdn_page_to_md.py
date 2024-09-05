# 将一个 CSDN 页面的文章转换成 markdown 文档

import requests
from bs4 import BeautifulSoup
import html2text
import os


def convert_to_markdown(url: str, save_dir: str) -> bool:
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    title_tag = soup.find("h1")  # 标题

    if title_tag is None:
        print("title could not be found, please check.")
        return False
    else:
        title = title_tag.text

    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

    file_name = f"{title}.md"
    markdown_file_path = os.path.join(save_dir, file_name)

    print(f"title: {title}")

    content_div = soup.find(
        "div", class_="article_content clearfix"
    )  # 修改为正确的类名

    if content_div is None:
        print("content could not be found, please check again.")
        return False
    else:
        markdown_content = html2text.html2text(str(content_div))
        markdown_output = f"# {title}\n\n{markdown_content}"

        with open(markdown_file_path, "w", encoding="utf-8") as f:
            f.write(markdown_output)

        print(f"markdown file is saved in {markdown_file_path}")
        return True


if __name__ == "__main__":
    URL = "https://blog.csdn.net/u011250186/article/details/141934381"  # 设置目标URL
    SAVE_PATH = "./"
    convert_to_markdown(URL, SAVE_PATH)
