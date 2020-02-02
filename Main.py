from textgenrnn import textgenrnn

def runTextGen():
    textgen = textgenrnn(weights_path='/home/sasraf0/McStoryGen5am/Test3_weights.hdf5',
    vocab_path='/home/sasraf0/McStoryGen5am/Test3_vocab.json',
    config_path='/home/sasraf0/McStoryGen5am/Test3_config.json')

    textgen.generate_samples(max_gen_length=1000)
    textgen.generate_to_file('/home/sasraf0/McStoryGen5am/textgenrnn_texts.txt', max_gen_length=1000)
