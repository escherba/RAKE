import atexit
import argparse
import rake
from operator import itemgetter


def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', action='store_true')
    namespace = parser.parse_args()
    return namespace


def quit_repl():
    print 'Bye'


PROMPT_STR = "%s> " % __package__


def main(args):
    atexit.register(quit_repl)
    rake_instance = rake.Rake()
    while True:
        print '-' * 80
        try:
            text = raw_input('Enter text to analyze\n%s' % PROMPT_STR)
        except EOFError:
            # Exit gracefully on Ctrl-D
            break

        # Split text into sentences
        sentenceList = rake.split_sentences(text)
        stopwordpattern = rake.build_stop_word_regex()

        # generate candidate keywords
        phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern)

        # calculate individual word scores
        wordscores = rake.calculate_word_scores(phraseList)

        # generate candidate keyword scores
        keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)
        if args.verbose:
            print keywordcandidates

        sortedKeywords = sorted(keywordcandidates.iteritems(), key=itemgetter(1), reverse=True)
        if args.verbose:
            print sortedKeywords

        totalKeywords = len(sortedKeywords)
        if args.verbose:
            print totalKeywords
        print sortedKeywords[0:(totalKeywords / 3)]

        keywords = rake_instance.run(text)
        print keywords


if __name__ == "__main__":
    main(parse_args())
