"""
This is a simple application for sentence embeddings: semantic search
We have a corpus with various sentences. Then, for a given query sentence,
we want to find the most similar sentence in this corpus.
This script outputs for various queries the top 5 most similar sentences in the corpus.
"""
from sentence_transformers import SentenceTransformer, util

class CommentFinder:
    def __init__(self):
        self.embedder = SentenceTransformer('bert-base-nli-mean-tokens')

        # Corpus with example sentences
        corpus = ['A man is eating food.',
                  'A man is eating a piece of bread.',
                  'The girl is carrying a baby.',
                  'A man is riding a horse.',
                  'A woman is playing violin.',
                  'Two men pushed carts through the woods.',
                  'A man is riding a white horse on an enclosed ground.',
                  'A monkey is playing drums.',
                  'A cheetah is running behind its prey.'
                  ]
        self.corpus_embeddings = self.embedder.encode(corpus, convert_to_tensor=True)

    def find_comment(self, query):
        query_embedding = self.embedder.encode(query, convert_to_tensor=True)
        scores = util.pytorch_cos_sim(query_embedding, self.corpus_embeddings)[0]

        results = zip(range(len(scores)), scores)
        results = sorted(results, key=lambda x: x[1], reverse=True)

        print("\n\n======================\n\n")
        print("Query:", query)
        print("\nMost similar sentences in corpus:")

        idx, score = results[0]
        print(self.corpus[idx].strip(), "(Score: %.4f)" % (score))
        #TODO : only return this if score is above certain threshold
        return self.corpus[idx].strip()

if __name__ == '__main__':
    commentFinder = CommentFinder()
    sentence = "A man is eating a hamburger"
    comment = commentFinder.find_comment(sentence)
    print(comment)