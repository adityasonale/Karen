import pickle

def Load_tokenizer():
    with open(r'D:\vs code\python\DeepLearning\Projects\Karen\v2\Pickles\my_tokenizer.picklev2','rb') as file:
        tokenizer = pickle.load(file)
        file.close()
    return tokenizer

def Load_tokenizer_func():
    with open(r'D:\vs code\python\DeepLearning\Projects\Karen\v2\Pickles\functional\my_tokenizer_functional.pickle','rb') as file:
        tokenizer = pickle.load(file)
        file.close()
    return tokenizer

def Load_tokenizer_non_func():
    with open(r'D:\vs code\python\DeepLearning\Projects\Karen\v2\Pickles\non_functional\my_tokenizer_non_functional.pickle','rb') as file:
        tokenizer = pickle.load(file)
        file.close()
    return tokenizer

# def Load_labels():
#     with open(r'D:\vs code\python\DeepLearning\Projects\Karen\v2\Pickles\labels.pickle','rb') as file:
#         labels = pickle.load(file)
#     return labels

def Load_labels_func():
    with open(r'D:\vs code\python\DeepLearning\Projects\Karen\v2\Pickles\functional\labels_functional.pickle','rb') as file:
        labels = pickle.load(file)
    return labels


def Load_labels_non_func():
    with open(r'D:\vs code\python\DeepLearning\Projects\Karen\v2\Pickles\non_functional\labels_non_functional.pickle','rb') as file:
        labels = pickle.load(file)
        return labels


def Load_maxlen():
    with open(r'D:\vs code\python\DeepLearning\Projects\Karen\v2\Pickles\padding_lengthv2.pickle','rb') as file:
        padding_length = pickle.load(file)
    return padding_length

def Load_maxlen_non_func():
    with open(r'D:\vs code\python\DeepLearning\Projects\Karen\v2\Pickles\non_functional\padding_length_non_functional.pickle','rb') as file:
        padding_length = pickle.load(file)
    return padding_length

def Load_maxlen_func():
    with open(r'D:\vs code\python\DeepLearning\Projects\Karen\v2\Pickles\functional\padding_length_functional.pickle','rb') as file:
        padding_length = pickle.load(file)
    return padding_length
