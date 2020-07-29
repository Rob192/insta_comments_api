"""
This is a simple application for sentence embeddings: semantic search
We have a corpus with various sentences. Then, for a given query sentence,
we want to find the most similar sentence in this corpus.
This script outputs for various queries the top 5 most similar sentences in the corpus.
"""
from sentence_transformers import SentenceTransformer, util

"""
This is a simple application for sentence embeddings: semantic search
We have a corpus with various sentences. Then, for a given query sentence,
we want to find the most similar sentence in this corpus.
This script outputs for various queries the top 5 most similar sentences in the corpus.
"""


class CommentFinder:
    def __init__(self):
        self.embedder = SentenceTransformer('distiluse-base-multilingual-cased')

        # Corpus with example sentences
        self.corpus = ["j'adore cette photo",
                       "oh ma pauvre, c'est trop triste",
                       "vous êtes adorables",
                       "oh mon pauvre, c'est trop triste",
                       "tu es trop belle !",
                       "C'est canon. Tu es une super maman !",
                       "J'adore la déco",
                       "Cette mise en scène est géniale",
                       "J'adore la mise en scène",
                       "Trop belle la déco sur cette photo !",
                       "Tellement CANON !!",
                       "Des très bons goûts, comme d'habitude !",
                       "Très belle décoration",
                       "Trop trop choupi :) :) ",
                       "mmmm il a l'air trop bon ce gâteau !",
                       "ce jeu est trop trop drôle !!!",
                       "J'adore ce jeu !!",
                       "ton petit bout de chou est trop mignon !",
                       "Adorable !",
                       "J'ai besoin de la recette de ce gateau !",
                       "Oh oui le temps passe si vite c’est fou ..",
                       "Il est déjà grand !",
                       'Trop beau'
                       ]

        self.corpus_embeddings = self.embedder.encode(self.corpus, convert_to_tensor=True)

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
        # TODO : only return this if score is above certain threshold
        return {'comment': self.corpus[idx].strip(), 'score': score}


if __name__ == '__main__':
    commentFinder = CommentFinder()
    sentence = "Tu es trop belle !"
    comment = commentFinder.find_comment(sentence)
    print(comment)
