import matplotlib.pyplot as plt
from cloud import Cloud
from collections import Counter

class Graph:
    def __init__(self, stop_file, comments_file, output):
        self.stop_file = stop_file
        self.comments_file = comments_file
        self.output = output

    def generate_graph(self, title, count=10):
        print("Generating graph...")
        my_cloud = Cloud(self.stop_file, self.comments_file)

        words = my_cloud.select_word()
        word_count = Counter(words)

        top_words = dict(word_count.most_common(count))

        word_keys = list(top_words.keys())
        word_values = list(top_words.values())

        plt.rcParams["font.family"] = ["SimHei"]
        plt.title(title)
        plt.bar(range(len(top_words)), word_values, tick_label=word_keys)

        # Adding word labels on top of each bar
        for index, value in enumerate(word_values):
            plt.text(index, value + 5, str(value), ha='center', va='bottom', fontweight='bold')

        plt.savefig(self.output)

        return("Generated graph.")















