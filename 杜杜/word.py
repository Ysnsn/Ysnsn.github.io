from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba

# 分词
def trans_CN(text):
    # 接收分词的字符串
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result

# 要读取的txt文本
with open("love.txt", encoding="utf-8") as fp:
    text = fp.read()
    # print(text)
    # 将读取的中文文档进行分词
    text = trans_CN(text)
    mask = np.array(image.open("love.png"))     #添加心形图片
    wordcloud = WordCloud(
        # 添加遮罩层
        mask=mask,
        # 生成中文字的字体,必须要加,不然看不到中文
        font_path="C:\Windows\Fonts\STXINGKA.TTF"
    ).generate(text)
    image_produce = wordcloud.to_image()
    image_produce.show()