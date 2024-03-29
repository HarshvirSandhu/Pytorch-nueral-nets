import torch
import torchtext

text = torchtext.data.Field(sequential=True, use_vocab=True, tokenize='spacy', tokenizer_language='en_core_web_sm')
label = torchtext.data.LabelField(dtype=torch.long)
fields = [('Label', label), ('Text', text)]
path_data = "C:/Users/harsh/Downloads/SpamClassifier-master/SpamClassifier-master/smsspamcollection/" \
            "SMSSpamCollection"
data_set = torchtext.data.TabularDataset(path=path_data, format='tsv', fields=fields, skip_header=True)
text.build_vocab(data_set, max_size=5000)
label.build_vocab(data_set)

data_load = torchtext.data.BucketIterator(data_set, batch_size=32)
print(label.vocab.stoi)
for data in data_load:
    # data.Text.shape: [len, batch_size], data.Text[i] is not the ith sentence of the batch. BUT data.Text.T[i] is the ith sentence of the batch
    print(data)
    print(label.vocab.itos[int(data.Label.T[0].item())])
    for i in list(data.Text.T[0]):
        print(text.vocab.itos[i], end=' ')
    break
