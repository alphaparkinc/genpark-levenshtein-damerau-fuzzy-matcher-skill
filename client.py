"""Damerau-Levenshtein Fuzzy Matcher Engine
100% Python Standard Library.
"""

class DamerauLevenshteinMatcher:
    """True Damerau-Levenshtein metric supporting adjacent transpositions."""
    def distance(self, s1, s2):
        d = {}
        len1, len2 = len(s1), len(s2)
        for i in range(-1, len1 + 1):
            d[(i, -1)] = i + 1
        for j in range(-1, len2 + 1):
            d[(-1, j)] = j + 1

        for i in range(len1):
            for j in range(len2):
                cost = 0 if s1[i] == s2[j] else 1
                d[(i, j)] = min(
                    d[(i - 1, j)] + 1,
                    d[(i, j - 1)] + 1,
                    d[(i - 1, j - 1)] + cost
                )
                if i > 0 and j > 0 and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                    d[(i, j)] = min(d[(i, j)], d[(i - 2, j - 2)] + 1)

        return d[(len1 - 1, len2 - 1)]

    def similarity_ratio(self, s1, s2):
        dist = self.distance(s1, s2)
        max_len = max(len(s1), len(s2))
        return round(1.0 if max_len == 0 else 1.0 - (dist / max_len), 4)

    def rank_candidates(self, query, candidates, top_k=5):
        ranked = []
        for c in candidates:
            dist = self.distance(query, c)
            ratio = self.similarity_ratio(query, c)
            ranked.append({"candidate": c, "distance": dist, "similarity": ratio})
        ranked.sort(key=lambda x: x["similarity"], reverse=True)
        return ranked[:top_k]
