import os
import pickle
import csv
from datetime import datetime
import numpy as np
from collections import Counter

base_path = '/Users/lauragraesser/Documents/NYU_Courses/medical_data'
from sklearn.feature_extraction import stop_words
import re
import random

import time
import sklearn
import pprint
from data_util import *

global_time = None
def gettime():
    global global_time
    if global_time is None:
        global_time = time.time()
        diff = 0
    else:
        diff = (time.time()-global_time)/60.0
        global_time = time.time()
    return diff

from nltk.tokenize import word_tokenize
def clean_str_no_stopwords(s, stopwords=stop_words.ENGLISH_STOP_WORDS):
    #s = re.sub('\[\*\*.*\*\*\]|\\n|\s+|[^\w\s]', ' ', s).replace('  ', ' ').lower()#.split()
    s = re.sub('\[\*\*.*\*\*\]|\\n|\s+', ' ', s).replace('  ', ' ').lower()#.split()
    if stopwords is not None:
        s = [w  for w in word_tokenize(s) if (w not in stopwords and not w.isdigit())]
    else:
        s = [w for w in word_tokenize(s)]
    return s

def read_fork(data, op_queue):
    rawdata = []
    for key in data:
        if 'notes' in data[key]:
            data[key]['notes'] = sorted(data[key]['notes'], key=lambda x:datetime.strptime(x['date'], '%Y-%m-%d'))
            for n, note in enumerate(data[key]['notes']):
                data[key]['notes'][n]['note'] = clean_str_no_stopwords(note['note'], None)

            rawdata.append(data[key])
    op_queue.put(rawdata)

def read_data_dump(data_path):
    with open(data_path, 'rb') as f:
        data = pickle.load(f)
    data = {k:data[k] for k in list(data.keys())[:10000]}
    import multiprocessing
    num_workers = 10
    output = multiprocessing.Queue()
    batch_size = len(data.keys()) // num_workers
    processes = []
    for _ in range(num_workers):
        st_ind = _*batch_size
        end_ind = st_ind+batch_size
        if _ == num_workers-1 and end_ind < len(data.keys()):
            end_ind = len(data.keys())
        batch_data = {idx: data[idx] for idx in list(data.keys())[st_ind:end_ind]}
        print(len(batch_data.keys()))
        processes.append(multiprocessing.Process(target=read_fork, args=(
                                            batch_data,  output)))
    for p in processes:
        p.start()
    rawdata = []
    results = [output.get() for p in processes]
    for result in results:
        rawdata.extend(result)

    return rawdata

def read_embeddings(vecidx_path, vec_path):
    words = []
    with open(vecidx_path, 'r') as f:
        tsvreader = csv.reader(f, delimiter='\t')
        for i,row in enumerate(tsvreader):
            words.append(row[0])

    vecs = np.ndarray((len(words), 400))
    with open(vec_path, 'r') as f:
        tsvreader = csv.reader(f, delimiter='\t')
        for i,row in enumerate(tsvreader):
            vecs[i,:] = row[:400]
    vecs = sklearn.preprocessing.normalize(vecs)
    word2vec = {_:vecs[i,:].reshape(-1) for i,_ in enumerate(words)}
    return word2vec

def filter_labels(data, num_labels):
    labels = [key['labels']['icd'][0] for key in data]
    labels = [_[0] for _ in list(Counter(labels).most_common(num_labels))]
    return labels

def filter_data_by_labels(data, labels):
    return [key for key in data if key['labels']['icd'][0] in labels]

def get_vocab(data):
    vocab = []
    for key in data:
        for note in key['notes']:
            if isinstance(note, dict):
                vocab.extend(note['note'])
            else:
                vocab.extend(note)
    # print(vocab[:200])
    vocab = [_[0] for _ in list(Counter(vocab).most_common(1000))]
    return vocab

def filter_data_by_vocab(data, vocab):
    for _,key in enumerate(data):
        for i, note in enumerate(key['notes']):
            if isinstance(key['notes'][i], dict):
                data[_]['notes'][i]['note'] = " ".join([word for word in key['notes'][i]['note'] if word in vocab])
            else:
                data[_]['notes'][i]['note'] = " ".join([word if word in vocab else 'unknown' for word in key['notes'][i]['note']])
    return data

def count_unk(data):
    num_toks = 0
    num_unks = 0
    for _,key in enumerate(data):
        for i, note in enumerate(key['notes']):
            num_toks += sum([1 for word in key['notes'][i]['note']])
            num_unks += sum([1 for word in key['notes'][i]['note'] if word is 'unknown'])
    prop_unks = (num_unks * 1.) / (num_toks * 1.) * 100
    print("{} tokens, {} unks, {:.2f}% unks".format(num_toks, num_unks, prop_unks))

def filter_embeddings(vocab):
    pretrained = read_embeddings(os.path.join(base_path, 'ri-3gram-400-tsv/vocab.tsv'),
                                         os.path.join(base_path, 'ri-3gram-400-tsv/vectors.tsv'))
    csvf = open(os.path.join(base_path, 'ri-3gram-400-tsv/filtered_embeddings.tsv'), 'w')
    writer = csv.writer(csvf, delimiter='\t')
    pretrained_filtered = {}
    writer.writerow(['pad']+list(pretrained['pad']))
    writer.writerow(['unknown']+list(pretrained['unknown']))
    for _,word in enumerate(vocab):
        vec = pretrained.get(word, None)
        if vec is not None:
            writer.writerow([word]+list(pretrained[word]))
    csvf.close()

if __name__ == "__main__":
    num_labels = 5
    #reading -> sort by date, remove de-id, puncts, tokenize , stopwords
    print("Reading data")
    rawdata = read_data_dump(os.path.join(base_path, 'notes_dump_small.pkl'))
    print("data size:", len(rawdata))
    print("Filtering labels")
    labels = filter_labels(rawdata, num_labels)
    f = open(os.path.join(base_path, 'labels.txt'), 'w')
    for la in labels:
        # print >>f, la
        f.write(la + '\n')
    f.close()
    print("num labels:", len(labels))
    print("Selected labels: {}".format(labels))
    print("filter_data_by_labels")
    print("Num data points: {}".format(len(rawdata)))
    rawdata = filter_data_by_labels(rawdata, labels)
    print("data size:", len(rawdata))
    print("vocab...")
    vocab = get_vocab(rawdata)
    print("Vocab size:", len(vocab))
    print(vocab[:200])
    print('postoperative' in vocab, 'amiodarone' in vocab, 'auscultation' in vocab)
    f = open(os.path.join(base_path, 'filtered_vocab_10000.txt'), 'w')
    for v in vocab:
        f.write(v + '\n')
    f.close()
    num_to_check = 200
    raw_lengths = []
    for i in range(min(num_to_check, len(rawdata))):
        raw_lengths.append(count_length(rawdata[i]))
    # pprint.pprint(rawdata[48])
    print("filter_data_by_vocab")
    rawdata = filter_data_by_vocab(rawdata, vocab)
    print("Counting unks...")
    count_unk(rawdata)
    print("Raw data filtered by vocab: ")
    print("Lengths ratio...")
    processed_lengths = []
    for i in range(min(num_to_check, len(rawdata))):
        processed_lengths.append(count_length(rawdata[i]))
    ratio = []
    for i in range(len(processed_lengths)):
        ratio.append(processed_lengths[i] / (raw_lengths[i] * 1.))
    print("Avg ratio of lengths: {} min: {} max: {} argmax: {} std dev: {}".format(
        np.mean(ratio), min(ratio), max(ratio), np.argmax(ratio), np.std(ratio)))
    print("Average raw length: {}, average processed length: {}".format(
        np.mean(raw_lengths), np.mean(processed_lengths)))
    f = open(os.path.join(base_path, 'notes_dump_cleaned_puncts.pkl'), 'wb')
    pickle.dump({'data':rawdata}, f)
    f.close()

    #print "filter_embeddings"

    #f = open(os.path.join(base_path, 'filtered_vocab_10000.txt'), 'r')
    #vocab = []
    #for line in f.readlines():
    #    vocab.append(line.replace('\n', ''))

    #filter_embeddings(vocab)
