from client import DamerauLevenshteinMatcher

def main():
    matcher = DamerauLevenshteinMatcher()
    query = "recieved"
    choices = ["received", "receive", "relieved", "deceived"]
    ranks = matcher.rank_candidates(query, choices)
    print("Damerau-Levenshtein Fuzzy Matcher Verification:")
    print(f"Query: '{query}'")
    for r in ranks:
        print(f"  Candidate: {r['candidate']} -> Dist: {r['distance']}, Sim: {r['similarity']}")

if __name__ == "__main__":
    main()
