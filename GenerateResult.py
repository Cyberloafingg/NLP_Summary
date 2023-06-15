import tqdm
import pandas as pd
from paddlenlp.transformers import PegasusForConditionalGeneration, PegasusChineseTokenizer

MAX_CONTENT_LENGTH = 512
MAX_ABSTRACT_LENGTH = 160
MIN_ABSTRACT_LENGTH = 0
NUM_BEAM = 4
def infer(text, model, tokenizer):
    tokenized = tokenizer(text,
                          truncation=True,
                          max_length=MAX_CONTENT_LENGTH,
                          return_tensors='pd')
    preds, _ = model.generate(input_ids=tokenized['input_ids'],
                              max_length=MAX_ABSTRACT_LENGTH,
                              min_length=MIN_ABSTRACT_LENGTH,
                              decode_strategy='beam_search', # 采用beam_search搜索
                              num_beams=NUM_BEAM)
    return(tokenizer.decode(preds[0], skip_special_tokens=True, clean_up_tokenization_spaces=False))
def read_test_data(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        next(f)
        for line in f:
            lines.append({"id":line.split("|")[0].strip(),"content":line.split("|")[1].strip()})
    return lines
def generate_result(test_file):
    model = PegasusForConditionalGeneration.from_pretrained('checkpoints')
    model.eval()
    tokenizer = PegasusChineseTokenizer.from_pretrained('checkpoints')
    result_data=pd.DataFrame()
    # 测试一个句子的推理
    infer("今天天气不错", model, tokenizer)
    idx = 0
    test_lines=read_test_data(test_file)
    for line in tqdm(test_lines, total=len(test_lines), desc="Infer:") :
        idx +=1
        test_id,content=line['id'],line['content']
        ret=infer(content, model, tokenizer)
        result={"id":test_id, "ret":ret}
        result_data=result_data._append(result,ignore_index=True)
    result_data.to_csv('result.csv',  index=False,encoding='utf-8',sep ='|',header =['id','ret'])

if __name__ == '__main__':
    test_file = 'processed/test_data.csv'
    generate_result(test_file)

