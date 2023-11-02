import torch
import re
import transformers
from textblob import TextBlob
Model, Tokenizer, Model_Checkpoints= None, None, None

"""
  Note that the model we made summarize the text into short text. for example it can summarize 2 papers of text into only one or two
   sentences. But since some people would like the summarization to be a bit larger we have devoloped a function (called long_summarization) 
   that does this, by slicing or spliting the original text, then apply the model on each split, then finally concatinating the results.

"""

def split_text(sentence):
  splits = sentence.split(".")
  splits = [''.join(splits[i:i+2]) for i in range(0, len(splits), 2)] # combine each two sentences together in one sentence
  return splits

def prepare_text(text):
  result = re.sub(r'</s>', '', text)
  result = re.sub(r'<s>', '', result)
  result = re.sub(r'</pad>', '', result)
  result = re.sub(r'<pad>', '', result)
  return result

def english_summarization(text, max_input = 512, max_target = 128):
    model = transformers.AutoModelForSeq2SeqLM.from_pretrained('./static/assets/models/summarization') if Model is None else Model
    model_checkpoints = 'facebook/bart-large-xsum' if Model_Checkpoints is None else Model_Checkpoints
    tokenizer = transformers.AutoTokenizer.from_pretrained(model_checkpoints) if Tokenizer is None else Tokenizer

    model_inputs = tokenizer(text,  max_length=max_input, padding='max_length', truncation=True)
    raw_pred = model.generate(torch.LongTensor([model_inputs["input_ids"]]))
    summarized = tokenizer.decode(raw_pred.numpy()[0])
    result = prepare_text(summarized)
    return result

def long_summarization(text):
  summzarization_chunks=[]
  splits = split_text(text)
  for split in splits:
    txt = english_summarization(split)
    summzarization_chunks.append(txt)
  final_summarization = ' '.join(summzarization_chunks)
  return final_summarization

def arabic_summarization(english_summarizated_text):
  translator = TextBlob(english_summarizated_text)
  res=translator.translate(from_lang='en', to='ar')
  return str(res)
