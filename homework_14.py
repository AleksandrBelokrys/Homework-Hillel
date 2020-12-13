import asyncio
import aiohttp
import json


async def request_data(url):

    async with aiohttp.request('get', url) as response:
        return await response.json()


async def get_reddit_top(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5"
    result = await request_data(url)

    data = dict()

    for post in result['data']['children']:

        title = post['data']['title']
        score = post['data']['score']
        link = post['data']['url']

        post_dict = {
            title: {
                score: 'int',
                link: 'str'
            }
        }

        data.update(post_dict)

    # print(json.dumps({f'{subreddit}': data}, indent=4))

    return {f'{subreddit}': data}


async def main():

    reddits = {
        "python",
        "compsci",
        "microbork"
    }

    requests = await asyncio.gather(*[get_reddit_top(reddit) for reddit in reddits])

    data = dict()
    for req in requests:
        data.update(req)

    with open('parser.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

asyncio.run(main())
