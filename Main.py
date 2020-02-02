from textgenrnn import textgenrnn
textgen = textgenrnn(weights_path='Test3_weights.hdf5',
                       vocab_path='Test3_vocab.json',
                       config_path='Test3_config.json')

textgen.generate_samples(max_gen_length=1000)
textgen.generate_to_file('textgenrnn_texts.txt', max_gen_length=1000)
#let's try this