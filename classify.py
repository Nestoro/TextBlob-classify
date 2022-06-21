
import argparse

args_parser = argparse.ArgumentParser(description='Run TextBlob classification for a file with text lines')

args_parser.add_argument('--input', type=str, help='input file', required=True)
args_parser.add_argument('--output', type=str, help='output file', required=True)
args_parser.add_argument('--mode', type=str, help='mode of row conversion default: calculate average of all sentencens in each row', required=False)
args_parser.add_argument('--language', type=str, help='language (en,de)', required=True)




args = args_parser.parse_args()

output_path = args.output
input_path = args.input
lang = args.language

inputFile = open(input_path, 'r')
OutputFile = open(output_path, 'w')

OutputFile.flush()

Lines = inputFile.readlines()

if (lang == 'de'):
    from textblob_de import TextBlobDE as TextBlob
else:
    from textblob import TextBlob

for line in Lines:
    blob = TextBlob(line);
    sentimentSum = 0
    for sentence in blob.sentences:
        sentimentSum += sentence.sentiment.polarity + 1
    sentiment = round(sentimentSum / len(blob.sentences)) - 1
    OutputFile.write(str(sentiment) + '\n')

inputFile.close()
OutputFile.close()