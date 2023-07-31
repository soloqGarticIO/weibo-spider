import stylecloud
import pandas as pd
import jieba
import re

class Cloud:
    def __init__(self, stop_file, comment_file):
        self.comment_file = comment_file
        self.stop_file = stop_file

    def select_word(self):
        stopwords = []
        with open(self.stop_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    stopwords.append(line.strip())
        comments = pd.read_csv(self.comment_file, header=None, names=["comment"])
        all_comments_text = "。".join(comments["comment"])
        filter = re.sub(r'\[[^\]]+\]', '', all_comments_text)
        filter = re.sub(r'[^\u4e00-\u9fa5]+', '', filter)
        words = jieba.lcut(filter, cut_all=False)
        word_selected = [word for word in words if word not in stopwords and len(word) >= 1]
        return word_selected
    
    def produce(self, output, shape="fas fa-heart"):
        print("Generating cloud...")
        text = self.select_word()
        try:
            stylecloud.gen_stylecloud(
                text=' '.join(text),
                collocations=False,
                font_path=r'C:\Windows\Fonts\msyh.ttc',
                icon_name=shape,
                size=768,
                output_name=output
            )
            return "Generated cloud."
        except AttributeError:
            return "Attribute Error: Invalid Pillow version."
             



        
