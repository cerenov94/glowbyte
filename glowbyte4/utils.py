import re
from tqdm import tqdm
import numpy as np


def split_merged_words(s):
    words = s.split(' ')
    r = []
    for word in words:
        for w in range(1,len(word)):
            if word[w-1].islower() and word[w].isupper():
                word =(' '.join([word[:w],word[w:]]))
        r.append(word)
    return " ".join(r)        



def split_merged_words_with_digits(s):
    r = []
    words = s.split(' ')
    for word in words:
        for w in range(1,len(word)):
            if word[w-1].isdigit() and word[w].isalpha():
                word = (' '.join([word[:w],word[w:]]))
                
            if word[w-1].isalpha() and word[w].isdigit():
                word = (' '.join([word[:w],word[w:]]))
        r.append(word)
    return " ".join(r)



def remove_repeated_symbols(text):

    result = []
    
    for x in text:
        if not result or result[-1] != x:
            result.append(x)
    
    return ''.join(result)


def remove_digits(text):
    r = []
    words = text.split(' ')
    for word in words:
        try:
            digit = round(float(word.replace(',','.')))
            word = str(digit)
            if digit > 10.:
                word = ''
        except:
            pass
        r.append(word)
    return " ".join(r)



def preprocess_text(text):
    text = split_merged_words(text)
    text = split_merged_words_with_digits(text)
    text = remove_digits(text)
    text = text.lower()
    text = re.sub('(\s[а-я]+/10)','/10',text)
    text = text.replace('\u200e','')
    text = text.replace('7-8 из 10','8/10')
    text = text.replace('1-2 из 10','2/10')
    text = text.replace('2-3 из 10','3/10')
    text = text.replace('3-4 из 10','4/10')
    text = text.replace('4-5 из 10','5/10')
    text = text.replace('6-7 из 10','7/10')
    text = text.replace('8-9 из 10','9/10')
    text = text.replace('9-10 из 10','10/10')
    text = text.replace('7-8/10','8/10')
    text = text.replace('1-2/10','2/10')
    text = text.replace('2-3/10','3/10')
    text = text.replace('3-4/10','4/10')
    text = text.replace('4-5/10','5/10')
    text = text.replace('6-7/10','7/10')
    text = text.replace('8-9/10','9/10')
    text = text.replace('9-10/10','10/10')
    text = text.replace('пойдет7.5/10','пойдет 8/10')
    text = re.sub('(10-[а-я]+)','10/10',text)
    text = text.replace('плохоединственный','плохо единственный')
    text = text.replace('\xa0','')
    text = text.replace('\u200b','')
    text = text.replace('\t','')
    text = text.replace('xd','хаха')
    text = text.replace('отлтчно','отлично')
    text = text.replace('гг','главный герой')
    text = text.replace('шыдевор','шедевр')
    text = text.replace('спасяб','спасибо')
    text = text.replace('дефолтнейшная','обычная')
    text = text.replace('коментари','комментарии')
    text = text.replace('масовый','массовый')
    text = text.replace('объяктивная','объективная')
    text = text.replace('абезяну','обезьяну')
    text = text.replace('абалденое','обалденное')
    text = text.replace('абаснуев','обосновать')
    text = text.replace('абаснуи','обосновать')
    text = text.replace('абгрейда','апгрейд')
    text = text.replace('абреаиатурой','аббревиатура')
    text = text.replace('адахнуть','отдохнуть')
    text = text.replace('афтор','автор')
    text = text.replace('аніме','аниме')
    text = text.replace('анїмє','аниме')
    text = text.replace('омниме','аниме')
    text = text.replace('анимцо','аниме')
    text = text.replace('єто','это')
    text = text.replace('есчо','если что')
    text = text.replace('1\\10','1/10')
    text = text.replace('2\\10','2/10')
    text = text.replace('3\\10','3/10')
    text = text.replace('4\\10','4/10')
    text = text.replace('5\\10','5/10')
    text = text.replace('6\\10','6/10')
    text = text.replace('7\\10','7/10')
    text = text.replace('8\\10','8/10')
    text = text.replace('9\\10','9/10')
    text = text.replace('10\\10','10/10')
    text = text.replace('№',' номер ')
    text = text.replace('86\'ые','')
    text = text.replace('[=спойлер]','')
    text = text.replace('[/]','')
    text = text.replace(']','')
    text = text.replace('[','')
    text = text.replace(')','')
    text = text.replace('(','')
    text = text.replace('~','')
    text = text.replace('\\','/')
    text = text.replace('"','')
    text = text.replace("'",'')
    text = text.replace('\n','')
    text = text.replace('³','')
    text = text.replace('⁹','')

    text = remove_repeated_symbols(text)

    text = re.sub(r'https?://(www\.)?(\w+)(\.\w+)(/\w*)?',"", text)
    text = re.sub(r'<.*?>',"", text)
    text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+',"", text)
    text = re.sub(r'(\d+x\d+)',"",text)
    text = re.sub(r'(x\d+)','',text)
    text = re.sub(r'(\d\d\d\d+)','',text)
    text = re.sub(r'(аням[а-я]+)','аниме',text)
    text = re.sub(r'(лубо[а-я]+)','любовь',text)
    text = re.sub(r'(ао){2,}','',text)
    text = re.sub(r'(дэвуш)','девуш',text)
    text = re.sub(r'(тут[а-я]+)','тут',text)
    text = re.sub(r'(ют[а-я]б[а-я]+)','ютуб',text)
    text = re.sub(r'(_{1,})','',text)
    text = re.sub(r'(\d\d-[а-я])','',text)
    text = re.sub(r'(\d{1,}%)','',text)
    text = re.sub(r'(\d{1,}-[а-я]+)','',text)
    text = re.sub(r'(\d+-\d+)','',text)
    text = re.sub(r'(\d{3,})','',text)
    text = re.sub(r'([«»|])','',text)
    text = re.sub(r'(-{2,})','',text)
    emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F" 
                            u"\U0001F300-\U0001F5FF" 
                            u"\U0001F680-\U0001F6FF"  
                            u"\U0001F1E0-\U0001F1FF" 
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            u"\U0001f926-\U0001f937"
                            u"\U00010000-\U0010ffff"
                            u"\u2640-\u2642" 
                            u"\u2600-\u2B55"
                            u"\u200d"
                            u"\u23cf"
                            u"\u23e9"
                            u"\u231a"
                            u"\ufe0f" 
                            u"\u3030"
                            "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    text = re.sub(r'@\w+',"", text)
    
    text = re.sub('(c[а-я]+)','',text)
    text = re.sub(r'(\d+x\d+)',"",text)
    text = re.sub(r'(x\d+)','',text)
    text = re.sub(r'(\d\d\d\d+)','',text)
    text = re.sub(r'([a-z])','',text)
    return text


def score_extr(df):
    scores = []
    for idx,text in enumerate(tqdm(df['text'])):
        words = text.split(' ')
        r = []
        for w_id,word in enumerate(words):
            
            if '/' in word and word.replace('/','').isdigit():
                numbers = word.split('/')
                try:
                    numbers.remove('')
                except:
                    pass
                s = float(numbers[0])/((float(numbers[-1]) + 1e-6))
                r.append(s)
                
        m = re.search(r'\d{1,2} из 10',text)
        if m:
            value = m.group().split('из')
            numbers = []
            for n in value:
                numbers.append(float(n.strip()))
            s = numbers[0]/(numbers[-1] + 1e-6)
            r.append(s)
        m = re.search(r'(ста[а-я]+\s\d{1,2})',text)
        if m:
            value = m.group().split(' ')
            n = float(value[-1])
            if n <= 10:
                s = n/10.
            r.append(s)
            
        m = re.search(r'(на \d{1,})',text)
        if m:
            value = m.group().split(' ')
            n = float(value[-1])
            if n <= 10:
                s = n/10.
            r.append(s)
        m = re.search(r'(\d{1,2} из-за)',text)
        if m:
            value = m.group().split(' ')
            n = float(value[0])
            if n <= 10:
                s = n/10.
            r.append(s)
            
        m = re.search(r'(ито[а-я]+. \d{1,2} \d{1,2})',text)
        if m:
            value = m.group().split(' ')
            n1 = float(value[-2])
            n2 = float(value[-1])
            s = n1/10.
            r.append(s)
            
        m = re.search(r'(оцен[а-я]+.\d{1,2}/10)',text)
        if m:
            value = m.group()
            value = re.sub(r'(оцен[а-я]+)','',value)
            numbers = value.split('/')
            n1 = re.sub(r'([\.,\?:])','',numbers[0].strip())
            n1 = float(n1)
            s = n1/10.
            r.append(s)
            
        m = re.search(r'(\.\d{1,2}/10)',text)
        if m:
            value = m.group().split('/')
            n1 = float(value[-2].replace('.',''))
            s = n1/10.
            r.append(s)
        m = re.search(r'(\d,\d/10)',text)
        if m:
            value = m.group().split('/')
            n1 = float(value[-2].replace(',','.'))
            s = n1/10.
            r.append(s)
            
        m = re.search(r'(\d{1,2}/10)',text)
        if m:
            value = m.group().split('/')
            n1 = float(value[-2].strip())
            s = n1/10.
            r.append(s)
        mean_score = 0.5 if np.isnan(np.mean(r)) else np.mean(r)
        scores.append(mean_score)
    return scores