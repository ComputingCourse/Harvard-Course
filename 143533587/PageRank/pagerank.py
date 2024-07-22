import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    N = len(corpus)
    links = corpus[page]
    dic = {}
    if len(links) == 0:
        for page in corpus:
            dic[page] = 1/N
        return dic
    for each in corpus:
        dic[each] = float(f"{(1-damping_factor)/N:.10f}")
    for pages in links:
        if pages != page:
            prob = (1/len(links))*damping_factor
            dic[pages] += prob
    return dic


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages = []
    count = {}
    for page in corpus:
        pages.append(page)
        count[page] = 0
    for i in range(n):
        if i != 0:
            probs = transition_model(corpus,page,damping_factor)
            wieght = []
            for i in range(len(pages)):
                wieght.append(probs[pages[i]])
            page =random.choices(pages, weights=wieght, k=1)
            page = page[0]
        else:
            page = random.choice(pages)
        count[page] += 1/n
    return count



def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    for page in corpus:
        if corpus[page] == set():
            for each in corpus:
                corpus[page].add(each)
    links_to_pages = {}
    prev = {}
    for page in corpus:
        links_to_pages[page]= []
        prev[page] = 1/len(corpus)
    for page in corpus:
        for links in corpus[page]:
            links_to_pages[links].append(page)

    while True:
        probs = {}
        for each in prev:#each page
            new = (1 - damping_factor)/len(corpus)
            for every in links_to_pages[each]:#for every page that links to page
                new += damping_factor * (prev[every]/len(corpus[every]))#prev
            probs[each] = new

        count = 0
        for each in prev:
            if float(f"{prev[each]:.3f}") == float(f"{probs[each]:.3f}"):
                count +=1
        if count == len(corpus):
            return  probs
        prev = probs


if __name__ == "__main__":
    main()
