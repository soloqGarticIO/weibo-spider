from spider import Spider
from cloud import Cloud
from graph import Graph



if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
    url = 'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4927756368879175&is_show_bulletin=3&is_mix=0&count=50&uid=5350509769&fetch_level=0&locale=en-GB&max_id='
    csv_file = "comments.csv"
    stop_file = "cn_stopwords.txt"
    cloud_img = "output.png"
    graph_title = "热门词汇"
    graph_file = "graph.png"

    my_spider = Spider(headers, url, csv_file)
    print(my_spider.crawl(50))
    # comments = pd.read_csv(outpath)
    
    my_cloud = Cloud(stop_file, csv_file)
    print(my_cloud.produce(cloud_img))

    my_graph = Graph(stop_file, csv_file, graph_file)
    print(my_graph.generate_graph(graph_title))


