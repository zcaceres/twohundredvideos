import urllib3
from twohundredvideos.debugging import debug # <--- Uncomment if you want to use "print_results" to see all your search results printed
from bs4 import BeautifulSoup
from twohundredvideos.util import youtube_search_paths

"""
––––––––––––––––– YOUTUBE EMBEDDABLE VIDEO SCRAPER –––––––––––––––
            Queries Youtube based on whatever you want.
            Returns a CSV w/200 embeddable video urls along with
            the user names and user channels for the video.
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
"""


# Captures User Inputs
def get_search_query():
    query = format_query(input("Please type your search query here: "))
    return query


def format_query(query):
    query = str.replace(query, " ", "+") # format string for youtube search results
    return query


# Requests the URL
def make_request(query):
    data_list = []
    # Parses all search pages with strings in youtube_search_paths.py. Add more there if you want.
    query_string = youtube_search_paths.get_search_strings(query)
    http = urllib3.PoolManager()
    for qs in query_string:
        print("Checking link: {0}".format(qs))
        r = http.request('GET', '{0}'.format(qs))
        data_list.append(r.data)
    return data_list


# Parses Youtube Search results page by CSS selector
def parse_html_in_request(requests):
    video_urls = []
    username_list = []
    user_channel_urls = []
    soups = []
    for req in requests:
        soups.append(BeautifulSoup(req, 'html.parser'))
    for soup in soups:
        videos = soup.select(".yt-uix-tile-link")
        for video in videos:
            if video.has_attr('href'):
                video_href = video['href']
                if "doubleclick" in video_href:
                    print("Ignoring Advertisement...")
                else:
                    video_urls.append(video['href'])
        # Get Usernames
        usernames = soup.select(".yt-lockup-byline a")
        for username in usernames:
            if username:
                username_list.append(username.text)
                # Get Channels or Username Pages
                if username.has_attr('href'):
                    user_channel_urls.append(username['href'])
                else:
                    user_channel_urls.append("No Channel URL")
            else:
                username_list.append("None given")
    return video_urls, username_list, user_channel_urls


# Reformats scraped urls to have embeddable links
def reformat_url_for_embed(video_urls):
    embed_links = []
    for url in video_urls:
        url = 'http://www.youtube.com/embed/{0}'.format(url[9:])
        embed_links.append(url)
    return embed_links


# Creates CSV file with video embed url, user that owns it, url to user's channel or profile page
def create_csv_file(links_list, username_list, user_channel_url_list):
    debug.print_results(links_list)
    debug.print_results(username_list)
    debug.print_results(user_channel_url_list)
    counter = 0
    with open('youtube_links.csv', 'w') as fin:
        fin.write("video_url, user_name, user_channel_info, likes\n")
        if len(links_list) <= len(username_list):
            iterate = links_list
        else:
            iterate = username_list
        while counter < len(iterate):
            fin.write("{0}, {1}, {2}, 0\n".format(links_list[counter],
                                                    username_list[counter],
                                                    user_channel_url_list[counter]))
            counter += 1
        else:
            print("FILE CLOSED")
            return fin


def scrape(search_query):
    if search_query:
        query = format_query(search_query)
        final_csv = main_process(query)
        return final_csv


def main_process(query):
    list_of_responses = make_request(query)
    video_urls, username_list, user_channel_urls = parse_html_in_request(list_of_responses)
    embeddable_links = reformat_url_for_embed(video_urls)
    final_csv = create_csv_file(embeddable_links, username_list, user_channel_urls)
    return final_csv


if __name__ == '__main__':
    # Call scrape with nonetype search query so that it prompts user in CLI for a query
    search_query = None
    scrape(search_query)
